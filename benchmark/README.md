# Benchmark giao thông: 15 dev / 5 test

[questions.json](questions.json) được soạn từ snapshot Luật 36/2024/QH15 trước khi chạy retrieval. Q01–Q15 là dev; Q16–Q20 là test. **Không dùng điểm test để chọn lại cấu hình.** Lựa chọn A và thời điểm chốt nằm ở [selection.json](../results/run/selection.json).

Mỗi câu có `id`, `split`, `type`, `question`, `expected_answer`, `gold_source_id`, `gold_page`, `evidence_quote`, `filter`. Trang là trang PDF vật lý 1-based theo từng file, không phải trang Công báo. `alternative_gold` là danh sách bằng chứng khác được hỗ trợ bởi evaluator nếu xác minh được; bộ hiện tại chỉ khai báo gold chính.

7 câu kiểm tra filter: Q01/I, Q13/II, Q14/IV, Q15/IV trên dev và Q18/IV, Q19/VII, Q20/IX trên test. Phạm vi chương xuất hiện trong lời hỏi; đây là input có trước retrieval. A/B giữ nguyên câu hỏi nhưng không filter; C áp dụng đúng `section`. Không đưa `expected_answer`, `gold_source_id`, `gold_page` hoặc `evidence_quote` vào embedding query hay filter. Câu không filter của C dùng đúng index B.

Lệnh `prepare` kiểm tra 20 evidence có thật trong nguồn sau chuẩn hóa và giá trị filter đúng chapter segment. Kiểm tra chuỗi không chứng minh đáp án đủ/đúng; Codex AI đã đọc để soạn nháp. Học viên Phạm Trung Kiên sau đó xác nhận trong hội thoại đã đối chiếu đủ 20 câu và đồng ý các đề xuất; xem [bản ghi xác nhận](../results/audit/human_confirmation.json) và [manual_evidence.csv](../results/audit/manual_evidence.csv). Đây là review có tham khảo AI, chưa có người chấm độc lập thứ hai.

[frozen_plan.json](frozen_plan.json) ghi hash corpus/config/câu hỏi, quy tắc chọn theo dev và 10 vị trí audit trước retrieval. Đây là nhật ký có hash, không phải timestamp được bên thứ ba chứng thực. Hệ thống từ chối chỉnh các đầu vào đã khóa. Muốn đổi bộ câu hỏi/model/chunking sau khi xem test phải mở thí nghiệm có phiên bản riêng và tập test mới nếu cần đánh giá độc lập.

Hạn chế: cùng một luật có chủ đề gần nhau ở dev/test; Q16 và Q17 cùng trang. Đây là holdout câu hỏi, không phải chia độc lập theo tài liệu. Người xây benchmark biết gold khi viết test; điểm retrieval test được chạy sau chốt dev. Tái chạy cùng test chỉ là tái lập, không tạo một holdout mới.
