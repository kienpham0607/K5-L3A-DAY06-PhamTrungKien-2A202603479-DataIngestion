"""Build source-backed evidence/audit packets. Never attest a student's review."""
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from starter.src.evaluation import comparable
from starter.src.ingestion import normalize_text, sha256, write_json
from starter.src.run import check_frozen

OUT = ROOT / 'results/audit'

# Explicit semantic judgments after reading the physical PDF text, not generated
# by the substring test. The program separately checks quote location/provenance.
SUPPORT = {
    'Q01': ('Điều 9 khoản 2', 'Khoản 2 nằm dưới tiêu đề Các hành vi bị nghiêm cấm. Đáp án có nồng độ cồn là hành vi bị cấm, đúng phạm vi Chương I; cần đọc cả tiêu đề để hiểu tính cấm.'),
    'Q02': ('Điều 2 khoản 6', 'Có đủ phần đường xe chạy, chia theo chiều dọc và chiều rộng cho xe chạy an toàn, khớp định nghĩa trong đáp án.'),
    'Q03': ('Điều 10 khoản 3', 'Nguồn dùng đồng thời hai điều kiện dưới 10 tuổi VÀ thấp hơn 1,35 mét; đủ quy tắc hàng ghế, ngoại lệ ô tô chỉ một hàng ghế và nghĩa vụ dùng/hướng dẫn thiết bị an toàn. Chỉ kiểm tra snapshot gốc.'),
    'Q04': ('Điều 11 khoản 2 điểm a–d', 'Thứ tự bốn loại mà câu hỏi nêu là người điều khiển, đèn, biển báo, vạch đường. Nguồn còn các mục đ/e nhưng câu hỏi không yêu cầu liệt kê tất cả loại báo hiệu.'),
    'Q05': ('Điều 13 khoản 2', 'Giữ đủ nơi cho phép, mỗi lần một làn liền kề, tín hiệu báo trước và quan sát khoảng cách an toàn trước/sau/hai bên.'),
    'Q06': ('Điều 14 khoản 2', 'Vượt trái là quy tắc; ngoại lệ vượt phải gồm xe trước báo rẽ trái/đang rẽ trái hoặc xe chuyên dùng làm việc không thể vượt trái. Không diễn giải là ngoại lệ cho mọi tình huống nhiều làn.'),
    'Q07': ('Điều 16 khoản 2', 'Đáp án liệt kê đúng các địa điểm cấm lùi, gồm đường một chiều, nơi cấm dừng, chỗ người đi bộ, giao nhau, giao cùng mức đường sắt, tầm nhìn khuất, hầm và cao tốc.'),
    'Q08': ('Điều 17 khoản 2 điểm b', 'Câu về xe xuống dốc nhường xe lên dốc đúng nguyên văn, đặt trong ngữ cảnh tránh xe đi ngược chiều.'),
    'Q09': ('Điều 20 khoản 1', 'Đáp án giữ đủ mốc 18 giờ–06 giờ và điều kiện sương mù/khói/bụi/mưa/thời tiết xấu làm hạn chế tầm nhìn.'),
    'Q10': ('Điều 21 khoản 2', 'Đúng khung giờ 22 giờ–05 giờ, khu đông dân cư/khu vực cơ sở khám chữa bệnh và ngoại lệ xe ưu tiên.'),
    'Q11': ('Điều 22 khoản 3', 'Có báo hiệu vòng xuyến thì nhường xe từ trái, không nhầm với quy tắc không có báo hiệu vòng xuyến ở khoản 2.'),
    'Q12': ('Điều 30 khoản 1 điểm a', 'Đáp án đi sát mép đường bên phải đúng ngoại lệ khi không có vỉa hè/lề đường/đường riêng cho người đi bộ.'),
    'Q13': ('Điều 31 khoản 1', 'Đủ quy tắc chở một người và ngoại lệ chở thêm một trẻ dưới 07 tuổi, tối đa hai người. Áp dụng xe đạp/xe đạp máy, không suy rộng sang xe mô tô.'),
    'Q14': ('Điều 58 khoản 2', 'Điều kiện giấy phép chưa bị trừ hết điểm có ngay trong câu hỏi; đáp án giữ đủ 12 tháng không bị trừ tiếp, tính từ lần bị trừ gần nhất.'),
    'Q15': ('Điều 59 khoản 1 điểm a', 'Đúng đủ 16 tuổi trở lên cho xe gắn máy; không nhầm với điều kiện cấp giấy phép các hạng khác.'),
    'Q16': ('Điều 25 khoản 2', 'Đúng trường hợp xe không vào được làn khẩn cấp: bật đèn khẩn cấp, đặt biển HOẶC đèn cảnh báo sau xe tối thiểu 150 mét, nhanh chóng báo CSGT trên tuyến HOẶC cơ quan quản lý cao tốc.'),
    'Q17': ('Điều 26 khoản 1', 'Đủ đèn chiếu gần cho xe cơ giới/xe máy chuyên dùng và đèn hoặc vật phát sáng báo hiệu cho xe thô sơ trong hầm.'),
    'Q18': ('Điều 64 khoản 1', 'Tiêu đề Điều 64 xác định phạm vi kinh doanh vận tải/vận tải nội bộ; đáp án giữ đủ 10 giờ/ngày, 48 giờ/tuần, 04 giờ liên tục và quy định liên quan của Bộ luật Lao động.'),
    'Q19': ('Điều 80 khoản 1 điểm b', 'Đủ mốc Công an đến, ba ngoại lệ cấp cứu/đưa người bị nạn cấp cứu/bị đe dọa tính mạng sức khỏe và nghĩa vụ trình báo ngay Công an HOẶC UBND gần nhất.'),
    'Q20': ('Điều 89 khoản 1', 'Đúng trường hợp giấy phép cấp trước ngày luật có hiệu lực, tiếp tục dùng theo thời hạn trên giấy phép; không nhầm với trừ điểm, giấy phép quốc tế hay thủ tục cấp đổi.'),
}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def read_csv(name):
    with (OUT / name).open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def blockquote(text):
    return '\n'.join('> ' + line for line in text.splitlines()) + '\n'


