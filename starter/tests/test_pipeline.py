"""Behavioral checks for provenance, evidence metrics and persistent retrieval.

Synthetic unit-test vectors below exercise the database adapter only. They are
never used in the actual corpus/benchmark, which uses the real pinned model.
"""
import json
from pathlib import Path
import unicodedata
import pytest

from starter.src.chunking import by_paragraph, fixed_size
from starter.src.evaluation import evaluate_query, summarize
from starter.src.ingestion import ROOT, load_corpus, normalize_text
from starter.src.models import Chunk, DocumentPage
from starter.src.store import ChromaStore


def test_pdf_line_wraps_and_unicode_keep_conditions():
    text = unicodedata.normalize('NFD', 'CÔNG BÁO/Số 1\n76\nĐiều 1. Quy tắc\n1. Chỉ được đi\nkhi an toàn.\n2. Trừ trường hợp khác.')
    normalized = normalize_text(text)
    assert 'CÔNG BÁO' not in normalized
    assert '1. Chỉ được đi khi an toàn.\n\n2. Trừ trường hợp khác.' in normalized
    assert unicodedata.is_normalized('NFC', normalized)


@pytest.mark.parametrize('chunker', [lambda p: fixed_size(p,80,10), lambda p: by_paragraph(p,100)])
def test_chunk_text_round_trips_to_physical_source_and_ids_stable(chunker):
    text = ('Điều 1. Quy tắc\n\n1. Người lái xe phải quan sát trước khi chuyển hướng.\n\n'
            '2. Khi không bảo đảm an toàn thì phải dừng lại. ' * 4)
    page = DocumentPage('doc','https://example.org/law.pdf',3,text,{'section':'II','page_offset':23})
    chunks = chunker(page)
    assert chunks == chunker(page)
    original = 'x'*23 + text
    covered = set()
    for chunk in chunks:
        start,end = chunk.metadata['char_start'],chunk.metadata['char_end']
        assert original[start:end] == chunk.text
        assert (chunk.page,chunk.metadata['section']) == (3,'II')
        covered.update(range(start-23,end-23))
    assert all(i in covered for i,char in enumerate(text) if not char.isspace())


@pytest.mark.parametrize('size,overlap', [(0,0),(10,10),(10,-1)])
def test_invalid_windows_rejected(size,overlap):
    with pytest.raises(ValueError):
        fixed_size(DocumentPage('d','s',1,'text'),size,overlap)


def test_hit_requires_full_evidence_on_correct_source_page():
    q = {'id':'Q','split':'dev','question':'When?','expected_answer':'After six months',
         'gold_source_id':'doc','gold_page':2,'evidence_quote':'at least six months'}
    def h(text,doc='doc',page=2):
        return {'chunk_id':'c','text':text,'metadata':{'document_id':doc,'page':page}}
    for hit in [h('six months'),h('at least six months','wrong'),h('at least six months',page=3)]:
        assert not evaluate_query(q,[hit])['hit3']
    trace = evaluate_query(q,[h('unrelated'),h('after at least\n six months')])
    assert not trace['hit1'] and trace['hit3']
    q['alternative_gold']=[{'gold_source_id':'other','gold_page':9,'evidence_quote':'six months or longer'}]
    assert evaluate_query(q,[h('six months or longer','other',9)])['hit1']
    trace['strategy']='B'
    summary=summarize([trace])[0]
    assert summary['hit3_count']==1 and summary['n']==1 and summary['hit1_count']==0


def test_persistent_chroma_filters_idempotency_and_changed_corpus(tmp_path):
    store=ChromaStore(tmp_path/'index',3,'unit-test-only')
    chunks=[Chunk('a','d','url',1,'first',{'section':'II'}),
            Chunk('b','d','url',2,'second',{'section':'IV'})]
    vectors=[[1.,0.,0.],[0.8,0.6,0.]]
    store.upsert('B',chunks,vectors)
    assert store.upsert('B',chunks,vectors)['after']==2
    assert store.search('B',[1.,0.,0.])[0]['chunk_id']=='a'
    assert store.search('C',[1.,0.,0.],filters={'section':'IV'})[0]['chunk_id']=='b'
    assert store.search('C',[1.,0.,0.],filters={'section':'missing'})==[]
    with pytest.raises(ValueError):
        store.search('B',[1.,0.,0.],filters={'gold_source_id':'d'})
    with pytest.raises(ValueError):
        store.upsert('B',chunks,[[1.,0.],[1.,0.]])
    changed=store.upsert('B',[chunks[1]],[vectors[1]])
    assert changed['after']==1 and changed['removed_stale']==1
    reopened=ChromaStore(tmp_path/'index',3,'unit-test-only')
    assert reopened.search('B',[1.,0.,0.])[0]['chunk_id']=='b'
    with pytest.raises(ValueError):
        ChromaStore(tmp_path/'index',3,'different-model').collection('B')


def test_real_corpus_chapter_boundary_and_evidence(tmp_path):
    pages,summary=load_corpus(ROOT/'data/manifest.json',tmp_path)
    assert summary['content_pages']==81
    boundary=[p for p in pages if p.document_id=='traffic-law-part1' and p.page==10]
    assert {p.metadata['section'] for p in boundary}=={'I','II'}
    assert 'Điều 10.' not in next(p.text for p in boundary if p.metadata['section']=='I')
    assert 'Điều 10.' in next(p.text for p in boundary if p.metadata['section']=='II')
    assert {p.metadata['section'] for p in pages}=={'I','II','III','IV','V','VI','VII','VIII','IX'}
    questions=json.loads((ROOT/'benchmark/questions.json').read_text(encoding='utf-8'))
    for q in questions:
        assert any(p.document_id==q['gold_source_id'] and p.page==q['gold_page'] and
                   ' '.join(q['evidence_quote'].split()) in ' '.join(p.text.split()) for p in pages)
