"""Print fixed samples and source context for an explicit qualitative review."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'results/run'
pages = {(p['document_id'],p['page']):p['text'] for p in
         map(json.loads,(ROOT/'data/processed/pages.jsonl').read_text(encoding='utf-8').splitlines())}
print('COHERENCE SAMPLES (C has exactly the same chunks as B)')
for sample in json.loads((OUT/'coherence_samples.json').read_text(encoding='utf-8')):
    if sample['strategy']=='C':
        continue
    print('\n',sample['strategy'],sample['sample_id'],sample['document_id'],sample['page'],
          'offset',sample['char_offset'],'chunk',sample['chunk']['chunk_id'])
    print('CHUNK:',sample['chunk']['text'])
    text=pages[(sample['document_id'],sample['page'])]
    offset=sample['char_offset']
    print('SOURCE CONTEXT:',text[max(0,offset-400):offset+400])
print('\nTEST TRACES')
for trace in map(json.loads,(OUT/'traces_test.jsonl').read_text(encoding='utf-8').splitlines()):
    print('\n',trace['strategy'],trace['question_id'],trace['question'])
    print('GOLD:',trace['gold'])
    for rank,hit in enumerate(trace['hits'],1):
        print('RANK',rank,'SOURCE',hit['metadata']['document_id'],'PAGE',hit['metadata']['page'],
              'CHAPTER',hit['metadata']['section'],'HIT',hit['evidence_hit'])
        print(hit['text'])
