"""Reproducible lab CLI: prepare -> freeze -> ingest -> dev -> test -> audit."""
import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
from importlib.metadata import version
import json
from pathlib import Path
import platform
import time
import traceback

from .ingestion import ROOT, load_corpus, sha256, write_json, write_jsonl
from .chunking import by_paragraph, fixed_size
from .evaluation import comparable, evaluate_query, golds, summarize

CONFIG_PATH = ROOT / 'starter/config.json'
MANIFEST_PATH = ROOT / 'data/manifest.json'
BENCHMARK_PATH = ROOT / 'benchmark/questions.json'
PLAN_PATH = ROOT / 'benchmark/frozen_plan.json'


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def now():
    return datetime.now(timezone.utc).isoformat()


def inputs():
    return {p.relative_to(ROOT).as_posix(): sha256(p) for p in [CONFIG_PATH, MANIFEST_PATH, BENCHMARK_PATH]}


def same_inputs(hashes):
    # Original run was on Windows. Preserve its signed/dated artifacts while
    # accepting equivalent relative paths on Linux and macOS replications.
    return {k.replace('\\','/'):v for k,v in hashes.items()} == inputs()


def check_frozen():
    plan = read_json(PLAN_PATH)
    if not same_inputs(plan['input_sha256']):
        raise ValueError('Frozen inputs changed. Start a documented new experiment; do not tune on test.')
    return plan


