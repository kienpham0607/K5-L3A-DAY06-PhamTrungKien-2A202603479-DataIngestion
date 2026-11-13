"""Strict whole-evidence hits; do not infer manual audit labels from a hit."""
from collections import defaultdict
from typing import Any
import unicodedata


def comparable(text: str) -> str:
    return ' '.join(unicodedata.normalize('NFC', text).split())


def golds(question: dict) -> list[dict]:
    primary = {k: question[k] for k in ('gold_source_id', 'gold_page', 'evidence_quote')}
    return [primary, *question.get('alternative_gold', [])]


def evidence_hit(question: dict, hit: dict) -> bool:
    metadata = hit['metadata']
    return any(metadata['document_id'] == g['gold_source_id'] and metadata['page'] == g['gold_page']
               and comparable(g['evidence_quote']) in comparable(hit['text']) for g in golds(question))


def evaluate_query(question: dict[str, Any], hits: list[dict[str, Any]]) -> dict[str, Any]:
    retrieved = [dict(h) | {'evidence_hit': evidence_hit(question, h)} for h in hits[:3]]
    return {'question_id': question['id'], 'split': question['split'], 'question': question['question'],
            'expected_answer': question['expected_answer'], 'gold': golds(question),
            'requested_filter': question.get('filter', {}), 'hits': retrieved,
            'hit1': bool(retrieved and retrieved[0]['evidence_hit']),
            'hit3': any(h['evidence_hit'] for h in retrieved)}


def summarize(traces: list[dict[str, Any]]) -> list[dict]:
    groups = defaultdict(list)
    for trace in traces:
        groups[(trace['strategy'], trace['split'])].append(trace)
    return [{'strategy': strategy, 'split': split, 'n': len(rows),
             'hit1_count': sum(r['hit1'] for r in rows), 'hit3_count': sum(r['hit3'] for r in rows),
             'hit1': sum(r['hit1'] for r in rows)/len(rows),
             'hit3': sum(r['hit3'] for r in rows)/len(rows)}
            for (strategy, split), rows in sorted(groups.items())]
