"""Render student-accepted audit results without hiding their AI-assisted origin."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]


def confirmed_summary():
    path=ROOT/'results/audit/manual_summary.json'
    if not path.exists():
        return None
    summary=json.loads(path.read_text(encoding='utf-8'))
    return summary if summary['status']=='human_verified' else None


def manual_table():
    summary=confirmed_summary()
    if summary is None:
        raise ValueError('No completed student audit')
    traces=[json.loads(line) for line in (ROOT/'results/run/traces_test.jsonl').read_text(encoding='utf-8').splitlines()]
    table=['| Strategy | Coherence trung bình /2 (n) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N hoặc N/A) | Grounding 0/1/2 (số câu) và trung bình /2 |',
           '|---|---|---|---|---|']
    for row in summary['manual_metrics']:
        strategy=row['strategy']
        filtered=[t for t in traces if t['strategy']==strategy and t['requested_filter']]
        compliant=sum(len(t['hits'])==3 and all(all(h['metadata'].get(k)==v for k,v in t['requested_filter'].items())
                      for h in t['hits']) for t in filtered)
        filter_text=f'{compliant}/{len(filtered)}' if filtered else 'N/A'
        cs=f"{row['coherence_mean']:.2f}".replace('.',',')
        gs=f"{row['grounding_mean']:.2f}".replace('.',',')
        d=row['grounding_distribution']
        table.append(f"| {strategy} | {cs} (10) | {row['metadata_correct']}/{row['metadata_n']} | {filter_text} | {d.get('0',0)}/{d.get('1',0)}/{d.get('2',0)} câu; {gs}/2 |")
    return '\n'.join(table)+'\n'


def apply_confirmed_review(text, prefix=''):
    summary=confirmed_summary()
    if summary is None:
        return text
    receipt=json.loads((ROOT/'results/audit/human_confirmation.json').read_text(encoding='utf-8'))
    evidence_link=prefix+'results/audit/human_confirmation.json'
    summary_link=prefix+'results/audit/manual_summary.json'
    statement=(f"**Học viên đã xác nhận:** {receipt['reviewer']} đã phản hồi “{receipt['student_statement']}”. "
               'Đã ghi nhận 20/20 câu evidence và đủ 90/90 mẫu audit: 30 coherence, 15 grounding, 45 metadata. '
               f"Xem [bản ghi xác nhận]({evidence_link}) và [tổng hợp nhãn học viên]({summary_link}). "
               'Nhãn ban đầu do AI đề xuất; học viên cho biết đã đối chiếu nguồn và đồng ý. Đây là review có AI hỗ trợ, sau khi đã xem kết quả, '
               'không phải đánh giá mù hoặc đánh giá độc lập của người chấm thứ hai.')
    old_root='**Bảng đánh giá định tính dưới đây là bản nháp AI, chưa phải kết quả học viên chấm thủ công.** Coherence/grounding do Codex AI đọc và đề xuất; metadata được kiểm tra nhất quán bằng code kèm nhận xét AI. Các phiếu human audit hiện còn trống, trạng thái `pending_human` với 90 bản ghi cần xác nhận.'
    old_personal='**Trạng thái quan trọng:** bảng dưới đây là **nhãn nháp do Codex AI đọc và nhận xét**, metadata còn có kiểm tra nhất quán bằng code. **Chưa có học viên chấm thủ công/xác nhận**; không trình bày chúng như số liệu human audit. Chưa hoàn tất hạng mục audit thủ công của lab. Phiếu trống và hướng dẫn ở [results/audit](../../results/audit/README.md). Trạng thái máy đọc được: [manual_summary.json](../../results/audit/manual_summary.json).'
    text=text.replace(old_root,statement).replace(old_personal,statement)
    text=re.sub(r'(?m)^\| Strategy \| Coherence[^\n]*\n\|[-| :]+\|\n(?:\| [ABC] \|[^\n]*\n){3}',
                lambda _: manual_table(),text)
    pairs=[
        ('Phần đánh giá định tính có nhãn nháp do AI hỗ trợ; trạng thái chấm thủ công của học viên được nêu riêng bên dưới.',
         'Phần đánh giá định tính sử dụng nhãn AI hỗ trợ đã được học viên xác nhận sau khi đối chiếu nguồn; phương pháp và nguy cơ thiên lệch được nêu rõ bên dưới.'),
        ('Codex AI hỗ trợ đọc nguồn và soạn đáp án; kiểm tra chuỗi không thay cho việc học viên tự xác minh ý nghĩa và độ đủ của bằng chứng.',
         'Codex AI hỗ trợ đọc nguồn và soạn đáp án; sau đó học viên xác nhận đã tự đối chiếu đủ 20 câu và đồng ý các đáp án/evidence.'),
        ('học viên vẫn cần kiểm chứng độc lập.', 'học viên đã xác nhận đối chiếu đủ 20 câu với nguồn, có tham khảo nhận xét AI.'),
        ('**nháp AI**, không phải human audit', '**bản đề xuất AI được học viên chấp nhận sau đối chiếu**, có ghi nguồn nhãn'),
        ('theo nháp AI,', 'theo nhãn có AI hỗ trợ đã được học viên xác nhận,'),
        ('trong nháp audit', 'trong audit có AI hỗ trợ đã được học viên xác nhận'),
        ('Kết luận định tính cần học viên xác nhận bằng phiếu chấm;', 'Học viên đã xác nhận các nhãn định tính trong phiếu chấm;'),
        ('nhưng người học chưa đối chiếu đủ PDF.', 'và học viên đã xác nhận đối chiếu đủ 45 bản ghi với nguồn.'),
        ('Chưa ghi nhận học viên đã chấm thủ công.', 'Học viên đã xác nhận đủ 90 mẫu trong bản ghi xác nhận, với nguồn nhãn AI được công bố.'),
        ('và chưa ghi nhận human audit.', 'và đã ghi nhận học viên xác nhận đủ 90 mẫu, có AI hỗ trợ.'),
        ('Chưa có người chấm thủ công được xác nhận; nhãn AI không thay cho yêu cầu này.',
         'Người xác nhận sau đối chiếu nguồn: Phạm Trung Kiên; đủ 90/90 mẫu, nhãn có nguồn gốc AI được lưu riêng.'),
        ('Các nhãn được giải thích từng câu, không suy ra máy móc từ Hit@3 và chưa được coi là human audit.',
         'Các nhãn được giải thích từng câu, không suy ra máy móc từ Hit@3; học viên đã đối chiếu và chấp nhận đề xuất AI.'),
        ('20 câu do AI hỗ trợ soạn, chưa có người kiểm chứng độc lập;',
         '20 câu do AI hỗ trợ soạn đã được học viên xác nhận sau đối chiếu; chưa có người chấm độc lập thứ hai;'),
        ('AI hỗ trợ soạn benchmark và chấm nháp sau khi đã xem trace/điểm, có nguy cơ thiên lệch; chưa có người học kiểm chứng độc lập. Human audit cần được hoàn thành trước khi coi các điểm coherence, metadata và grounding là nhãn chấm thủ công của bài nộp.',
         'AI hỗ trợ soạn benchmark và đề xuất nhãn sau khi đã xem trace/điểm; học viên xác nhận đã đối chiếu đủ 20 câu và 90 mẫu, đồng ý các đề xuất. Vì đã xem gợi ý AI, nhãn có nguy cơ thiên lệch xác nhận và không phải đánh giá mù; chưa có người chấm độc lập thứ hai.'),
        ('thang điểm định tính có thiên lệch;', 'thang điểm định tính có thiên lệch vì học viên tham khảo gợi ý AI;'),
        ('**Lớp:** L3A (theo tên repo, cần học viên xác nhận).', '**Lớp:** L3A.'),
        ('grounding AI=1;', 'grounding có AI hỗ trợ được học viên chấp nhận = 1;'),
        ('nên nháp grounding chỉ đạt mức 1.', 'nên grounding được học viên chấp nhận ở mức 1.'),
    ]
    for old,new in pairs:
        text=text.replace(old,new)
    old_end='Học viên cần đọc 3 phiếu `manual_*.csv` (30 coherence, 15 grounding, 45 metadata), sửa/điền nhãn và lý do sau đối chiếu nguồn, ghi người chấm thật và `human_verified`; chạy `summarize_manual.py`, cập nhật bảng human audit và giới hạn thiên lệch. Sau đó xác nhận thông tin cá nhân, tạo commit chốt, kiểm tra quyền truy cập repo và nộp link theo kênh lớp. **Không đánh dấu bài đã nộp hoặc audit đã hoàn thành khi chưa có bằng chứng.**'
    text=text.replace(old_end,'Học viên Phạm Trung Kiên xác nhận đã đối chiếu đủ 20 câu và 90 mẫu, đồng ý các đề xuất. Codex hỗ trợ nhập nhãn theo phản hồi này vào `manual_*.csv`, giữ bản nháp AI riêng và ghi `human_verified` kèm liên kết bản ghi xác nhận. Chưa có đánh giá mù hoặc người chấm độc lập thứ hai. Các bước còn lại là chốt commit, đẩy đầy đủ bài làm lên repo và nộp link theo kênh lớp; chưa ghi nhận đã nộp bài.')
    old_root_end='Học viên cần tự đối chiếu evidence, hoàn thành các phiếu human audit, ghi người chấm và lý do, cập nhật bảng nhãn thủ công rồi chốt commit/nộp link theo hướng dẫn lớp.'
    text=text.replace(old_root_end,'Học viên Phạm Trung Kiên đã xác nhận đối chiếu đủ 20 câu và 90 mẫu, đồng ý nhãn AI đề xuất. Codex nhập nhãn và lý do theo phản hồi, giữ nguyên nguồn gốc AI và bản ghi xác nhận; các bước còn lại là chốt commit, push bài làm và nộp link theo hướng dẫn lớp.')
    return text