def prepare(output):
    pages, summary = load_corpus(MANIFEST_PATH, output)
    originals = {(p['document_id'], p['page']): p for p in
                 map(json.loads, (ROOT / 'data/processed/pages.jsonl').read_text(encoding='utf-8').splitlines())}
    questions = read_json(BENCHMARK_PATH)
    if len({q['id'] for q in questions}) != len(questions):
        raise ValueError('Duplicate question IDs')
    splits = Counter(q['split'] for q in questions)
    if splits['dev'] < 15 or splits['test'] < 5 or set(splits) != {'dev', 'test'}:
        raise ValueError('Need >=15 dev and >=5 test')
    filter_counts = Counter(q['split'] for q in questions if q.get('filter'))
    if sum(filter_counts.values()) < 3 or filter_counts['test'] < 1:
        raise ValueError('Need >=3 filtered questions, including >=1 test')
    validations = []
    for q in questions:
        for g in golds(q):
            page = originals[(g['gold_source_id'], g['gold_page'])]
            if not g['evidence_quote'].strip() or comparable(g['evidence_quote']) not in comparable(page['text']):
                raise ValueError(f'Evidence not found: {q["id"]}')
            # All gold alternatives for filtered questions must match the stated
            # chapter, checked against the actual text segments, not the answer.
            if q.get('filter'):
                candidates = [p for p in pages if p.document_id == g['gold_source_id']
                              and p.page == g['gold_page'] and
                              comparable(g['evidence_quote']) in comparable(p.text)]
                if not any(all(p.metadata.get(k) == v for k,v in q['filter'].items()) for p in candidates):
                    raise ValueError(f'Gold outside supplied filter: {q["id"]}')
            validations.append({'question_id': q['id'], 'source_id': g['gold_source_id'],
                                'page': g['gold_page'], 'exact_evidence_present': True})
    positions = [{'sample_id': f'P{i:02d}', 'document_id': p['document_id'], 'page': p['page'],
                  'char_offset': len(p['text'])//2}
                 for i,p in enumerate(sorted(originals.values(), key=lambda p: (p['document_id'],p['page']))[:10],1)]
    write_json(output / 'benchmark_validation.json', {'splits': splits, 'filter_counts': filter_counts,
                                                     'evidence_checks': validations})
    return pages, positions, summary


def freeze(output):
    _, positions, _ = prepare(output)
    if PLAN_PATH.exists():
        check_frozen()
        print('Existing frozen plan verified', flush=True)
        return
    config = read_json(CONFIG_PATH)
    write_json(PLAN_PATH, {'frozen_at_utc': now(), 'input_sha256': inputs(),
                          'selection_rule': config['selection_rule'], 'audit_rule': config['audit_rule'],
                          'coherence_positions': positions,
                          'split_method': 'Q01-Q15 dev; Q16-Q20 test. Topic overlap exists within one law. Authored before retrieval. Test answers known during benchmark design, test retrieval scores hidden until dev choice saved.',
                          'human_audit_status': 'AI-authored evidence and draft reviews; student must independently verify and sign manual labels.'})
    print('Experiment frozen before retrieval', flush=True)


def get_embedder(config):
    from .embeddings import MyEmbedder
    return MyEmbedder(config['model_name'], config['model_revision'], ROOT / 'artifacts/models/hub')


def get_store(config, path):
    from .store import ChromaStore
    fingerprint = f'{config["model_name"]}@{config["model_revision"]}:max256:normalized'
    return ChromaStore(path, config['dimensions'], fingerprint)


def ingest(output, store_path):
    check_frozen()
    pages, _, _ = prepare(output)
    config = read_json(CONFIG_PATH)
    t0 = time.perf_counter()
    embedder = get_embedder(config)
    if embedder.dimensions != config['dimensions']:
        raise ValueError('Actual model dimensions do not match the frozen configuration')
    load_seconds = time.perf_counter()-t0
    store = get_store(config, store_path)
    stats, all_chunks = [], {}
    for strategy in ('A', 'B'):
        t0 = time.perf_counter()
        spec = config['strategies'][strategy]
        chunks = [c for p in pages for c in (fixed_size(p, spec['size'], spec['overlap']) if strategy == 'A'
                                             else by_paragraph(p, spec['max_size']))]
        texts = [c.text for c in chunks]
        tokens = embedder.token_counts(texts)
        vectors, cached = embedder.cached_documents(texts, ROOT / 'artifacts/cache/embeddings')
        first = store.upsert(strategy, chunks, vectors)
        ingest_seconds = time.perf_counter()-t0
        reload_start = time.perf_counter()
        repeated = store.upsert(strategy, chunks, vectors)
        if repeated['before'] != len(chunks) or repeated['after'] != len(chunks):
            raise AssertionError('Reload changed count')
        lengths = sorted(map(len, texts))
        row = {'strategy': strategy, 'chunk_count': len(chunks),
               'total_characters': sum(lengths), 'min_characters': min(lengths),
               'median_characters': lengths[len(lengths)//2], 'max_characters': max(lengths),
               'p95_characters': lengths[int((len(lengths)-1)*.95)],
               'total_input_tokens_untruncated': sum(tokens), 'max_input_tokens': max(tokens),
               'truncated_chunks': sum(n > 256 for n in tokens), 'max_seq_length': 256,
               'embedding_cache_hit': cached, 'ingest_seconds': ingest_seconds,
               'model_load_seconds_shared': load_seconds,
               'reload_seconds': time.perf_counter()-reload_start,
               'first_upsert': first, 'repeat_upsert': repeated, 'api_cost_usd': 0,
               'metric': 'cosine', 'index': 'Chroma HNSW approximate', 'model_dimensions': embedder.dimensions}
        stats.append(row)
        all_chunks[strategy] = [asdict(c) for c in chunks]
        write_jsonl(output / f'chunks_{strategy}.jsonl', all_chunks[strategy])
        print(f'{strategy}: {len(chunks)} chunks, {ingest_seconds:.2f}s, reload count OK', flush=True)
    stats.append(dict(stats[1]) | {'strategy': 'C', 'shared_index': 'B', 'ingest_seconds': 0,
                                  'reload_seconds': 0, 'embedding_cache_hit': True})
    write_json(output / 'index_stats.json', stats)
    versions = {name: version(name) for name in ['chromadb','sentence-transformers','transformers','torch',
                                                'numpy','PyMuPDF','huggingface-hub']}
    write_json(output / 'environment.json', {'python': platform.python_version(), 'platform': platform.platform(),
                                           'packages': versions, 'config': config, 'started_at_utc': now(),
                                           'inputs': inputs(), 'store_path': str(store_path)})


def benchmark(split, output, store_path):
    check_frozen()
    config = read_json(CONFIG_PATH)
    if split == 'test':
        selection = read_json(output / 'selection.json')
        if not same_inputs(selection['input_sha256']):
            raise ValueError('Selection does not match frozen inputs')
        if (output / 'traces_test.jsonl').exists():
            raise ValueError('Test already evaluated in this output. Use a new output for a declared replication.')
    elif (output / 'traces_test.jsonl').exists():
        raise ValueError('Do not reselect after seeing test. Use a new output for replication.')
    embedder = get_embedder(config)
    store = get_store(config, store_path)
    questions = [q for q in read_json(BENCHMARK_PATH) if q['split'] == split]
    vectors = embedder.embed_documents([q['question'] for q in questions])
    traces = []
    for strategy in ('A','B','C'):
        for question, vector in zip(questions, vectors):
            filters = question.get('filter', {}) if strategy == 'C' else {}
            t0 = time.perf_counter()
            hits = store.search(strategy, vector, config['top_k'], filters)
            trace = evaluate_query(question, hits) | {'strategy': strategy, 'applied_filter': filters,
                    'search_seconds': time.perf_counter()-t0, 'executed_at_utc': now()}
            traces.append(trace)
    write_jsonl(output / f'traces_{split}.jsonl', traces)
    metrics = summarize(traces)
    write_json(output / f'metrics_{split}.json', metrics)
    if split == 'dev':
        counts = {r['strategy']: r['chunk_count'] for r in read_json(output / 'index_stats.json')}
        chosen = sorted(metrics, key=lambda r: (-r['hit3_count'], -r['hit1_count'],
                                                counts[r['strategy']], r['strategy']))[0]['strategy']
        write_json(output / 'selection.json', {'chosen_strategy': chosen, 'selected_at_utc': now(),
                   'input_sha256': inputs(), 'rule': config['selection_rule'], 'dev_metrics': metrics,
                   'test_evaluated_at_selection': False})
    print(json.dumps(metrics, ensure_ascii=False), flush=True)


def audit_templates(output):
    plan = check_frozen()
    samples = []
    for strategy in ('A','B','C'):
        chunk_path = output / f'chunks_{"B" if strategy == "C" else strategy}.jsonl'
        chunks = [json.loads(line) for line in chunk_path.read_text(encoding='utf-8').splitlines()]
        for position in plan['coherence_positions']:
            choices = [c for c in chunks if c['document_id'] == position['document_id'] and
                       c['page'] == position['page'] and
                       c['metadata']['char_start'] <= position['char_offset'] < c['metadata']['char_end']]
            if not choices:
                raise ValueError(f'Anchor not covered: {position}')
            chosen = min(choices, key=lambda c: (c['metadata']['char_start'],c['chunk_id']))
            samples.append(dict(position) | {'strategy': strategy, 'chunk': chosen,
                                            'score': None, 'reason': '', 'reviewer': '',
                                            'review_status': 'pending_human'})
    write_json(output / 'coherence_samples.json', samples)
    traces = [json.loads(line) for line in (output / 'traces_test.jsonl').read_text(encoding='utf-8').splitlines()]
    write_json(output / 'grounding_samples.json', [dict(t) | {'grounding_score': None, 'reason': '',
                                                             'reviewer': '', 'review_status': 'pending_human'}
                                                   for t in traces])
    metadata = []
    for trace in traces:
        for rank, hit in enumerate(trace['hits'],1):
            metadata.append({'strategy': trace['strategy'], 'question_id': trace['question_id'], 'rank': rank,
                             'chunk_id': hit['chunk_id'], 'metadata': hit['metadata'], 'text': hit['text'],
                             'complete_and_correct': None, 'reason': '', 'reviewer': '',
                             'review_status': 'pending_human'})
    write_json(output / 'metadata_samples.json', metadata)
    print('Prepared 30 coherence, 15 grounding and 45 metadata records for manual review', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare','freeze','ingest','dev','test','audit','query','all'],
                        default='all', nargs='?')
    parser.add_argument('--output', type=Path, default=ROOT / 'results/run')
    parser.add_argument('--store', type=Path, default=ROOT / 'artifacts/chroma')
    parser.add_argument('--question', default='Khi nào phải bật đèn chiếu sáng phía trước?')
    parser.add_argument('--strategy', choices=['A','B','C'], default='C')
    parser.add_argument('--section', default=None)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        if args.command in {'ingest','all'} and (args.output/'traces_test.jsonl').exists():
            raise ValueError('This run already has test results. Preserve its artifacts; specify a new --output for replication.')
        if args.command in {'prepare','all'}:
            prepare(args.output)
        if args.command in {'freeze','all'}:
            freeze(args.output)
        if args.command in {'ingest','all'}:
            ingest(args.output, args.store)
        for split in ('dev','test'):
            if args.command in {split,'all'}:
                benchmark(split, args.output, args.store)
        if args.command in {'audit','all'}:
            audit_templates(args.output)
        if args.command == 'query':
            check_frozen()
            config = read_json(CONFIG_PATH)
            embedder = get_embedder(config)
            filters = {'section': args.section} if args.section and args.strategy == 'C' else {}
            print(json.dumps(get_store(config, args.store).search(args.strategy,
                  embedder.embed_query(args.question), 3, filters), ensure_ascii=False, indent=2))
    except Exception as error:
        write_json(args.output / 'last_error.json', {'at_utc': now(), 'command': args.command,
                   'error_type': type(error).__name__, 'message': str(error), 'traceback': traceback.format_exc()})
        raise


if __name__ == '__main__':
    main()
