"""Compare a declared replication to original measured scores, without tuning."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from starter.src.ingestion import write_json


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replica',type=Path,default=ROOT/'artifacts/runs/reproduction')
    args=parser.parse_args()
    def read(path):
        return json.loads(path.read_text(encoding='utf-8'))
    original=ROOT/'results/run'
    checks={split:read(original/f'metrics_{split}.json')==read(args.replica/f'metrics_{split}.json')
            for split in ('dev','test')}
    for strategy in 'AB':
        checks[f'chunks_{strategy}_identical']=((original/f'chunks_{strategy}.jsonl').read_bytes()==
                                               (args.replica/f'chunks_{strategy}.jsonl').read_bytes())
    original_selection=read(original/'selection.json')
    replica_selection=read(args.replica/'selection.json')
    checks['same_dev_choice']=original_selection['chosen_strategy']==replica_selection['chosen_strategy']
    result={'checks':checks,'all_equal':all(checks.values()),
            'replica_output':str(args.replica.relative_to(ROOT)),
            'replica_selected_at_utc':replica_selection['selected_at_utc'],
            'replica_embedding_cache_hits':{r['strategy']:r['embedding_cache_hit'] for r in read(args.replica/'index_stats.json')},
            'note':'Declared replication after observing original test; no retuning, same frozen inputs. Not an independent new holdout. Original first-run metrics/timing preserved.'}
    write_json(ROOT/'results/reproduction_check.json',result)
    assert result['all_equal'], 'Replication differs; preserve both runs and investigate without retuning on test'
    print('Replication: identical chunk dumps, dev/test metrics and dev selection')


if __name__=='__main__':
    main()