def main():
    plan = check_frozen()
    from starter.scripts.summarize_manual import summarize as summarize_manual
    human_done = summarize_manual(OUT)['status'] == 'human_verified'
    receipt = None
    if human_done:
        from starter.scripts.record_confirmed_review import verified_receipt
        receipt = verified_receipt()
    human_status = 'human_verified' if human_done else 'pending_human'
    checked_box = '[x]' if human_done else '[ ]'
    manifest = read(ROOT / 'data/manifest.json')
    entries = {d['source_id']: d for d in manifest['documents']}
    questions = read(ROOT / 'benchmark/questions.json')
    raw_pages, chapter_ranges = {}, {}
    chapter = 'I'
    for entry in manifest['documents']:
        path = ROOT / entry['local_path']
        if sha256(path) != entry['sha256']:
            raise ValueError('PDF checksum changed')
        with pymupdf.open(path) as doc:
            for number in entry['included_pages']:
                text = normalize_text(doc[number-1].get_text())
                if not text:
                    raise ValueError('Content page has no text')
                key = (entry['source_id'], number)
                raw_pages[key] = text
                boundaries = list(re.finditer(r'(?m)^Chương ([IVX]+)\b', text))
                points = [(0, chapter)]
                for match in boundaries:
                    points.append((match.start(), match.group(1)))
                    chapter = match.group(1)
                # Duplicate start=0: the actual heading supersedes inheritance.
                starts = dict(points)
                ordered = sorted(starts)
                chapter_ranges[key] = [(start, ordered[i+1] if i+1 < len(ordered) else len(text), starts[start])
                                       for i, start in enumerate(ordered)]

    def source_link(document_id, page):
        path = entries[document_id]['local_path']
        return f'../../{path}#page={page}'

    def validate_chunk(chunk, metadata=None):
        m = metadata if metadata is not None else dict(chunk['metadata']) | {
            'document_id': chunk['document_id'], 'source': chunk['source'], 'page': chunk['page']}
        key = m['document_id'], m['page']
        text = raw_pages[key]
        assert m['source'] == entries[m['document_id']]['source_url']
        assert text[m['char_start']:m['char_end']] == chunk['text']
        assert any(a <= m['char_start'] < m['char_end'] <= b and section == m['section']
                   for a,b,section in chapter_ranges[key])
        assert m['printed_page'] == entries[m['document_id']]['printed_page_start'] + m['page']-1
        assert m['language'] == 'vi' and m['law_id'] == '36/2024/QH15' and m['version'] == 'original-2024'

    evidence_rows = []
    evidence_md = ['# Đối chiếu 20 câu hỏi với PDF gốc', '',
        'Người kiểm tra: **Codex AI**. Đây là kiểm chứng AI có đọc ngữ cảnh và kiểm tra vị trí bằng code; **chưa phải học viên tự xác nhận**.', '',
        'Chỉ kiểm tra bản luật gốc trong corpus, không xác nhận pháp luật hiện hành. Bộ câu hỏi, evidence, split và metrics đã khóa được giữ nguyên.', '',
        'Kết quả: **20/20 evidence có thật đúng trang; 20/20 đáp án được nguồn hỗ trợ theo nhận xét AI; 15 dev / 5 test; 7 câu filter khớp chương**.', '',
        'Cách dùng: đọc câu hỏi, đáp án, evidence và ghi chú; mở liên kết PDF để đối chiếu. Đánh dấu ô sau mỗi câu chỉ khi chính bạn đã đọc và đồng ý; nếu khác, ghi ID và lý do để sửa bản review, không tự thay benchmark sau khi đã xem test.', '']
    for q in questions:
        key = q['gold_source_id'], q['gold_page']
        text = raw_pages[key]
        quote = comparable(q['evidence_quote'])
        flat = comparable(text)
        assert quote in flat, q['id']
        begin = flat.index(quote)
        end = begin + len(quote)
        # Verify chapter using offsets in raw-normalized physical page text.
        if q.get('filter'):
            assert q['filter'].keys() == {'section'}
            assert any(q['filter']['section'] == section and
                       quote in comparable(text[a:b]) for a,b,section in chapter_ranges[key])
        citation, rationale = SUPPORT[q['id']]
        row = {'question_id':q['id'], 'split':q['split'], 'source_id':key[0], 'page':key[1],
               'citation':citation, 'evidence_exact_match':True, 'answer_supported_ai':True,
               'reason':rationale, 'reviewer':'Codex AI', 'human_status':human_status}
        if human_done:
            row.update(human_reviewer=receipt['reviewer'], answer_supported_human=True,
                       confirmation_record='results/audit/human_confirmation.json')
        evidence_rows.append(row)
        evidence_md += [f"## {q['id']} — {citation} ({q['split']})", '',
            f"**Nguồn:** [{key[0]}, trang PDF {key[1]}]({source_link(*key)}).", '',
            f"**Câu hỏi:** {q['question']}", '', f"**Đáp án:** {q['expected_answer']}", '',
            '**Evidence nguyên văn:**', '', blockquote(q['evidence_quote']),
            '**Ngữ cảnh quanh evidence:**', '', blockquote(flat[max(0,begin-400):end+200]),
            '**Nhận xét AI:** '+rationale, '',
            f'- {checked_box} Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.', '']
    write_json(OUT / 'evidence_review.json', {
        'reviewed_at_utc': datetime.now(timezone.utc).isoformat(), 'reviewer':'Codex AI',
        'method':'Fresh PyMuPDF extraction from SHA-256 verified PDFs; NFC/whitespace exact check plus explicit AI reading of question, answer, quote and surrounding legal context.',
        'after_original_test':True, 'frozen_inputs_changed':False, 'rows':evidence_rows,
        'human_status':human_status,
        'human_reviewer':receipt['reviewer'] if human_done else None,
        'confirmation_record':'results/audit/human_confirmation.json' if human_done else None,
        'review_mode':receipt['review_mode'] if human_done else None})
    if human_done:
        evidence_md[2]=(f"**Đã ghi nhận học viên {receipt['reviewer']} xác nhận:** “{receipt['student_statement']}”. "
                        'Bản kiểm tra do AI hỗ trợ đã được học viên chấp nhận sau đối chiếu nguồn; không phải đánh giá mù. '
                        'Xem [bản ghi xác nhận](human_confirmation.json) và [manual_evidence.csv](manual_evidence.csv).')
    (OUT / 'EVIDENCE_REVIEW.md').write_text('\n'.join(evidence_md)+'\n', encoding='utf-8')

    ai_coherence = {(r['strategy'],r['sample_id']):r for r in read_csv('ai_coherence.csv')}
    samples = read(ROOT / 'results/run/coherence_samples.json')
    positions = {p['sample_id']:p for p in plan['coherence_positions']}
    audit_md = ['# Đối chiếu audit: coherence, grounding và metadata', '',
        '**Đây là gói hỗ trợ học viên review, không phải giấy xác nhận đã chấm thủ công.** Nhãn và lý do hiện do Codex AI đề xuất sau khi đã xem trace/điểm, có nguy cơ thiên lệch. Bạn được sửa nhãn kèm lý do.', '',
        'Coherence: 0 = không hiểu được vì mất ý/chủ thể; 1 = hiểu một phần, thiếu ngữ cảnh; 2 = trọn ý và tự hiểu. Grounding: 0 = không có bằng chứng; 1 = thiếu điều kiện/ngữ cảnh; 2 = đủ trả lời và truy nguồn.', '',
        'A/P04 được rà soát từ 0 lên 1 vì vẫn hiểu được một phần; coherence AI của A hiện là 0,90/2. Xem [lịch sử sửa nhãn AI](review_corrections.json). Không sửa metrics retrieval hoặc lựa chọn A trên dev.', '',
        '## 1. Coherence — 30 bản ghi, cùng 10 vị trí nguồn', '',
        'B/C dùng chính cùng chunk; nội dung chỉ in một lần ở B để tránh đọc lặp. C vẫn có 10 nhãn riêng trong phiếu chấm.', '']
    for s in samples:
        validate_chunk(s['chunk'])
        p = positions[s['sample_id']]
        assert (p['document_id'],p['page'],p['char_offset']) == (s['document_id'],s['page'],s['char_offset'])
        assert s['chunk']['metadata']['char_start'] <= p['char_offset'] < s['chunk']['metadata']['char_end']
        a = ai_coherence[s['strategy'],s['sample_id']]
        audit_md += [f"### {s['strategy']}/{s['sample_id']} — đề xuất {a['score']}/2", '',
            f"Nguồn: [{s['document_id']}, PDF trang {s['page']}]({source_link(s['document_id'],s['page'])}); vị trí mẫu {s['char_offset']}; chunk `{s['chunk']['chunk_id']}`.", '']
        if s['strategy'] == 'C':
            b = next(x for x in samples if x['strategy']=='B' and x['sample_id']==s['sample_id'])
            assert b['chunk'] == s['chunk']
            audit_md += [f"Text giống hoàn toàn mẫu B/{s['sample_id']} ở trên.", '']
        else:
            audit_md += ['**Toàn bộ chunk:**', '', blockquote(s['chunk']['text'])]
            page_text = raw_pages[s['document_id'],s['page']]
            offset = s['char_offset']
            audit_md += ['**Ngữ cảnh nguồn quanh vị trí mẫu:**', '',
                         blockquote(page_text[max(0,offset-350):offset+500])]
        audit_md += ['**Lý do AI:** '+a['reason'], '',
                     f"- {checked_box} Đã tự đọc mẫu {s['strategy']}/{s['sample_id']}; đồng ý hoặc đã ghi nhãn/lý do khác.", '']

    traces = [json.loads(line) for line in (ROOT / 'results/run/traces_test.jsonl').read_text(encoding='utf-8').splitlines()]
    ai_grounding = {(r['strategy'],r['question_id']):r for r in read_csv('ai_grounding.csv')}
    question_map = {q['id']:q for q in questions}
    metadata_rows = []
    audit_md += ['## 2. Grounding — 15 câu/cấu hình với đủ top-3', '']
    for t in traces:
        a = ai_grounding[t['strategy'],t['question_id']]
        q = question_map[t['question_id']]
        audit_md += [f"### {t['strategy']}/{t['question_id']} — đề xuất {a['score']}/2", '',
            '**Câu hỏi:** '+q['question'], '', '**Đáp án cần bằng chứng:** '+q['expected_answer'], '',
            f"**Gold:** [{q['gold_source_id']}, PDF trang {q['gold_page']}]({source_link(q['gold_source_id'],q['gold_page'])}).", '',
            '**Evidence cần đủ:**', '', blockquote(q['evidence_quote'])]
        for rank,h in enumerate(t['hits'],1):
            m = h['metadata']
            validate_chunk(h, m)
            metadata_rows.append({'strategy':t['strategy'],'question_id':t['question_id'],'rank':rank,
                'chunk_id':h['chunk_id'],'source_id':m['document_id'],'page':m['page'],'section':m['section'],
                'url_correct':True,'physical_page_correct':True,'offsets_exact':True,'section_correct':True,
                'complete_and_correct_auto':True,'human_status':human_status})
            if human_done:
                metadata_rows[-1]['human_reviewer']=receipt['reviewer']
            audit_md += [f"**Rank {rank}:** [{m['document_id']}, trang {m['page']}, Chương {m['section']}]({source_link(m['document_id'],m['page'])}); chunk `{h['chunk_id']}`.", '', blockquote(h['text'])]
        audit_md += ['**Lý do AI:** '+a['reason'], '',
                     f"- {checked_box} Đã tự đọc top-3 của {t['strategy']}/{t['question_id']}; đồng ý hoặc đã ghi nhãn/lý do khác.", '']

    audit_md += ['## 3. Metadata — 45 bản ghi', '',
        'Code đã đối chiếu URL, trang vật lý, text theo offsets, chương, số trang in và nhãn snapshot với PDF/manifest: **45/45 khớp**. Học viên cần mở nguồn và xác nhận từng bản ghi; cột khớp tự động không đồng nghĩa đã human_verified.', '',
        '| Strategy/câu/rank | PDF nguồn | Chương | URL/trang/text/chương khớp tự động | Học viên đã kiểm tra |',
        '|---|---|---|---|---|']
    for r in metadata_rows:
        audit_md.append(f"| {r['strategy']}/{r['question_id']}/{r['rank']} | [{r['source_id']}, trang {r['page']}]({source_link(r['source_id'],r['page'])}) | {r['section']} | Có | {'Đã xác nhận' if human_done else 'Chưa xác nhận'} |")
    audit_md += ['', 'Text của từng hit nằm trong phần grounding ở trên, đối chiếu theo strategy/câu/rank. Các trường đầy đủ trong [metadata_samples.json](../run/metadata_samples.json).', '',
        '## 4. Ghi nhận kết quả tự chấm', '',
        'Điền nhãn, lý do, tên người chấm thật và `status=human_verified` trong [manual_coherence.csv](manual_coherence.csv), [manual_grounding.csv](manual_grounding.csv), [manual_metadata.csv](manual_metadata.csv). Giữ ID và nguồn của mẫu. Không tự thay reviewer của nhãn AI để coi là nhãn học viên.', '',
        'Nếu đã tự đọc và đồng ý tất cả đề xuất, có thể phản hồi rõ phạm vi đã đối chiếu để Codex hỗ trợ nhập lại đúng những nhãn bạn xác nhận. Nếu khác, ghi ID và điểm/lý do mới. Việc xem đề xuất AI trước chấm cần được công bố như một nguồn thiên lệch.', '',
        'Chạy `starter/scripts/summarize_manual.py` để tổng hợp sau khi điền; hiện vẫn giữ pending_human.']
    if human_done:
        audit_md[2]=(f"**Đã ghi nhận học viên {receipt['reviewer']} xác nhận đủ 90 mẫu:** “{receipt['student_statement']}”. "
                     'Nhãn ban đầu do Codex AI đề xuất, học viên chấp nhận sau đối chiếu nguồn. Đã xem gợi ý và kết quả nên có nguy cơ thiên lệch; không phải đánh giá mù. '
                     'Xem [bản ghi xác nhận](human_confirmation.json), [tổng hợp](manual_summary.json) và ba phiếu manual đã điền.')
        audit_md=[line.replace('Học viên cần mở nguồn và xác nhận từng bản ghi; cột khớp tự động không đồng nghĩa đã human_verified.',
                               'Học viên đã xác nhận đối chiếu đủ 45 bản ghi với nguồn; cột tự động và xác nhận của học viên được ghi riêng.').replace(
                               'Chạy `starter/scripts/summarize_manual.py` để tổng hợp sau khi điền; hiện vẫn giữ pending_human.',
                               'Đã tổng hợp đủ 90/90 dòng `human_verified`; xem `manual_summary.json`. Nhãn AI gốc được giữ riêng; thay đổi sau này cần được review và ghi nhận rõ.')
                  for line in audit_md]
    (OUT / 'AUDIT_REVIEW.md').write_text('\n'.join(audit_md)+'\n', encoding='utf-8')
    write_json(OUT / 'review_checks.json', {
        'reviewer':'Codex AI + deterministic source consistency checks',
        'pdf_content_pages_reextracted':len(raw_pages), 'questions_reviewed':len(evidence_rows),
        'evidence_exact_matches':sum(r['evidence_exact_match'] for r in evidence_rows),
        'answers_supported_ai':sum(r['answer_supported_ai'] for r in evidence_rows),
        'coherence_samples_read_ai':len(samples),'grounding_cases_read_ai':len(traces),
        'metadata_records_checked':len(metadata_rows),
        'metadata_correct_auto':sum(r['complete_and_correct_auto'] for r in metadata_rows),
        'frozen_inputs_unchanged':True,'retrieval_not_rerun':True,
        'human_confirmation_recorded':human_done,'human_status':human_status,
        'human_reviewer':receipt['reviewer'] if human_done else None,
        'confirmation_record':'results/audit/human_confirmation.json' if human_done else None,
        'metadata_details':metadata_rows})
    check_frozen()
    print('Fresh PDF review: 81 content pages; 20/20 evidence/answer checks; 30 coherence samples; 15 grounding cases; 45/45 metadata consistency checks. Human status:',human_status)


if __name__ == '__main__':
    main()
