# Starter đã hoàn thiện: bài lab giao thông

Phần triển khai của bài này dùng **Sentence Transformers local + Chroma PersistentClient**, một lựa chọn được GUIDE.md cho phép. Không cần API key hoặc Docker. Các TODO trong `src/` đã được thay bằng pipeline chạy thật.

Đọc [README tại root](../README.md) để xem dữ liệu, cách cài/chạy, kết quả và phần audit thủ công cần học viên xác nhận. Cấu hình đã khóa ở [config.json](config.json).

Nếu đang đứng trong `starter/`, dùng môi trường ảo ở root:

```powershell
../.venv/Scripts/python.exe -m src.run prepare
../.venv/Scripts/python.exe -m src.run query --strategy C --section II --question "Khi nào phải bật đèn chiếu sáng phía trước?"
```

Chạy lại toàn bộ vào **thư mục kết quả/index mới**, giữ nguyên bộ thí nghiệm đã nộp:

```powershell
../.venv/Scripts/python.exe -m src.run all --output ../results/reproduction --store ../artifacts/reproduction-chroma
```

`all` lần lượt kiểm chứng nguồn/evidence, xác minh freeze, ingest + kiểm tra nạp lại, dev + chọn cấu hình, test, xuất mẫu audit. Nếu thư mục output đã có test, lệnh từ chối ghi đè. Tái chạy test cũ là tái lập, không phải holdout mới. Model phải được tải trước theo hướng dẫn root.

| Module | Nhiệm vụ |
|---|---|
| `ingestion.py` | Đọc PDF, NFC, nối dòng, giữ trang, tách chương và ghi lỗi |
| `chunking.py` | Fixed 500/50 và paragraph tối đa 800, giữ offsets/ID ổn định |
| `embeddings.py` | MiniLM đa ngữ thật, revision pin, normalize vectors, cache theo nội dung |
| `store.py` | Chroma cosine HNSW, filter whitelist, upsert/xóa chunk cũ |
| `evaluation.py` | Strict evidence hit đúng nguồn/trang, hỗ trợ alternative_gold |
| `run.py` | CLI prepare/freeze/ingest/dev/test/audit/query/all |

`docker-compose.yml`, `init.sql` và `scripts/check_setup.py` được giữ từ đề bài để tham khảo PostgreSQL + pgvector. Chúng không phải backend dùng trong số liệu của bài nộp này; không cần chạy chúng để tái lập kết quả Chroma.
