# Kết quả chạy thật

| Strategy | Split | Hit@1 | Evidence Hit@3 | Chunks | Ingest (s) | API USD |
|---|---|---|---|---|---|---|
| A | dev | 4/15 (26.7%) | 10/15 (66.7%) | 397 | 8.645 | 0 |
| A | test | 3/5 (60.0%) | 4/5 (80.0%) | 397 | 8.645 | 0 |
| B | dev | 8/15 (53.3%) | 9/15 (60.0%) | 310 | 7.452 | 0 |
| B | test | 3/5 (60.0%) | 4/5 (80.0%) | 310 | 7.452 | 0 |
| C | dev | 8/15 (53.3%) | 9/15 (60.0%) | 310 | Dùng chung B | 0 |
| C | test | 3/5 (60.0%) | 5/5 (100.0%) | 310 | Dùng chung B | 0 |

## Audit đã được học viên xác nhận — có AI hỗ trợ

| Strategy | Coherence trung bình /2 (n) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N hoặc N/A) | Grounding 0/1/2 (số câu) và trung bình /2 |
|---|---|---|---|---|
| A | 0,90 (10) | 15/15 | 1/3 | 0/1/4 câu; 1,80/2 |
| B | 1,50 (10) | 15/15 | 1/3 | 1/0/4 câu; 1,60/2 |
| C | 1,50 (10) | 15/15 | 3/3 | 0/0/5 câu; 2,00/2 |

Lựa chọn từ dev: A. Phạm Trung Kiên xác nhận đã đối chiếu 20 câu và đủ 90 mẫu, đồng ý các đề xuất. Nhãn AI ban đầu được giữ riêng; đây không phải đánh giá mù. Xem [bản ghi xác nhận](audit/human_confirmation.json) và [manual_summary.json](audit/manual_summary.json).

Rà soát AI bổ sung: A/P04 đổi 0 → 1 do còn hiểu được một phần; xem [lịch sử sửa nhãn](audit/review_corrections.json). Evidence được đối chiếu trực tiếp PDF ở [EVIDENCE_REVIEW.md](audit/EVIDENCE_REVIEW.md), mẫu audit ở [AUDIT_REVIEW.md](audit/AUDIT_REVIEW.md). Không thay số liệu retrieval.
