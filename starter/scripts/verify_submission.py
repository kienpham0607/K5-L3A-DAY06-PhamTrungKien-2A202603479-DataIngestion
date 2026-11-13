"""Recompute artifact consistency without rerunning/tuning the benchmark."""
import json
from pathlib import Path
import sys
from datetime import datetime

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from starter.src.run import check_frozen, read_json
from starter.src.evaluation import evaluate_query, summarize
from starter.src.ingestion import sha256, write_json


def main():
    check_frozen()
    questions={q['id']:q for q in read_json(ROOT/'benchmark/questions.json')}
    out=ROOT/'results/run'
    traces=[]
    for split,expected in [('dev',45),('test',15)]:
        rows=[json.loads(l) for l in (out/f'traces_{split}.jsonl').read_text(encoding='utf-8').splitlines()]
        assert len(rows)==expected
        for row in rows:
            recomputed=evaluate_query(questions[row['question_id']],row['hits'])
            assert (recomputed['hit1'],recomputed['hit3'])==(row['hit1'],row['hit3'])
            assert len(row['hits'])==3
        assert summarize(rows)==read_json(out/f'metrics_{split}.json')
        traces.extend(rows)
    assert len({(r['strategy'],r['question_id']) for r in traces})==60
    # C cannot differ from B without an explicit input filter.
    index={(t['strategy'],t['question_id']):t for t in traces}
    for qid,q in questions.items():
        b,c=index['B',qid],index['C',qid]
        if not q.get('filter'):
            assert b['hits']==c['hits']
        else:
            assert all(all(h['metadata'][k]==v for k,v in q['filter'].items()) for h in c['hits'])
    selected=read_json(out/'selection.json')
    first_test=min(datetime.fromisoformat(r['executed_at_utc']) for r in traces if r['split']=='test')
    assert datetime.fromisoformat(selected['selected_at_utc']) < first_test
    assert datetime.fromisoformat(read_json(ROOT/'benchmark/frozen_plan.json')['frozen_at_utc']) < datetime.fromisoformat(selected['selected_at_utc'])
    stats=read_json(out/'index_stats.json')
    counts={r['strategy']:r['chunk_count'] for r in stats}
    winner=sorted(selected['dev_metrics'],key=lambda r:(-r['hit3_count'],-r['hit1_count'],counts[r['strategy']],r['strategy']))[0]['strategy']
    assert winner==selected['chosen_strategy']
    for row in stats[:2]:
        assert row['repeat_upsert']['before']==row['repeat_upsert']['after']==row['chunk_count']
    assert read_json(out/'ingestion.json')['content_pages']>=30
    for document in read_json(ROOT/'data/manifest.json')['documents']:
        assert sha256(ROOT/document['local_path'])==document['sha256']
    from starter.scripts.summarize_manual import summarize as summarize_manual
    manual=summarize_manual(ROOT/'results/audit')
    evidence=read_json(ROOT/'results/audit/evidence_review.json')
    evidence_done=(evidence.get('human_status')=='human_verified' and len(evidence['rows'])==20 and
                   all(r.get('human_status')=='human_verified' and r.get('answer_supported_human')
                       for r in evidence['rows']))
    if manual['status']=='human_verified' or evidence_done:
        from starter.scripts.record_confirmed_review import verified_receipt
        verified_receipt()
    local_complete=manual['status']=='human_verified' and evidence_done
    result={'technical_artifacts_consistent':True,'queries':60,'retrieved_records':180,
            'chosen_on_dev_before_test':winner,'unfiltered_B_C_identical':True,
            'manual_audit_status':manual['status'], 'evidence_human_verified':evidence_done,
            'local_lab_artifacts_complete':local_complete,
            'ready_for_full_lab_submission':False,
            'remaining_external_steps':['final commit','push completed work','submit repo URL through class channel'],
            'external_submission_status':'Student must verify repo access, create final commit and submit repo URL through class channel.'}
    write_json(ROOT/'results/verification.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
