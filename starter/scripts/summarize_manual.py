"""Validate student-signed manual CSVs and summarize only genuinely filled labels."""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from starter.src.ingestion import write_json


def summarize(directory):
    records={}
    pending=[]
    for kind,total in [('coherence',30),('grounding',15),('metadata',45)]:
        with (directory/f'manual_{kind}.csv').open(encoding='utf-8-sig',newline='') as handle:
            rows=list(csv.DictReader(handle))
        if len(rows)!=total:
            raise ValueError(f'{kind}: expected {total} rows')
        key_fields=['strategy','sample_id'] if kind=='coherence' else (
            ['strategy','question_id','rank'] if kind=='metadata' else ['strategy','question_id'])
        keys=[tuple(row[k] for k in key_fields) for row in rows]
        with (directory/f'ai_{kind}.csv').open(encoding='utf-8-sig',newline='') as handle:
            reference=list(csv.DictReader(handle))
        expected={tuple(row[k] for k in key_fields):row for row in reference}
        if len(set(keys))!=total or set(keys)!=set(expected):
            raise ValueError(f'{kind}: duplicate/missing/wrong sample identities')
        for row,key in zip(rows,keys):
            fields=['document_id','page','char_offset','chunk_id'] if kind=='coherence' else (
                ['chunk_id','source','page','section'] if kind=='metadata' else [])
            if any(row[field]!=expected[key][field] for field in fields):
                raise ValueError(f'{kind}: source/sample identity was changed for {key}')
        label='complete_and_correct' if kind=='metadata' else 'score'
        for row in rows:
            if (row['status']!='human_verified' or not row['reviewer'].strip() or
                not row['reason'].strip() or row[label]==''):
                pending.append(f'{kind}:{row["strategy"]}:{row.get("sample_id",row.get("question_id"))}:{row.get("rank","")}')
            elif kind=='metadata' and row[label].lower() not in {'true','false'}:
                raise ValueError('Metadata labels must be True/False')
            elif kind!='metadata' and row[label] not in {'0','1','2'}:
                raise ValueError('Scores must be 0/1/2')
        records[kind]=rows
    if pending:
        result={'status':'pending_human','pending_rows':len(pending),'required_rows':90,
                'pending_ids':pending,'manual_metrics':None}
    else:
        metrics=[]
        for strategy in 'ABC':
            cs=[int(r['score']) for r in records['coherence'] if r['strategy']==strategy]
            gs=[int(r['score']) for r in records['grounding'] if r['strategy']==strategy]
            ms=[r['complete_and_correct'].lower()=='true' for r in records['metadata'] if r['strategy']==strategy]
            if (len(cs),len(gs),len(ms))!=(10,5,15):
                raise ValueError('Wrong strategy sample sizes')
            metrics.append({'strategy':strategy,'coherence_mean':sum(cs)/len(cs),
                            'grounding_distribution':dict(Counter(gs)),'grounding_mean':sum(gs)/len(gs),
                            'metadata_correct':sum(ms),'metadata_n':len(ms)})
        result={'status':'human_verified','pending_rows':0,'required_rows':90,'manual_metrics':metrics}
    result['reviewers']=sorted({row['reviewer'] for rows in records.values() for row in rows if row['reviewer'].strip()})
    receipt=directory/'human_confirmation.json'
    if receipt.exists():
        confirmation=json.loads(receipt.read_text(encoding='utf-8'))
        result['confirmation_record']='results/audit/human_confirmation.json'
        result['review_mode']=confirmation['review_mode']
        result['ai_assisted']=confirmation['ai_assisted']
        result['independent_blind_review']=confirmation['independent_blind_review']
    write_json(directory/'manual_summary.json',result)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,default=ROOT/'results/audit')
    result=summarize(parser.parse_args().directory)
    print('Manual status:',result['status'],'pending rows:',result['pending_rows'])
