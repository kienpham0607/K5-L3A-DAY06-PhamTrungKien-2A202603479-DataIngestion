# Báo cáo cá nhân — Day 6

**Họ và tên:** Phạm Trung Kiên  
**MSSV:** 2A202603479  
**Lớp:** L3A  
**Đề tài:** Xây dựng kho tri thức truy xuất về trật tự, an toàn giao thông đường bộ Việt Nam.  
**Repository:** [K5-L3A-DAY06-PhamTrungKien-2A202603479-DataIngestion](https://github.com/kienpham0607/K5-L3A-DAY06-PhamTrungKien-2A202603479-DataIngestion)

## Dữ liệu và pipeline

**Chủ đề, nguồn/quyền, số trang và quy tắc tính trang**

Corpus gồm hai PDF của **Luật Trật tự, an toàn giao thông đường bộ số 36/2024/QH15, bản gốc năm 2024**, tải từ [Cổng Thông tin điện tử Chính phủ](https://vanban.chinhphu.vn/?classid=1&docid=211194&pageid=27160). Mục tiêu là truy xuất các quy tắc, điều kiện và ngoại lệ trong luật. Corpus là snapshot phục vụ thí nghiệm; không khẳng định đã cập nhật toàn bộ sửa đổi pháp luật tại thời điểm sử dụng.

| Tài liệu | Trang vật lý | Trang tính nội dung | Trang loại |
|---|---:|---|---|
| [PDF phần 1](data/raw/36-2024-qh15-part1.pdf) | 21 | 1–20: 20 trang | Trang 21 chỉ có thông tin xuất bản dạng ảnh, không có nội dung luật |
| [PDF phần 2](data/raw/36-2024-qh15-part2.pdf) | 61 | 1–61: 61 trang | Không |
| **Tổng** | **82** | **81 trang nội dung** | **1 trang** |

Trang được tính theo trang vật lý PDF, bắt đầu từ 1 trong từng file, có nội dung luật trích xuất được. Trang đầu có điều luật nên được tính; không nhân bản nội dung để đạt số trang tối thiểu. Sau chuẩn hóa, corpus có **164.494 ký tự**. Việc tách tại ranh giới chương tạo 89 segment nhưng không làm tăng số trang nội dung.

Quyền xử lý được ghi trong [manifest](data/manifest.json): văn bản quy phạm pháp luật thuộc nhóm không được bảo hộ quyền tác giả theo khoản 2 Điều 15 Luật Sở hữu trí tuệ, dẫn chiếu [văn bản hợp nhất trên Cổng Chính phủ](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/9/155-vbhn-vpqh.pdf). Dự án khai thác phần văn bản luật và ghi nguồn. Manifest lưu URL, ngày truy cập, SHA-256, danh sách trang và số ký tự từng trang.

**Chuẩn hóa, lỗi và giới hạn**

Pipeline Python thực hiện: đọc PDF bằng PyMuPDF → chuẩn hóa Unicode NFC → bỏ header Công báo và số trang → nối các dòng bị xuống hàng do dàn trang, giữ ranh giới điều/khoản/điểm → tách chương → chia chunk → tạo embedding → lưu Chroma → truy xuất top-3 và đánh giá.

Một trang có thể chứa phần cuối chương trước và phần đầu chương sau. Pipeline tách hai phần trước khi chia chunk để metadata `section` không gắn nhầm nội dung. Chương được nhận từ tiêu đề nguồn, kế thừa liên tục giữa các trang và hai PDF.

Trang 21 phần 1 không trích xuất được text; kiểm tra ảnh cho thấy đây là khối thông tin xuất bản, nên loại khỏi corpus và không OCR. Log ở [ingestion_errors.jsonl](results/run/ingestion_errors.jsonl). Các giới hạn còn lại gồm chữ ký số lẫn trong text ở một số trang đầu và điều/khoản tiếp nối qua trang bị chia tách. Các điểm này được ghi nhận khi review sau test, không dùng kết quả test để sửa corpus rồi báo lại như một phép đo độc lập.

**Embedding model/provider/version/số chiều, vector store/version, metric, lệnh chạy và chi phí**

| Thành phần | Cấu hình thực tế |
|---|---|
| Provider | Model local chạy trên CPU qua Sentence Transformers |
| Model | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| Revision | `e8f8c211226b894fcb81acc59f3b34ba3efd5f42` |
| Thư viện embedding | Sentence Transformers 6.3.0; Transformers 5.22.2; Torch 2.15.0 |
| Số chiều | 384 |
| Encode query/document | Cùng model và cách encode; mean pooling theo model, L2 normalize, không thêm prefix |
| Giới hạn đầu vào | 256 token; A tối đa thực tế 160, B/C tối đa 232; không chunk nào bị cắt token |
| Vector store | Chroma 1.5.9, `PersistentClient` |
| Metric/index | Cosine, HNSW approximate; `ef_construction=200`, `ef_search=100`, `num_threads=1` |
| Collection | A: `traffic-fixed`; B/C dùng chung `traffic-paragraph` |
| Lưu bền | `artifacts/chroma/` trên máy chạy; index được dựng lại khi clone repo |
| Môi trường | Python 3.12.10, Windows; seed 42, CPU 4 thread cho model |
| Chi phí API | **0 USD**, chưa đo chi phí điện, phần cứng và lưu lượng tải |

Giới hạn 256 token được khóa trước retrieval, khác mặc định 128 của model card; không có truncation ở giới hạn đã chọn nhưng chất lượng ngữ nghĩa vẫn cần đánh giá bằng benchmark. Cả ba cấu hình dùng embedding thật, cùng model/revision; không dùng vector ngẫu nhiên thay thế khi lỗi.

Lệnh từ root repository để cài và tái lập vào thư mục kết quả/index mới:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r starter/requirements.txt
$env:PYTHONIOENCODING = 'utf-8'
.venv/Scripts/python.exe starter/scripts/prepare_sources.py
.venv/Scripts/python.exe starter/scripts/download_model.py
$env:HF_HUB_OFFLINE = '1'
.venv/Scripts/python.exe -m starter.src.run all --output results/reproduction --store artifacts/reproduction-chroma
```

Sau khi tải đủ model và corpus, pipeline chạy local. Nếu thư mục output đã có kết quả test, cần chọn thư mục output mới để giữ nguyên lần chạy trước. Phiên bản thực tế và cấu hình được lưu tại [environment.json](results/run/environment.json); hướng dẫn đầy đủ ở [README.md](README.md).

**Metadata bắt buộc, trường lọc bổ sung, nguồn giá trị và lý do chọn**

| Trường | Kiểu/nguồn giá trị | Mục đích |
|---|---|---|
| `document_id` | String, ID từng PDF trong manifest | Phân biệt hai file nguồn |
| `source` | String, URL PDF chính thức | Truy về tài liệu gốc |
| `page` | Integer, trang vật lý PDF từ 1 | Mở đúng trang để kiểm tra evidence |
| `section` | String số La Mã I–IX, lấy từ tiêu đề chương | Lọc đúng phạm vi chương được người hỏi cung cấp |
| `printed_page` | Integer, số trang in Công báo theo từng file | Hỗ trợ đối chiếu với bản in, không thay `page` |
| `char_start`, `char_end` | Integer, offsets trên text trang đã chuẩn hóa | Xác minh text chunk khớp vị trí nguồn |
| `law_id`, `version`, `language` | Nhãn luật, snapshot `original-2024`, ngôn ngữ `vi` | Mô tả và phân biệt phiên bản corpus |

Trường lọc thực nghiệm là `section`, có giá trị phân biệt được giữa các chương. Filter được lấy từ phạm vi nêu trong câu hỏi trước truy xuất; không lấy `gold_source_id`, trang gold hoặc đáp án để lọc. Metadata đúng giúp truy vết và giới hạn phạm vi, nhưng không tự bảo đảm chunk chứa đủ bằng chứng.

## Cấu hình và benchmark

**A / B / C và tham số cụ thể**

| Strategy | Chunking | Metadata/truy xuất | Giả thuyết trước thử nghiệm |
|---|---|---|---|
| A | Fixed-size 500 ký tự, overlap 50 | Đủ metadata; cosine top-3 không filter | Cửa sổ ngắn dễ truy xuất ý cụ thể nhưng có thể cắt câu/điều kiện |
| B | Gom đoạn/khoản tối đa 800 ký tự, overlap 0; đoạn dài tách theo câu/từ | Cùng metadata; cosine top-3 không filter | Giữ mạch ý tốt hơn, giảm số chunk nhưng có thể làm loãng ngữ nghĩa |
| C | Dùng chính chunk, vector và collection của B | Chỉ thêm filter `section` khi câu hỏi có phạm vi chương | Loại kết quả sai chương; không sửa được evidence bị cắt |

**B–C chỉ thay một yếu tố là metadata filter.** A–B so sánh một gói thay đổi chunking, gồm cách chia, kích thước và overlap; không diễn giải là phép đo riêng từng tham số. Corpus, model, backend, cosine metric, bộ câu hỏi và top-k đều giữ nguyên.

**Bộ câu hỏi, phân chia dev/test và kiểm chứng evidence**

[questions.json](benchmark/questions.json) có **20 câu**: **Q01–Q15 là dev**, **Q16–Q20 là test**. Mỗi câu có đáp án kỳ vọng, ID tài liệu, trang vật lý và evidence. Các dạng câu gồm hỏi trực tiếp, diễn đạt lại, điều kiện, ngoại lệ và quy định chuyển tiếp.

Có **7 câu metadata filter**: Q01/I, Q13/II, Q14/IV, Q15/IV ở dev; Q18/IV, Q19/VII, Q20/IX ở test. Phạm vi chương xuất hiện ngay trong câu hỏi. Câu không có filter của C chạy cùng index B, không bổ sung điều kiện lọc.

Trước retrieval, code kiểm tra **20/20 evidence có thật** tại nguồn/trang đã khai báo sau chuẩn hóa whitespace; đồng thời đối chiếu filter với chapter segment chứa evidence. Codex AI hỗ trợ đọc nguồn và soạn đáp án; kiểm tra chuỗi không thay cho việc học viên tự xác minh ý nghĩa và độ đủ của bằng chứng.

Split, cấu hình, hash đầu vào và vị trí audit được lưu trước retrieval trong [frozen_plan.json](benchmark/frozen_plan.json). Bộ dev/test vẫn dùng cùng một luật, có nội dung gần nhau và Q16/Q17 cùng trang; đây là holdout câu hỏi nhỏ, không phải holdout tài liệu độc lập. Người soạn biết gold khi xây benchmark; điểm truy xuất test chỉ được chạy sau khi chốt lựa chọn từ dev.

**Tiêu chí chọn chiến lược đã chốt trước khi xem test**

Ưu tiên **Evidence Hit@3 trên dev**, sau đó **Hit@1 trên dev**, tiếp theo **ít chunk hơn**, cuối cùng theo thứ tự A/B/C nếu vẫn hòa. Theo tiêu chí này, **A được chọn** với Hit@3 dev 10/15. Lựa chọn được lưu trước lần truy vấn test đầu tiên tại [selection.json](results/run/selection.json); không chọn lại C dựa trên điểm test.

## Kết quả

Một hit yêu cầu chunk đúng nguồn và trang gold, đồng thời chứa **toàn bộ evidence** đã ghi sau chuẩn hóa NFC/whitespace. Hit@1 xét rank 1; Evidence Hit@3 xét có ít nhất một chunk đạt điều kiện trong top-3. Không tính hit chỉ vì chung trang hoặc ghép nhiều mảnh evidence để thay định nghĩa chính.

| Strategy | Split | Hit@1 (n/N) | Evidence Hit@3 (n/N) | Chunk count | Thời gian | Chi phí |
|---|---|---|---|---:|---|---|
| A | dev | 4/15 — 26,7% | 10/15 — 66,7% | 397 | Ingest 8,645 s | API 0 USD |
| A | test | 3/5 — 60,0% | 4/5 — 80,0% | 397 | Dùng index A đã nạp | API 0 USD |
| B | dev | 8/15 — 53,3% | 9/15 — 60,0% | 310 | Ingest 7,452 s | API 0 USD |
| B | test | 3/5 — 60,0% | 4/5 — 80,0% | 310 | Dùng index B đã nạp | API 0 USD |
| C | dev | 8/15 — 53,3% | 9/15 — 60,0% | 310 | Dùng chung index B | API 0 USD |
| C | test | 3/5 — 60,0% | 5/5 — 100,0% | 310 | Dùng chung index B | API 0 USD |

Thời gian ở bảng là **thời gian ingest**, gồm chunking, đếm token, tạo embedding và upsert lần đầu; không phải tổng thời gian benchmark. Không cộng lại ingest cho từng split. Chưa tính tải PDF/model, thời gian load model chung **14,651 s** hoặc upsert lần hai để kiểm tra trùng. A/B lần gốc không dùng cache embedding; C không có một lần tạo vector/nạp index riêng. Thời gian truy vấn từng câu nằm trong trace nhưng chưa được đo lặp để kết luận hiệu năng.

| Chỉ số tài nguyên | A | B/C |
|---|---:|---:|
| Tổng ký tự trong các chunk | 179.716 | 164.036 |
| Tổng token đầu vào trước truncation | 46.767 | 42.364 |
| Độ dài chunk nhỏ nhất / median / p95 / lớn nhất | 51 / 499 / 500 / 500 | 30 / 598 / 783 / 799 |
| Chunk bị cắt token | 0 | 0 |
| Số chunk sau nạp lần đầu → nạp lại | 397 → 397 | 310 → 310 |

Nguồn số đo: [index_stats.json](results/run/index_stats.json). ID chunk được tạo ổn định từ tài liệu, trang, offset, cách chia và text. Khi đồng bộ toàn corpus, store upsert rồi xóa ID lỗi thời; kiểm thử corpus thay đổi xác nhận chunk cũ được loại bỏ. Các batch không có transaction toàn cục, nên cần nạp lại nếu tiến trình dừng giữa chừng.

**Bảng đánh giá định tính dưới đây là bản nháp AI, chưa phải kết quả học viên chấm thủ công.** Coherence/grounding do Codex AI đọc và đề xuất; metadata được kiểm tra nhất quán bằng code kèm nhận xét AI. Các phiếu human audit hiện còn trống, trạng thái `pending_human` với 90 bản ghi cần xác nhận.

| Strategy | Coherence trung bình /2 (n) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N hoặc N/A) | Grounding 0/1/2 (số câu) và trung bình /2 |
|---|---|---|---|---|
| A | 0,80 (10; nháp AI) | 15/15 (tự động + AI) | 1/3 câu test có filter | 0/1/4 câu; 1,80/2 (nháp AI) |
| B | 1,50 (10; nháp AI) | 15/15 (tự động + AI) | 1/3 câu test có filter | 1/0/4 câu; 1,60/2 (nháp AI) |
| C | 1,50 (10; nháp AI) | 15/15 (tự động + AI) | 3/3 câu test có filter | 0/0/5 câu; 2,00/2 (nháp AI) |

Tỷ lệ filter tính theo câu hỏi: một câu tuân thủ khi cả top-3 đều khớp phạm vi yêu cầu. A/B không áp dụng filter nên sự tuân thủ là tình cờ. Grounding ở đây đo **độ đủ bằng chứng truy xuất**, không phải độ chính xác câu trả lời do LLM sinh.

**Đường dẫn trace, nhãn thủ công và cách chọn mẫu**

- Trace đầy đủ: [dev](results/run/traces_dev.jsonl), [test](results/run/traces_test.jsonl); tổng 60 lượt truy xuất, 180 hits, có ID, text, score và metadata.
- Metrics gốc: [metrics_dev.json](results/run/metrics_dev.json), [metrics_test.json](results/run/metrics_test.json); cấu hình và giả thuyết trong [experiment_log.csv](artifacts/experiment_log.csv).
- Coherence: chọn giữa trang của **10 trang nội dung đầu theo document_id/page**, trước retrieval; lấy chunk có `char_start` nhỏ nhất bao phủ vị trí đó. A/B/C dùng cùng vị trí; [mẫu có text/offset](results/run/coherence_samples.json), [nhãn AI](results/audit/ai_coherence.csv), [phiếu học viên](results/audit/manual_coherence.csv).
- Metadata: kiểm tra **5 câu test × top-3 × 3 cấu hình = 45 bản ghi**, đối chiếu URL, trang, chương và offsets; [mẫu](results/run/metadata_samples.json), [nhãn tự động + AI](results/audit/ai_metadata.csv), [phiếu học viên](results/audit/manual_metadata.csv).
- Grounding: đọc top-3 của cùng **5 câu test cho mỗi cấu hình**, chấm 0/1/2 theo thiếu/đủ evidence và điều kiện; [mẫu](results/run/grounding_samples.json), [nhãn AI và lý do](results/audit/ai_grounding.csv), [phiếu học viên](results/audit/manual_grounding.csv).
- Trạng thái và cách chốt human audit: [manual_summary.json](results/audit/manual_summary.json), [hướng dẫn chấm](results/audit/README.md). Chưa có người chấm thủ công được xác nhận; nhãn AI không thay cho yêu cầu này.

Đã có **9 kiểm thử đạt**, gồm truy vết text, metric evidence, filter, nạp lại không trùng, lưu bền và xóa chunk cũ; kết quả ở [tests.xml](results/tests.xml). Lần tái lập trên index mới dùng cache embedding cho cùng chunk dumps, điểm dev/test và lựa chọn A, được ghi tại [reproduction_check.json](results/reproduction_check.json). Đây là kiểm tra tái lập sau khi đã xem test, không phải một holdout mới.

## Phân tích và kết luận

**So sánh A–B và B–C theo năm khía cạnh**

1. **Retrieval accuracy:** A đạt dev Hit@3 cao hơn B/C một câu, nhưng Hit@1 thấp hơn bốn câu. B giúp bằng chứng đúng xuất hiện ở rank đầu thường xuyên hơn trên dev, trong khi A bao phủ thêm một câu khi xét cả top-3. Trên test, A/B cùng 4/5; C đạt 5/5 nhưng chỉ có năm câu, chưa đủ để suy rộng.
2. **Chunk coherence:** theo nháp AI, B/C giữ khoản và câu tốt hơn A. Cấu hình A thường cắt giữa từ hoặc điều kiện; B/C vẫn có thể mất tiêu đề điều, câu dẫn danh sách và nội dung ở trang tiếp nối. Kết luận định tính cần học viên xác nhận bằng phiếu chấm; mẫu chỉ lấy 10 trang đầu nên chưa đại diện toàn corpus.
3. **Metadata usefulness:** `source/page/offsets` giúp kiểm tra chunk với nguồn; `section` giúp lọc đúng phạm vi như Q20. Metadata đủ/đúng không chứng minh nội dung đủ trả lời. Nếu người dùng đưa nhầm chương, filter có thể loại đáp án đúng; thí nghiệm chưa đo tình huống đó.
4. **Grounding quality:** A/Q16 có con số liên quan nhưng thiếu điều kiện, nên nháp grounding chỉ đạt mức 1. B/Q20 không có bằng chứng chuyển tiếp nên mức 0. Các nhãn được giải thích từng câu, không suy ra máy móc từ Hit@3 và chưa được coi là human audit.
5. **Data strategy impact:** B giảm **87 chunk**, giảm token đầu vào và thời gian ingest quan sát được so với A. C tái sử dụng vector/index của B nên không phát sinh document embedding riêng; lợi ích là giới hạn phạm vi, không sửa biên chunk. A–B đồng thời đổi nhiều tham số nên chưa xác định được ảnh hưởng riêng của size hoặc overlap.

**Hai ví dụ sai có ID câu và nguồn**

| Trường hợp | Nguồn gold | Kết quả và nguyên nhân |
|---|---|---|
| **A — Q16** | `traffic-law-part2`, trang vật lý 2, Điều 25 khoản 2 | Rank 2 có khoảng cách 150 mét nhưng bắt đầu ở đuôi từ “cấp”, thiếu điều kiện xe không thể vào làn dừng khẩn cấp và phần bật đèn. Vì không chứa đủ evidence, Hit@3 = 0 dù đúng trang; grounding AI = 1. B/C giữ được toàn bộ điều kiện ở rank 3. |
| **B — Q20** | `traffic-law-part2`, trang vật lý 58, Điều 89 khoản 1, Chương IX | Top-3 thuộc các trang 33/32/37 Chương IV về điểm, hiệu lực/giấy phép quốc tế và cấp đổi; không đủ trả lời quy định chuyển tiếp. C nhận phạm vi IX từ câu hỏi nên truy được đúng Điều 89 ở rank 2. |

Có thể đối chiếu cả hai trường hợp bằng `strategy` và `question_id` trong [traces_test.jsonl](results/run/traces_test.jsonl).

**Chiến lược chọn, đánh đổi và điều kiện áp dụng**

Giữ **A là chiến lược được chọn theo quy tắc dev đã khóa**, ưu tiên tìm đủ evidence trong top-3. Đánh đổi là nhiều chunk/token hơn và chất lượng mạch lạc thấp hơn trong nháp audit. B phù hợp để tiếp tục nghiên cứu khi muốn đoạn dễ đọc và ít chunk hơn; C có ích khi người hỏi cung cấp đúng chương. Kết quả test cao hơn của C được dùng để phân tích, không làm căn cứ chọn lại cấu hình cho thí nghiệm này.

**Hạn chế của dữ liệu, nhãn, test nhỏ và thời gian/chi phí**

Corpus chỉ là một luật gốc năm 2024, chưa bao gồm nghị định về mức phạt hoặc toàn bộ sửa đổi. Bộ câu hỏi có 20 câu, test chỉ năm câu; một câu tương đương 20 điểm phần trăm. Có chủ đề/trang gần nhau giữa dev và test, nên mức độc lập còn hạn chế. Metric exact evidence có thể bỏ sót bằng chứng tương đương nếu chưa được khai báo và xác minh.

AI hỗ trợ soạn benchmark và chấm nháp sau khi đã xem trace/điểm, có nguy cơ thiên lệch; chưa có người học kiểm chứng độc lập. Human audit cần được hoàn thành trước khi coi các điểm coherence, metadata và grounding là nhãn chấm thủ công của bài nộp. Thời gian chỉ là số đo trên một máy, chịu ảnh hưởng thứ tự chạy và cache; HNSW là approximate search. Chi phí 0 USD chỉ nói về API, chưa bao gồm điện và phần cứng.

**Nếu làm lại hoặc mở rộng**

Xây một thí nghiệm mới với chunk theo Điều, kèm tiêu đề và ngữ cảnh; xử lý khoản nối trang bằng `page_start/page_end`; loại chữ ký số sau xác minh; mở rộng corpus và số câu hỏi; chia test theo chủ đề hoặc tài liệu khi khả thi; so sánh riêng từng kích thước/overlap. Các thay đổi sau khi đã xem test phải được ghi nhận và cần tập test mới nếu muốn đánh giá độc lập.

Codex được dùng để hỗ trợ đọc yêu cầu, viết code, tìm nguồn, soạn benchmark, chạy model thật và phân tích. Số liệu định lượng trong báo cáo lấy từ artifacts đã chạy. Học viên cần tự đối chiếu evidence, hoàn thành các phiếu human audit, ghi người chấm và lý do, cập nhật bảng nhãn thủ công rồi chốt commit/nộp link theo hướng dẫn lớp.
