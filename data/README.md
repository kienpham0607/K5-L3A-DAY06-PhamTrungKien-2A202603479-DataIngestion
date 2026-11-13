# Corpus giao thông

Hai PDF bản gốc năm 2024 của Luật 36/2024/QH15 được tải từ [Cổng TTĐT Chính phủ](https://vanban.chinhphu.vn/?classid=1&docid=211194&pageid=27160). [manifest.json](manifest.json) ghi URL chính thức, quyền sử dụng, ngày truy cập thực tế, SHA-256, trang tính/loại và số ký tự mỗi trang. Chỉ xử lý bản văn luật; không thu thập bình luận pháp lý.

- `raw/36-2024-qh15-part1.pdf`: 21 trang vật lý, dùng 1–20; trang 21 là khối thông tin xuất bản dạng ảnh, không có nội dung luật/text trích được.
- `raw/36-2024-qh15-part2.pdf`: 61 trang vật lý, dùng 1–61.
- Tổng **81 trang nội dung**, không đếm segment hay bản sao. Trang đầu có điều luật nên được tính. `printed_page` tách riêng khỏi `page` vật lý.
- `processed/pages.jsonl`: văn bản trích xuất, Unicode NFC, gỡ header/số trang và nối dòng; có nguồn/trang/số ký tự để tái kiểm tra evidence.

Đây là snapshot phục vụ lab, không phải kho cập nhật pháp luật hiện hành hoặc tra cứu mức phạt. Quyền xử lý dựa trên khoản 2 Điều 15 Luật Sở hữu trí tuệ, dẫn nguồn trong manifest; không tự gán giấy phép mở cho nội dung trang web hoặc phần bình luận.

Từ root repo:

```powershell
.venv/Scripts/python.exe starter/scripts/prepare_sources.py
.venv/Scripts/python.exe -m starter.src.run prepare
```

Nếu PDF đã có, `prepare_sources.py` chỉ xác minh hash và **giữ nguyên manifest đã khóa**. Khi thiếu PDF, tải từ URL manifest rồi kiểm tra hash; nếu máy chủ thay file sẽ dừng thay vì lặng lẽ đổi corpus. Pipeline benchmark đọc file local, không cần mạng sau khi tải model.

Giới hạn: chưa OCR; một số chữ ký số của cổng xuất hiện trong text trang đầu. Đã phát hiện trong review sau test và ghi nhận tại [setup_notes.json](../results/setup_notes.json), chưa chỉnh bằng kết quả test. [format-example.json](format-example.json) là mẫu đề bài, không thuộc corpus đo.
