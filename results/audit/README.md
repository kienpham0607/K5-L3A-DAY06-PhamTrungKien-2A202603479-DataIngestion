# Phiếu audit — đã ghi nhận học viên xác nhận, có AI hỗ trợ

**Phạm Trung Kiên đã xác nhận trong hội thoại:** “Đã đối chiếu 20 câu và đủ 90 mẫu; đồng ý các đề xuất”. Codex đã nhập các nhãn được chấp nhận vào `manual_*.csv`, ghi tên học viên, lý do và `status=human_verified`, giữ nguyên bản nháp AI ở `ai_*.csv`. Xem [bản ghi xác nhận và hash nguồn/nhãn](human_confirmation.json), [20 câu evidence đã xác nhận](manual_evidence.csv) và [tổng hợp audit](manual_summary.json).

Đây là xác nhận tự khai của học viên sau đối chiếu nguồn với hỗ trợ AI, không phải đánh giá mù, chữ ký số hoặc chứng thực độc lập. Nhãn AI được xem trước nên có nguy cơ thiên lệch xác nhận. Trạng thái hiện tại: **20/20 câu evidence, 90/90 mẫu audit đã xác nhận; 0 dòng chờ**.

Đã chuẩn bị hai bản đối chiếu để đọc trực tiếp thay vì tự ghép nhiều file JSON/CSV:

- [EVIDENCE_REVIEW.md](EVIDENCE_REVIEW.md): đủ 20 câu, đáp án, evidence, ngữ cảnh, điều/khoản và link mở đúng trang PDF. Kết quả AI: 20/20 đúng nguồn và đáp án được hỗ trợ. Mỗi câu có ô trống để bạn tự đánh dấu sau khi đọc.
- [AUDIT_REVIEW.md](AUDIT_REVIEW.md): đủ 30 mẫu coherence, 15 bộ top-3 grounding và bảng 45 metadata; có nhãn AI đề xuất và lý do, để bạn đồng ý hoặc sửa dựa trên nguồn.

Rà soát AI sửa A/P04 từ 0 lên 1 vì còn hiểu được một phần, nên coherence A hiện **0,90/2**, đã được học viên chấp nhận cùng các nhãn khác; xem [review_corrections.json](review_corrections.json) để biết trạng thái lịch sử trước khi xác nhận. Script `prepare_review.py` dựng lại bản đối chiếu từ nguồn, giữ trạng thái theo các phiếu đã điền và bản ghi xác nhận.

| File đã ghi nhận | Số dòng | Nội dung |
|---|---:|---|
| `manual_coherence.csv` | 30 | 10 vị trí nguồn × A/B/C, score 0/1/2 |
| `manual_grounding.csv` | 15 | 5 câu test × A/B/C, score 0/1/2 |
| `manual_metadata.csv` | 45 | 5 câu test × 3 rank × A/B/C, complete_and_correct True/False |

CSV dùng UTF-8 BOM để mở tiếng Việt bằng Excel. **Giữ nguyên ID, strategy, rank, chunk_id và vị trí nguồn.** Chỉ điền/sửa nhãn, `reason`, `reviewer` (tên người thật đã đọc), `status=human_verified`. Nhãn nháp và nhãn người học nằm ở file riêng để tránh vô tình ghi nhận AI là human.

1. Mở [coherence_samples.json](../run/coherence_samples.json): mỗi mẫu có text chunk, source/page/offset. Đối chiếu [pages.jsonl](../../data/processed/pages.jsonl) và [PDF phần 1](../../data/raw/36-2024-qh15-part1.pdf). Vị trí là giữa 10 trang đầu, đã khóa trước retrieval. B/C cùng chunk nên có thể ghi rõ dùng chung đánh giá.
2. Chấm coherence: **0** cắt ý/mất chủ thể không hiểu được; **1** hiểu một phần, thiếu ngữ cảnh; **2** tự hiểu và trọn ý. Đánh giá nội dung, không chỉ nhìn độ dài hay dấu chấm. Ghi lý do từng mẫu.
3. Mở [grounding_samples.json](../run/grounding_samples.json) và [questions.json](../../benchmark/questions.json): đọc cùng top-3, kiểm tra đủ điều kiện/ngoại lệ để trả lời. **0** không có bằng chứng; **1** có nhưng thiếu điều kiện/ngữ cảnh; **2** đủ để trả lời và truy nguồn. Không chuyển Hit@3 tự động thành nhãn grounding.
4. Mở [metadata_samples.json](../run/metadata_samples.json), kiểm tra từng hit theo PDF phần 1/2: URL, **trang vật lý 1-based**, chương và offset có đúng không. `page` không phải số trang in Công báo. Ghi True chỉ khi metadata đủ và đúng; nếu False nêu trường lỗi và đối chiếu nguồn.
5. Có thể xem `ai_coherence.csv`, `ai_grounding.csv`, `ai_metadata.csv` sau khi tự chấm để so sánh. Nếu đã xem trước, ghi nguy cơ bị ảnh hưởng bởi AI. Không bắt buộc đồng ý nhãn nháp.
6. Từ root repo, chạy:

```powershell
.venv/Scripts/python.exe starter/scripts/summarize_manual.py
.venv/Scripts/python.exe starter/scripts/verify_submission.py
```

Khi còn dòng thiếu, `manual_summary.json` giữ `pending_human` và không công bố manual metrics. Khi cả 90 dòng có nhãn, lý do và người chấm, script xuất bảng metrics; học viên phải chép bảng đó vào báo cáo, ghi người chấm, cách kiểm tra và thiên lệch. Bộ kiểm tra xác nhận định dạng và tính nhất quán, không thể xác minh danh tính hoặc việc đọc thủ công.

`write_report.py` đọc trạng thái và metrics từ `manual_summary.json` khi human audit đã được xác nhận, giữ công bố nguồn gốc AI. Tuy nhiên script vẫn dựng lại báo cáo cá nhân, nên cần giữ bản sao nếu bạn đã tự sửa thêm nội dung. `write_review_draft.py` không ghi đè file `manual_*.csv` đã tồn tại. Nếu thay nhãn AI hoặc corpus đã được xác nhận, kiểm tra hash sẽ báo cần review mới thay vì tự nhận lại xác nhận cũ.
