# Đối chiếu audit: coherence, grounding và metadata

**Đã ghi nhận học viên Phạm Trung Kiên xác nhận đủ 90 mẫu:** “Đã đối chiếu 20 câu và đủ 90 mẫu; đồng ý các đề xuất”. Nhãn ban đầu do Codex AI đề xuất, học viên chấp nhận sau đối chiếu nguồn. Đã xem gợi ý và kết quả nên có nguy cơ thiên lệch; không phải đánh giá mù. Xem [bản ghi xác nhận](human_confirmation.json), [tổng hợp](manual_summary.json) và ba phiếu manual đã điền.

Coherence: 0 = không hiểu được vì mất ý/chủ thể; 1 = hiểu một phần, thiếu ngữ cảnh; 2 = trọn ý và tự hiểu. Grounding: 0 = không có bằng chứng; 1 = thiếu điều kiện/ngữ cảnh; 2 = đủ trả lời và truy nguồn.

A/P04 được rà soát từ 0 lên 1 vì vẫn hiểu được một phần; coherence AI của A hiện là 0,90/2. Xem [lịch sử sửa nhãn AI](review_corrections.json). Không sửa metrics retrieval hoặc lựa chọn A trên dev.

## 1. Coherence — 30 bản ghi, cùng 10 vị trí nguồn

B/C dùng chính cùng chunk; nội dung chỉ in một lần ở B để tránh đọc lặp. C vẫn có 10 nhãn riêng trong phiếu chấm.

### A/P01 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 1](../../data/raw/36-2024-qh15-part1.pdf#page=1); vị trí mẫu 912; chunk `29e81e1f6dad353166063e3ae5988503`.

**Toàn bộ chunk:**

> ng bộ có trật tự, bảo đảm an toàn, thông suốt; được hình thành và điều chỉnh bởi các quy tắc, nguyên tắc, quy phạm pháp luật trong lĩnh vực giao thông đường bộ.
> 
> 2. Phương tiện giao thông đường bộ là các loại xe, bao gồm: phương tiện giao thông cơ giới đường bộ (sau đây gọi là xe cơ giới), phương tiện giao thông thô sơ đường bộ (sau đây gọi là xe thô sơ), xe máy chuyên dùng và các loại xe tương tự.
> 
> 3. Phương tiện tham gia giao thông đường bộ là phương tiện giao thông đường bộ tham gia giao thôn

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> an đến trật tự, an toàn giao thông đường bộ.
> 
> Điều 2. Giải thích từ ngữ
> 
> 1. Trật tự, an toàn giao thông đường bộ là trạng thái giao thông trên đường bộ có trật tự, bảo đảm an toàn, thông suốt; được hình thành và điều chỉnh bởi các quy tắc, nguyên tắc, quy phạm pháp luật trong lĩnh vực giao thông đường bộ.
> 
> 2. Phương tiện giao thông đường bộ là các loại xe, bao gồm: phương tiện giao thông cơ giới đường bộ (sau đây gọi là xe cơ giới), phương tiện giao thông thô sơ đường bộ (sau đây gọi là xe thô sơ), xe máy chuyên dùng và các loại xe tương tự.
> 
> 3. Phương tiện tham gia giao thông đường bộ là phương tiện giao thông đường bộ tham gia giao thông trên đường bộ.
> 
> 4. Đường ưu tiên là đường mà trên đó phương tiện tham gia giao thông đường bộ được các phương tiện tham gia giao thông đường bộ đến từ hướng khác nhường đường khi qua nơi đường giao nhau

**Lý do AI:** Có trọn định nghĩa phương tiện nhưng đầu và cuối chunk bị cắt giữa từ, thiếu hai định nghĩa lân cận.

- [x] Đã tự đọc mẫu A/P01; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P02 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 2](../../data/raw/36-2024-qh15-part1.pdf#page=2); vị trí mẫu 1054; chunk `8773a4ee8a8033999a746f4ea9adde80`.

**Toàn bộ chunk:**

> ham gia giao thông đường bộ bị dồn ứ, di chuyển với tốc độ rất chậm hoặc không thể di chuyển được.
> 
> 12. Tai nạn giao thông đường bộ là va chạm liên quan đến người, phương tiện khi tham gia giao thông đường bộ, xảy ra ngoài ý muốn của người tham gia giao thông đường bộ, gây thiệt hại đến tính mạng, sức khỏe, tài sản của cá nhân hoặc tài sản của cơ quan, tổ chức.
> 
> 13. Thiết bị an toàn cho trẻ em là thiết bị có đủ khả năng bảo đảm an toàn cho trẻ em ở tư thế ngồi hoặc nằm trên xe ô tô, được thiết k

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ) bao gồm: Cảnh sát giao thông và người được giao nhiệm vụ hướng dẫn giao thông trên đường bộ.
> 
> 11. Ùn tắc giao thông đường bộ (sau đây gọi là ùn tắc giao thông) là tình trạng người, phương tiện tham gia giao thông đường bộ bị dồn ứ, di chuyển với tốc độ rất chậm hoặc không thể di chuyển được.
> 
> 12. Tai nạn giao thông đường bộ là va chạm liên quan đến người, phương tiện khi tham gia giao thông đường bộ, xảy ra ngoài ý muốn của người tham gia giao thông đường bộ, gây thiệt hại đến tính mạng, sức khỏe, tài sản của cá nhân hoặc tài sản của cơ quan, tổ chức.
> 
> 13. Thiết bị an toàn cho trẻ em là thiết bị có đủ khả năng bảo đảm an toàn cho trẻ em ở tư thế ngồi hoặc nằm trên xe ô tô, được thiết kế để giảm nguy cơ chấn thương cho người dùng trong trường hợp xảy ra va chạm hoặc xe ô tô giảm tốc độ đột ngột, bằng cách hạn chế sự di chuyển của cơ thể 

**Lý do AI:** Định nghĩa tai nạn đủ chủ thể và hậu quả; đầu là phần cuối định nghĩa ùn tắc, cuối cắt định nghĩa thiết bị an toàn.

- [x] Đã tự đọc mẫu A/P02; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P03 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 3](../../data/raw/36-2024-qh15-part1.pdf#page=3); vị trí mẫu 1014; chunk `ca25e52b9e80d7b7ba0a1de3f6175d0a`.

**Toàn bộ chunk:**

> ộ phải công khai, minh bạch và thuận lợi cho người dân.
> 
> 7. Công tác bảo đảm trật tự, an toàn giao thông đường bộ được thực hiện thống nhất trên cơ sở phân công, phân cấp, phù hợp với chức năng, nhiệm vụ và sự phối hợp chặt chẽ giữa các cơ quan, tổ chức, cá nhân có liên quan.
> 
> Điều 4. Chính sách của Nhà nước về trật tự, an toàn giao thông đường bộ
> 
> 1. Bảo đảm ngân sách nhà nước, cơ sở vật chất, phương tiện, thiết bị hiện đại, các điều kiện bảo đảm và nâng cao năng lực thực thi nhiệm vụ của lực l

**Ngữ cảnh nguồn quanh vị trí mẫu:**

>  khác.
> 
> 5. Mọi hành vi vi phạm pháp luật về trật tự, an toàn giao thông đường bộ phải được phát hiện, ngăn chặn kịp thời và phải bị xử lý nghiêm minh theo quy định của pháp luật.
> 
> 6. Hoạt động bảo đảm trật tự, an toàn giao thông đường bộ phải công khai, minh bạch và thuận lợi cho người dân.
> 
> 7. Công tác bảo đảm trật tự, an toàn giao thông đường bộ được thực hiện thống nhất trên cơ sở phân công, phân cấp, phù hợp với chức năng, nhiệm vụ và sự phối hợp chặt chẽ giữa các cơ quan, tổ chức, cá nhân có liên quan.
> 
> Điều 4. Chính sách của Nhà nước về trật tự, an toàn giao thông đường bộ
> 
> 1. Bảo đảm ngân sách nhà nước, cơ sở vật chất, phương tiện, thiết bị hiện đại, các điều kiện bảo đảm và nâng cao năng lực thực thi nhiệm vụ của lực lượng trực tiếp bảo đảm trật tự, an toàn giao thông đường bộ. Huy động, sử dụng các nguồn lực để bảo đảm trật tự, a

**Lý do AI:** Khoản 7 nguyên tắc phối hợp còn trọn; hai đầu bị cắt, khoản 1 Điều 4 chưa đủ nội dung.

- [x] Đã tự đọc mẫu A/P03; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P04 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 4](../../data/raw/36-2024-qh15-part1.pdf#page=4); vị trí mẫu 1229; chunk `8571ee97684bd142747395f28b0eab23`.

**Toàn bộ chunk:**

> uật về giao thông đường bộ cho trẻ em, học sinh để hình thành, nâng cao ý thức tự bảo vệ bản thân và tự giác chấp hành pháp luật khi tham gia giao thông đường bộ.
> 
> 5. Cơ quan, tổ chức, cá nhân tham gia phối hợp, cộng tác, hỗ trợ, giúp đỡ cơ quan nhà nước thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ, có thành tích thì được khen thưởng, bị thiệt hại về tài sản thì được đền bù; người bị tổn hại về danh dự, nhân phẩm thì được khôi phục; người bị thương, bị tổn hại về sức khỏe, tín

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ưỡng kiến thức pháp luật về giao thông đường bộ cho trẻ em, học sinh để hình thành, nâng cao ý thức tự bảo vệ bản thân và tự giác chấp hành pháp luật khi tham gia giao thông đường bộ.
> 
> 5. Cơ quan, tổ chức, cá nhân tham gia phối hợp, cộng tác, hỗ trợ, giúp đỡ cơ quan nhà nước thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ, có thành tích thì được khen thưởng, bị thiệt hại về tài sản thì được đền bù; người bị tổn hại về danh dự, nhân phẩm thì được khôi phục; người bị thương, bị tổn hại về sức khỏe, tính mạng thì bản thân, gia đình được hưởng chế độ, chính sách theo quy định của pháp luật.
> 
> 6. Phát triển phương tiện giao thông đường bộ đồng bộ với phát triển kết cấu hạ tầng đường bộ, điều kiện kinh tế - xã hội và nhu cầu đi lại của người dân; nhập khẩu, sản xuất, lắp ráp phương tiện giao thông đường bộ bảo đảm chất lượng an t

**Lý do AI:** Khoản 5 còn giữ được chủ thể và các ý khen thưởng, đền bù tài sản, khôi phục danh dự; phần chế độ cho người bị thương bị cắt cuối. Hiểu được một phần nên mức 1, chưa đủ trọn ý để mức 2. Rà soát lại nhãn AI trước đây là 0.

- [x] Đã tự đọc mẫu A/P04; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P05 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 5](../../data/raw/36-2024-qh15-part1.pdf#page=5); vị trí mẫu 1073; chunk `1ec29e5bdb416efc4caef7a3397606a8`.

**Toàn bộ chunk:**

> n vị lực lượng vũ trang nhân dân, cơ quan, tổ chức, cơ sở giáo dục có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ cho đối tượng thuộc thẩm quyền quản lý.
> 
> 7. Thành viên trong gia đình có trách nhiệm tuyên truyền, nhắc nhở thành viên khác chấp hành pháp luật về trật tự, an toàn giao thông đường bộ, sử dụng dây đai an toàn, ghế dành cho trẻ em hoặc có người lớn ngồi cùng trẻ em phía sau khi chở trẻ em dưới 06 tuổi bằng xe gắn máy, xe mô tô.
> 
> Điều 6.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> của mình, có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ, có hình thức tuyên truyền, phổ biến phù hợp với từng đối tượng.
> 
> 6. Đơn vị lực lượng vũ trang nhân dân, cơ quan, tổ chức, cơ sở giáo dục có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ cho đối tượng thuộc thẩm quyền quản lý.
> 
> 7. Thành viên trong gia đình có trách nhiệm tuyên truyền, nhắc nhở thành viên khác chấp hành pháp luật về trật tự, an toàn giao thông đường bộ, sử dụng dây đai an toàn, ghế dành cho trẻ em hoặc có người lớn ngồi cùng trẻ em phía sau khi chở trẻ em dưới 06 tuổi bằng xe gắn máy, xe mô tô.
> 
> Điều 6. Giáo dục kiến thức pháp luật về trật tự, an toàn giao thông đường bộ
> 
> 1. Giáo dục kiến thức pháp luật về trật tự, an toàn giao thông đường bộ cho trẻ em của cơ sở giáo dục 

**Lý do AI:** Khoản 7 trách nhiệm gia đình được giữ đủ; khoản 6 mất đầu chủ thể và cuối chỉ còn tiêu đề Điều 6.

- [x] Đã tự đọc mẫu A/P05; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P06 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 6](../../data/raw/36-2024-qh15-part1.pdf#page=6); vị trí mẫu 883; chunk `d3e090d401aad25cec28ae08965b6249`.

**Toàn bộ chunk:**

> liệu về đào tạo, sát hạch, cấp giấy phép lái xe, chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ;
> 
> d) Cơ sở dữ liệu về người điều khiển xe cơ giới, xe máy chuyên dùng;
> 
> đ) Cơ sở dữ liệu về bảo hiểm của chủ xe cơ giới, xe máy chuyên dùng;
> 
> e) Cơ sở dữ liệu về xử lý vi phạm hành chính về trật tự, an toàn giao thông đường bộ;
> 
> g) Cơ sở dữ liệu về tai nạn giao thông đường bộ;
> 
> h) Cơ sở dữ liệu về hành trình của phương tiện giao thông đường bộ, hình ảnh người lái xe theo quy định của

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> p luật về giao thông đường bộ;
> 
> d) Cơ sở dữ liệu về người điều khiển xe cơ giới, xe máy chuyên dùng;
> 
> đ) Cơ sở dữ liệu về bảo hiểm của chủ xe cơ giới, xe máy chuyên dùng;
> 
> e) Cơ sở dữ liệu về xử lý vi phạm hành chính về trật tự, an toàn giao thông đường bộ;
> 
> g) Cơ sở dữ liệu về tai nạn giao thông đường bộ;
> 
> h) Cơ sở dữ liệu về hành trình của phương tiện giao thông đường bộ, hình ảnh người lái xe theo quy định của Luật này;
> 
> i) Cơ sở dữ liệu về quản lý thời gian điều khiển phương tiện của người lái xe theo quy định của Luật này;
> 
> k) Cơ sở dữ liệu khác liên quan đến công tác bảo đảm trật tự, an toàn giao thông đường bộ.
> 
> 2. Cơ sở dữ liệu về trật tự, an toàn giao thông đường bộ là cơ sở dữ liệu dùng chung; được kết nối, chia sẻ với Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu đường bộ và các cơ sở dữ liệu khác có liên quan.
> 
> 3. Chính phủ 

**Lý do AI:** Các mục cơ sở dữ liệu đọc được nhưng thiếu câu dẫn danh sách; mục h bị cắt trước phần quy định dẫn chiếu.

- [x] Đã tự đọc mẫu A/P06; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P07 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 7](../../data/raw/36-2024-qh15-part1.pdf#page=7); vị trí mẫu 936; chunk `559f751b1b56c5420c20831a9aca8afb`.

**Toàn bộ chunk:**

> chuyển giao công nghệ có liên quan đến trật tự, an toàn giao thông đường bộ;
> 
> c) Đào tạo, tập huấn, nâng cao năng lực cho lực lượng bảo đảm trật tự, an toàn giao thông đường bộ;
> 
> d) Tăng cường điều kiện vật chất để bảo đảm trật tự, an toàn giao thông đường bộ;
> 
> đ) Giải quyết tai nạn giao thông đường bộ;
> 
> e) Thực hiện nội dung hợp tác quốc tế khác theo quy định của pháp luật Việt Nam và điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
> 
> 3. Bộ Công an chủ trì

**Ngữ cảnh nguồn quanh vị trí mẫu:**

>  đảm trật tự, an toàn giao thông đường bộ;
> 
> d) Tăng cường điều kiện vật chất để bảo đảm trật tự, an toàn giao thông đường bộ;
> 
> đ) Giải quyết tai nạn giao thông đường bộ;
> 
> e) Thực hiện nội dung hợp tác quốc tế khác theo quy định của pháp luật Việt Nam và điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
> 
> 3. Bộ Công an chủ trì, phối hợp với các Bộ, ngành liên quan giúp Chính phủ đàm phán, ký kết điều ước quốc tế, thỏa thuận quốc tế hoặc đề xuất cấp có thẩm quyền ký kết điều ước quốc tế, thỏa thuận quốc tế về trật tự, an toàn giao thông đường bộ; chủ trì, phối hợp với các Bộ, ngành liên quan thực hiện hợp tác quốc tế về trật tự, an toàn giao thông đường bộ.
> 
> Điều 9. Các hành vi bị nghiêm cấm
> 
> 1. Điều khiển xe cơ giới tham gia giao thông đường bộ không có giấy phép lái xe theo quy định của pháp luật; điều

**Lý do AI:** Một số mục hợp tác quốc tế đủ nội dung; thiếu câu dẫn, khoản 3 bị dừng ngay sau Bộ Công an chủ trì.

- [x] Đã tự đọc mẫu A/P07; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P08 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 8](../../data/raw/36-2024-qh15-part1.pdf#page=8); vị trí mẫu 1086; chunk `41baa334b41b1a5cf78b91fe06bfbf4c`.

**Toàn bộ chunk:**

> áy chuyên dùng không bảo đảm quy định của pháp luật về chất lượng an toàn kỹ thuật và bảo vệ môi trường.
> 
> 10. Cải tạo xe ô tô loại khác thành xe ô tô chở người, trừ cải tạo thành xe ô tô chở người phục vụ mục đích quốc phòng, an ninh.
> 
> 11. Cải tạo trái phép; cố ý can thiệp làm sai lệch chỉ số trên đồng hồ báo quãng đường đã chạy của xe ô tô; cắt, hàn, tẩy xóa, đục sửa, đóng lại trái phép số khung, số động cơ của xe cơ giới, xe máy chuyên dùng.
> 
> 12. Cố ý can thiệp, thay đổi phần mềm điều khiển củ

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ảo vệ môi trường, phương tiện khác không đủ điều kiện theo quy định của pháp luật để tham gia giao thông đường bộ.
> 
> 9. Nhập khẩu, sản xuất, lắp ráp xe cơ giới, xe máy chuyên dùng không bảo đảm quy định của pháp luật về chất lượng an toàn kỹ thuật và bảo vệ môi trường.
> 
> 10. Cải tạo xe ô tô loại khác thành xe ô tô chở người, trừ cải tạo thành xe ô tô chở người phục vụ mục đích quốc phòng, an ninh.
> 
> 11. Cải tạo trái phép; cố ý can thiệp làm sai lệch chỉ số trên đồng hồ báo quãng đường đã chạy của xe ô tô; cắt, hàn, tẩy xóa, đục sửa, đóng lại trái phép số khung, số động cơ của xe cơ giới, xe máy chuyên dùng.
> 
> 12. Cố ý can thiệp, thay đổi phần mềm điều khiển của xe, động cơ của xe đã được đăng ký với cơ quan quản lý, nhằm mục đích gian lận kết quả kiểm tra, thử nghiệm, kiểm định; thuê, mượn phụ tùng xe cơ giới chỉ để thực hiện việc kiểm định.

**Lý do AI:** Khoản 10 và 11 đủ câu nhưng mất tiêu đề hành vi nghiêm cấm; đầu, cuối bị cắt giữa từ.

- [x] Đã tự đọc mẫu A/P08; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P09 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 9](../../data/raw/36-2024-qh15-part1.pdf#page=9); vị trí mẫu 1019; chunk `e2928714e055c1ee1023c58d833d0c51`.

**Toàn bộ chunk:**

> t bị thông minh hỗ trợ chỉ huy, điều khiển giao thông đường bộ.
> 
> 20. Đặt, để chướng ngại vật, vật cản khác trái phép trên đường bộ; rải vật sắc nhọn, đổ chất gây trơn trượt trên đường bộ; làm rơi vãi đất đá, hàng hóa, vật liệu xây dựng, phế thải trên đường bộ; đổ, xả thải, làm rơi vãi hóa chất, chất thải gây mất an toàn giao thông đường bộ.
> 
> 21. Cản trở người, phương tiện tham gia giao thông trên đường bộ; ném gạch, đất, đá, cát hoặc vật thể khác vào người, phương tiện đang tham gia giao thông t

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> Làm gián đoạn hoạt động hoặc làm sai lệch dữ liệu của thiết bị giám sát hành trình, camera lắp trên xe theo quy định của Luật này.
> 
> 19. Hủy hoại, làm hư hỏng, làm mất tác dụng thiết bị điều khiển, giám sát giao thông đường bộ, thiết bị thông minh hỗ trợ chỉ huy, điều khiển giao thông đường bộ.
> 
> 20. Đặt, để chướng ngại vật, vật cản khác trái phép trên đường bộ; rải vật sắc nhọn, đổ chất gây trơn trượt trên đường bộ; làm rơi vãi đất đá, hàng hóa, vật liệu xây dựng, phế thải trên đường bộ; đổ, xả thải, làm rơi vãi hóa chất, chất thải gây mất an toàn giao thông đường bộ.
> 
> 21. Cản trở người, phương tiện tham gia giao thông trên đường bộ; ném gạch, đất, đá, cát hoặc vật thể khác vào người, phương tiện đang tham gia giao thông trên đường bộ.
> 
> 22. Lợi dụng, lạm dụng nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ để thực hiện hành vi vi phạ

**Lý do AI:** Khoản 20 về đặt vật cản và chất thải đủ; đầu còn đuôi khoản 19, cuối cắt khoản 21 và thiếu tiêu đề cấm.

- [x] Đã tự đọc mẫu A/P09; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/P10 — đề xuất 0/2

Nguồn: [traffic-law-part1, PDF trang 10](../../data/raw/36-2024-qh15-part1.pdf#page=10); vị trí mẫu 1013; chunk `940793a248e159faf27e2c28b1186a7a`.

**Toàn bộ chunk:**

> lái, phương tiện bay siêu nhẹ được cấp phép bay.
> 
> 28. Hành vi khác vi phạm quy tắc giao thông đường bộ quy định tại Chương II của Luật này.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> 27. Điều khiển vật thể bay, tàu bay không người lái, phương tiện bay siêu nhẹ hoạt động trong phạm vi khổ giới hạn đường bộ gây cản trở hoặc nguy cơ mất an toàn cho người, phương tiện tham gia giao thông đường bộ, trừ tàu bay không người lái, phương tiện bay siêu nhẹ được cấp phép bay.
> 
> 28. Hành vi khác vi phạm quy tắc giao thông đường bộ quy định tại Chương II của Luật này.
> 
> Chương II
> 
> QUY TẮC GIAO THÔNG ĐƯỜNG BỘ
> 
> Điều 10. Quy tắc chung
> 
> 1. Người tham gia giao thông đường bộ phải đi bên phải theo chiều đi của mình, đi đúng làn đường, phần đường quy định, chấp hành báo hiệu đường bộ và các quy tắc giao thông đường bộ khác.
> 
> 2. Người lái xe và người được chở trên xe ô tô phải thắt dây đai an toàn tại những chỗ có trang bị dây đai an toàn khi tham gia giao thông đường bộ.
> 
> 3. Khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 mét trên xe ô 

**Lý do AI:** Đầu là đuôi ngoại lệ tàu bay; khoản 28 chỉ dẫn hành vi khác theo Chương II, không tự giải thích được nội dung tại vị trí mẫu.

- [x] Đã tự đọc mẫu A/P10; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P01 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 1](../../data/raw/36-2024-qh15-part1.pdf#page=1); vị trí mẫu 912; chunk `eb0ede421e043fa8a2b1b2dfaa34d7e2`.

**Toàn bộ chunk:**

> Điều 2. Giải thích từ ngữ
> 
> 1. Trật tự, an toàn giao thông đường bộ là trạng thái giao thông trên đường bộ có trật tự, bảo đảm an toàn, thông suốt; được hình thành và điều chỉnh bởi các quy tắc, nguyên tắc, quy phạm pháp luật trong lĩnh vực giao thông đường bộ.
> 
> 2. Phương tiện giao thông đường bộ là các loại xe, bao gồm: phương tiện giao thông cơ giới đường bộ (sau đây gọi là xe cơ giới), phương tiện giao thông thô sơ đường bộ (sau đây gọi là xe thô sơ), xe máy chuyên dùng và các loại xe tương tự.
> 
> 3. Phương tiện tham gia giao thông đường bộ là phương tiện giao thông đường bộ tham gia giao thông trên đường bộ.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> an đến trật tự, an toàn giao thông đường bộ.
> 
> Điều 2. Giải thích từ ngữ
> 
> 1. Trật tự, an toàn giao thông đường bộ là trạng thái giao thông trên đường bộ có trật tự, bảo đảm an toàn, thông suốt; được hình thành và điều chỉnh bởi các quy tắc, nguyên tắc, quy phạm pháp luật trong lĩnh vực giao thông đường bộ.
> 
> 2. Phương tiện giao thông đường bộ là các loại xe, bao gồm: phương tiện giao thông cơ giới đường bộ (sau đây gọi là xe cơ giới), phương tiện giao thông thô sơ đường bộ (sau đây gọi là xe thô sơ), xe máy chuyên dùng và các loại xe tương tự.
> 
> 3. Phương tiện tham gia giao thông đường bộ là phương tiện giao thông đường bộ tham gia giao thông trên đường bộ.
> 
> 4. Đường ưu tiên là đường mà trên đó phương tiện tham gia giao thông đường bộ được các phương tiện tham gia giao thông đường bộ đến từ hướng khác nhường đường khi qua nơi đường giao nhau

**Lý do AI:** Giữ tiêu đề Điều 2 và trọn ba định nghĩa đầu, có đủ chủ thể và vị ngữ.

- [x] Đã tự đọc mẫu B/P01; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P02 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 2](../../data/raw/36-2024-qh15-part1.pdf#page=2); vị trí mẫu 1054; chunk `4aa34de6b07f5e77ebe7d0f187d27cda`.

**Toàn bộ chunk:**

> 11. Ùn tắc giao thông đường bộ (sau đây gọi là ùn tắc giao thông) là tình trạng người, phương tiện tham gia giao thông đường bộ bị dồn ứ, di chuyển với tốc độ rất chậm hoặc không thể di chuyển được.
> 
> 12. Tai nạn giao thông đường bộ là va chạm liên quan đến người, phương tiện khi tham gia giao thông đường bộ, xảy ra ngoài ý muốn của người tham gia giao thông đường bộ, gây thiệt hại đến tính mạng, sức khỏe, tài sản của cá nhân hoặc tài sản của cơ quan, tổ chức.
> 
> 13. Thiết bị an toàn cho trẻ em là thiết bị có đủ khả năng bảo đảm an toàn cho trẻ em ở tư thế ngồi hoặc nằm trên xe ô tô, được thiết kế để giảm nguy cơ chấn thương cho người dùng trong trường hợp xảy ra va chạm hoặc xe ô tô giảm tốc độ đột ngột, bằng cách hạn chế sự di chuyển của cơ thể trẻ em.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ) bao gồm: Cảnh sát giao thông và người được giao nhiệm vụ hướng dẫn giao thông trên đường bộ.
> 
> 11. Ùn tắc giao thông đường bộ (sau đây gọi là ùn tắc giao thông) là tình trạng người, phương tiện tham gia giao thông đường bộ bị dồn ứ, di chuyển với tốc độ rất chậm hoặc không thể di chuyển được.
> 
> 12. Tai nạn giao thông đường bộ là va chạm liên quan đến người, phương tiện khi tham gia giao thông đường bộ, xảy ra ngoài ý muốn của người tham gia giao thông đường bộ, gây thiệt hại đến tính mạng, sức khỏe, tài sản của cá nhân hoặc tài sản của cơ quan, tổ chức.
> 
> 13. Thiết bị an toàn cho trẻ em là thiết bị có đủ khả năng bảo đảm an toàn cho trẻ em ở tư thế ngồi hoặc nằm trên xe ô tô, được thiết kế để giảm nguy cơ chấn thương cho người dùng trong trường hợp xảy ra va chạm hoặc xe ô tô giảm tốc độ đột ngột, bằng cách hạn chế sự di chuyển của cơ thể 

**Lý do AI:** Ba định nghĩa ùn tắc, tai nạn và thiết bị an toàn đều trọn câu, tự hiểu được.

- [x] Đã tự đọc mẫu B/P02; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P03 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 3](../../data/raw/36-2024-qh15-part1.pdf#page=3); vị trí mẫu 1014; chunk `093711d60db1680f7d118fcaba05f15a`.

**Toàn bộ chunk:**

> 5. Mọi hành vi vi phạm pháp luật về trật tự, an toàn giao thông đường bộ phải được phát hiện, ngăn chặn kịp thời và phải bị xử lý nghiêm minh theo quy định của pháp luật.
> 
> 6. Hoạt động bảo đảm trật tự, an toàn giao thông đường bộ phải công khai, minh bạch và thuận lợi cho người dân.
> 
> 7. Công tác bảo đảm trật tự, an toàn giao thông đường bộ được thực hiện thống nhất trên cơ sở phân công, phân cấp, phù hợp với chức năng, nhiệm vụ và sự phối hợp chặt chẽ giữa các cơ quan, tổ chức, cá nhân có liên quan.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

>  khác.
> 
> 5. Mọi hành vi vi phạm pháp luật về trật tự, an toàn giao thông đường bộ phải được phát hiện, ngăn chặn kịp thời và phải bị xử lý nghiêm minh theo quy định của pháp luật.
> 
> 6. Hoạt động bảo đảm trật tự, an toàn giao thông đường bộ phải công khai, minh bạch và thuận lợi cho người dân.
> 
> 7. Công tác bảo đảm trật tự, an toàn giao thông đường bộ được thực hiện thống nhất trên cơ sở phân công, phân cấp, phù hợp với chức năng, nhiệm vụ và sự phối hợp chặt chẽ giữa các cơ quan, tổ chức, cá nhân có liên quan.
> 
> Điều 4. Chính sách của Nhà nước về trật tự, an toàn giao thông đường bộ
> 
> 1. Bảo đảm ngân sách nhà nước, cơ sở vật chất, phương tiện, thiết bị hiện đại, các điều kiện bảo đảm và nâng cao năng lực thực thi nhiệm vụ của lực lượng trực tiếp bảo đảm trật tự, an toàn giao thông đường bộ. Huy động, sử dụng các nguồn lực để bảo đảm trật tự, a

**Lý do AI:** Giữ trọn khoản 5-7 về phát hiện vi phạm, minh bạch và phối hợp quản lý.

- [x] Đã tự đọc mẫu B/P03; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P04 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 4](../../data/raw/36-2024-qh15-part1.pdf#page=4); vị trí mẫu 1229; chunk `d4b150ac8bfb9d67f60a95353ce8fbd1`.

**Toàn bộ chunk:**

> 5. Cơ quan, tổ chức, cá nhân tham gia phối hợp, cộng tác, hỗ trợ, giúp đỡ cơ quan nhà nước thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ, có thành tích thì được khen thưởng, bị thiệt hại về tài sản thì được đền bù; người bị tổn hại về danh dự, nhân phẩm thì được khôi phục; người bị thương, bị tổn hại về sức khỏe, tính mạng thì bản thân, gia đình được hưởng chế độ, chính sách theo quy định của pháp luật.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ưỡng kiến thức pháp luật về giao thông đường bộ cho trẻ em, học sinh để hình thành, nâng cao ý thức tự bảo vệ bản thân và tự giác chấp hành pháp luật khi tham gia giao thông đường bộ.
> 
> 5. Cơ quan, tổ chức, cá nhân tham gia phối hợp, cộng tác, hỗ trợ, giúp đỡ cơ quan nhà nước thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ, có thành tích thì được khen thưởng, bị thiệt hại về tài sản thì được đền bù; người bị tổn hại về danh dự, nhân phẩm thì được khôi phục; người bị thương, bị tổn hại về sức khỏe, tính mạng thì bản thân, gia đình được hưởng chế độ, chính sách theo quy định của pháp luật.
> 
> 6. Phát triển phương tiện giao thông đường bộ đồng bộ với phát triển kết cấu hạ tầng đường bộ, điều kiện kinh tế - xã hội và nhu cầu đi lại của người dân; nhập khẩu, sản xuất, lắp ráp phương tiện giao thông đường bộ bảo đảm chất lượng an t

**Lý do AI:** Khoản 5 giữ đủ đối tượng hỗ trợ, thành tích và các điều kiện bồi thường/chế độ.

- [x] Đã tự đọc mẫu B/P04; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P05 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 5](../../data/raw/36-2024-qh15-part1.pdf#page=5); vị trí mẫu 1073; chunk `27947c86ed83a05960908b522ce947d4`.

**Toàn bộ chunk:**

> 5. Bộ, cơ quan ngang Bộ, Ủy ban nhân dân các cấp, trong phạm vi nhiệm vụ, quyền hạn của mình, có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ, có hình thức tuyên truyền, phổ biến phù hợp với từng đối tượng.
> 
> 6. Đơn vị lực lượng vũ trang nhân dân, cơ quan, tổ chức, cơ sở giáo dục có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ cho đối tượng thuộc thẩm quyền quản lý.
> 
> 7. Thành viên trong gia đình có trách nhiệm tuyên truyền, nhắc nhở thành viên khác chấp hành pháp luật về trật tự, an toàn giao thông đường bộ, sử dụng dây đai an toàn, ghế dành cho trẻ em hoặc có người lớn ngồi cùng trẻ em phía sau khi chở trẻ em dưới 06 tuổi bằng xe gắn máy, xe mô tô.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> của mình, có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ, có hình thức tuyên truyền, phổ biến phù hợp với từng đối tượng.
> 
> 6. Đơn vị lực lượng vũ trang nhân dân, cơ quan, tổ chức, cơ sở giáo dục có trách nhiệm tổ chức tuyên truyền, phổ biến pháp luật về trật tự, an toàn giao thông đường bộ cho đối tượng thuộc thẩm quyền quản lý.
> 
> 7. Thành viên trong gia đình có trách nhiệm tuyên truyền, nhắc nhở thành viên khác chấp hành pháp luật về trật tự, an toàn giao thông đường bộ, sử dụng dây đai an toàn, ghế dành cho trẻ em hoặc có người lớn ngồi cùng trẻ em phía sau khi chở trẻ em dưới 06 tuổi bằng xe gắn máy, xe mô tô.
> 
> Điều 6. Giáo dục kiến thức pháp luật về trật tự, an toàn giao thông đường bộ
> 
> 1. Giáo dục kiến thức pháp luật về trật tự, an toàn giao thông đường bộ cho trẻ em của cơ sở giáo dục 

**Lý do AI:** Khoản 5-7 giữ các chủ thể tuyên truyền, trách nhiệm gia đình và điều kiện chở trẻ.

- [x] Đã tự đọc mẫu B/P05; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P06 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 6](../../data/raw/36-2024-qh15-part1.pdf#page=6); vị trí mẫu 883; chunk `2861c372477031dbc6c3cad79bf66691`.

**Toàn bộ chunk:**

> Điều 7. Cơ sở dữ liệu về trật tự, an toàn giao thông đường bộ
> 
> 1. Cơ sở dữ liệu về trật tự, an toàn giao thông đường bộ bao gồm:
> 
> a) Cơ sở dữ liệu về đăng ký, quản lý xe cơ giới, xe máy chuyên dùng;
> 
> b) Cơ sở dữ liệu về đăng kiểm xe cơ giới, xe máy chuyên dùng;
> 
> c) Cơ sở dữ liệu về đào tạo, sát hạch, cấp giấy phép lái xe, chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ;
> 
> d) Cơ sở dữ liệu về người điều khiển xe cơ giới, xe máy chuyên dùng;
> 
> đ) Cơ sở dữ liệu về bảo hiểm của chủ xe cơ giới, xe máy chuyên dùng;
> 
> e) Cơ sở dữ liệu về xử lý vi phạm hành chính về trật tự, an toàn giao thông đường bộ;
> 
> g) Cơ sở dữ liệu về tai nạn giao thông đường bộ;
> 
> h) Cơ sở dữ liệu về hành trình của phương tiện giao thông đường bộ, hình ảnh người lái xe theo quy định của Luật này;

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> p luật về giao thông đường bộ;
> 
> d) Cơ sở dữ liệu về người điều khiển xe cơ giới, xe máy chuyên dùng;
> 
> đ) Cơ sở dữ liệu về bảo hiểm của chủ xe cơ giới, xe máy chuyên dùng;
> 
> e) Cơ sở dữ liệu về xử lý vi phạm hành chính về trật tự, an toàn giao thông đường bộ;
> 
> g) Cơ sở dữ liệu về tai nạn giao thông đường bộ;
> 
> h) Cơ sở dữ liệu về hành trình của phương tiện giao thông đường bộ, hình ảnh người lái xe theo quy định của Luật này;
> 
> i) Cơ sở dữ liệu về quản lý thời gian điều khiển phương tiện của người lái xe theo quy định của Luật này;
> 
> k) Cơ sở dữ liệu khác liên quan đến công tác bảo đảm trật tự, an toàn giao thông đường bộ.
> 
> 2. Cơ sở dữ liệu về trật tự, an toàn giao thông đường bộ là cơ sở dữ liệu dùng chung; được kết nối, chia sẻ với Cơ sở dữ liệu quốc gia về dân cư, Cơ sở dữ liệu đường bộ và các cơ sở dữ liệu khác có liên quan.
> 
> 3. Chính phủ 

**Lý do AI:** Có Điều 7 và câu dẫn danh sách, nhưng chunk chỉ tới mục h, các mục i/k nằm chunk kế tiếp; chưa đủ toàn bộ danh mục.

- [x] Đã tự đọc mẫu B/P06; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P07 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 7](../../data/raw/36-2024-qh15-part1.pdf#page=7); vị trí mẫu 936; chunk `321f72fb15ca5a232068a5be8600247c`.

**Toàn bộ chunk:**

> e) Thực hiện nội dung hợp tác quốc tế khác theo quy định của pháp luật Việt Nam và điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
> 
> 3. Bộ Công an chủ trì, phối hợp với các Bộ, ngành liên quan giúp Chính phủ đàm phán, ký kết điều ước quốc tế, thỏa thuận quốc tế hoặc đề xuất cấp có thẩm quyền ký kết điều ước quốc tế, thỏa thuận quốc tế về trật tự, an toàn giao thông đường bộ; chủ trì, phối hợp với các Bộ, ngành liên quan thực hiện hợp tác quốc tế về trật tự, an toàn giao thông đường bộ.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

>  đảm trật tự, an toàn giao thông đường bộ;
> 
> d) Tăng cường điều kiện vật chất để bảo đảm trật tự, an toàn giao thông đường bộ;
> 
> đ) Giải quyết tai nạn giao thông đường bộ;
> 
> e) Thực hiện nội dung hợp tác quốc tế khác theo quy định của pháp luật Việt Nam và điều ước quốc tế có liên quan mà nước Cộng hòa xã hội chủ nghĩa Việt Nam là thành viên.
> 
> 3. Bộ Công an chủ trì, phối hợp với các Bộ, ngành liên quan giúp Chính phủ đàm phán, ký kết điều ước quốc tế, thỏa thuận quốc tế hoặc đề xuất cấp có thẩm quyền ký kết điều ước quốc tế, thỏa thuận quốc tế về trật tự, an toàn giao thông đường bộ; chủ trì, phối hợp với các Bộ, ngành liên quan thực hiện hợp tác quốc tế về trật tự, an toàn giao thông đường bộ.
> 
> Điều 9. Các hành vi bị nghiêm cấm
> 
> 1. Điều khiển xe cơ giới tham gia giao thông đường bộ không có giấy phép lái xe theo quy định của pháp luật; điều

**Lý do AI:** Khoản 3 về cơ quan chủ trì đủ nội dung nhưng bắt đầu bằng mục e thiếu câu dẫn danh sách hợp tác quốc tế.

- [x] Đã tự đọc mẫu B/P07; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P08 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 8](../../data/raw/36-2024-qh15-part1.pdf#page=8); vị trí mẫu 1086; chunk `3f991c4b16e0392fac9de20e981d96bf`.

**Toàn bộ chunk:**

> 8. Đưa xe cơ giới, xe máy chuyên dùng không bảo đảm quy định của pháp luật về an toàn kỹ thuật và bảo vệ môi trường, phương tiện khác không đủ điều kiện theo quy định của pháp luật để tham gia giao thông đường bộ.
> 
> 9. Nhập khẩu, sản xuất, lắp ráp xe cơ giới, xe máy chuyên dùng không bảo đảm quy định của pháp luật về chất lượng an toàn kỹ thuật và bảo vệ môi trường.
> 
> 10. Cải tạo xe ô tô loại khác thành xe ô tô chở người, trừ cải tạo thành xe ô tô chở người phục vụ mục đích quốc phòng, an ninh.
> 
> 11. Cải tạo trái phép; cố ý can thiệp làm sai lệch chỉ số trên đồng hồ báo quãng đường đã chạy của xe ô tô; cắt, hàn, tẩy xóa, đục sửa, đóng lại trái phép số khung, số động cơ của xe cơ giới, xe máy chuyên dùng.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> ảo vệ môi trường, phương tiện khác không đủ điều kiện theo quy định của pháp luật để tham gia giao thông đường bộ.
> 
> 9. Nhập khẩu, sản xuất, lắp ráp xe cơ giới, xe máy chuyên dùng không bảo đảm quy định của pháp luật về chất lượng an toàn kỹ thuật và bảo vệ môi trường.
> 
> 10. Cải tạo xe ô tô loại khác thành xe ô tô chở người, trừ cải tạo thành xe ô tô chở người phục vụ mục đích quốc phòng, an ninh.
> 
> 11. Cải tạo trái phép; cố ý can thiệp làm sai lệch chỉ số trên đồng hồ báo quãng đường đã chạy của xe ô tô; cắt, hàn, tẩy xóa, đục sửa, đóng lại trái phép số khung, số động cơ của xe cơ giới, xe máy chuyên dùng.
> 
> 12. Cố ý can thiệp, thay đổi phần mềm điều khiển của xe, động cơ của xe đã được đăng ký với cơ quan quản lý, nhằm mục đích gian lận kết quả kiểm tra, thử nghiệm, kiểm định; thuê, mượn phụ tùng xe cơ giới chỉ để thực hiện việc kiểm định.

**Lý do AI:** Các khoản 8-11 trọn câu, nhưng thiếu tiêu đề Điều 9; người đọc không thấy rõ toàn bộ chúng là hành vi bị nghiêm cấm.

- [x] Đã tự đọc mẫu B/P08; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P09 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 9](../../data/raw/36-2024-qh15-part1.pdf#page=9); vị trí mẫu 1019; chunk `9308d00226440292caea4d1a017e64c6`.

**Toàn bộ chunk:**

> 19. Hủy hoại, làm hư hỏng, làm mất tác dụng thiết bị điều khiển, giám sát giao thông đường bộ, thiết bị thông minh hỗ trợ chỉ huy, điều khiển giao thông đường bộ.
> 
> 20. Đặt, để chướng ngại vật, vật cản khác trái phép trên đường bộ; rải vật sắc nhọn, đổ chất gây trơn trượt trên đường bộ; làm rơi vãi đất đá, hàng hóa, vật liệu xây dựng, phế thải trên đường bộ; đổ, xả thải, làm rơi vãi hóa chất, chất thải gây mất an toàn giao thông đường bộ.
> 
> 21. Cản trở người, phương tiện tham gia giao thông trên đường bộ; ném gạch, đất, đá, cát hoặc vật thể khác vào người, phương tiện đang tham gia giao thông trên đường bộ.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> Làm gián đoạn hoạt động hoặc làm sai lệch dữ liệu của thiết bị giám sát hành trình, camera lắp trên xe theo quy định của Luật này.
> 
> 19. Hủy hoại, làm hư hỏng, làm mất tác dụng thiết bị điều khiển, giám sát giao thông đường bộ, thiết bị thông minh hỗ trợ chỉ huy, điều khiển giao thông đường bộ.
> 
> 20. Đặt, để chướng ngại vật, vật cản khác trái phép trên đường bộ; rải vật sắc nhọn, đổ chất gây trơn trượt trên đường bộ; làm rơi vãi đất đá, hàng hóa, vật liệu xây dựng, phế thải trên đường bộ; đổ, xả thải, làm rơi vãi hóa chất, chất thải gây mất an toàn giao thông đường bộ.
> 
> 21. Cản trở người, phương tiện tham gia giao thông trên đường bộ; ném gạch, đất, đá, cát hoặc vật thể khác vào người, phương tiện đang tham gia giao thông trên đường bộ.
> 
> 22. Lợi dụng, lạm dụng nhiệm vụ bảo đảm trật tự, an toàn giao thông đường bộ để thực hiện hành vi vi phạ

**Lý do AI:** Các khoản 19-21 trọn câu nhưng thiếu tiêu đề xác định đây là các hành vi bị nghiêm cấm.

- [x] Đã tự đọc mẫu B/P09; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/P10 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 10](../../data/raw/36-2024-qh15-part1.pdf#page=10); vị trí mẫu 1013; chunk `e0d6e6d7f23b212371d6ab55ee1f0b4e`.

**Toàn bộ chunk:**

> 27. Điều khiển vật thể bay, tàu bay không người lái, phương tiện bay siêu nhẹ hoạt động trong phạm vi khổ giới hạn đường bộ gây cản trở hoặc nguy cơ mất an toàn cho người, phương tiện tham gia giao thông đường bộ, trừ tàu bay không người lái, phương tiện bay siêu nhẹ được cấp phép bay.
> 
> 28. Hành vi khác vi phạm quy tắc giao thông đường bộ quy định tại Chương II của Luật này.

**Ngữ cảnh nguồn quanh vị trí mẫu:**

> 27. Điều khiển vật thể bay, tàu bay không người lái, phương tiện bay siêu nhẹ hoạt động trong phạm vi khổ giới hạn đường bộ gây cản trở hoặc nguy cơ mất an toàn cho người, phương tiện tham gia giao thông đường bộ, trừ tàu bay không người lái, phương tiện bay siêu nhẹ được cấp phép bay.
> 
> 28. Hành vi khác vi phạm quy tắc giao thông đường bộ quy định tại Chương II của Luật này.
> 
> Chương II
> 
> QUY TẮC GIAO THÔNG ĐƯỜNG BỘ
> 
> Điều 10. Quy tắc chung
> 
> 1. Người tham gia giao thông đường bộ phải đi bên phải theo chiều đi của mình, đi đúng làn đường, phần đường quy định, chấp hành báo hiệu đường bộ và các quy tắc giao thông đường bộ khác.
> 
> 2. Người lái xe và người được chở trên xe ô tô phải thắt dây đai an toàn tại những chỗ có trang bị dây đai an toàn khi tham gia giao thông đường bộ.
> 
> 3. Khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 mét trên xe ô 

**Lý do AI:** Khoản 27 đủ ngoại lệ và khoản 28 đủ dẫn chiếu, nhưng thiếu tiêu đề nghiêm cấm và nội dung Chương II được dẫn chiếu.

- [x] Đã tự đọc mẫu B/P10; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P01 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 1](../../data/raw/36-2024-qh15-part1.pdf#page=1); vị trí mẫu 912; chunk `eb0ede421e043fa8a2b1b2dfaa34d7e2`.

Text giống hoàn toàn mẫu B/P01 ở trên.

**Lý do AI:** Giữ tiêu đề Điều 2 và trọn ba định nghĩa đầu, có đủ chủ thể và vị ngữ.

- [x] Đã tự đọc mẫu C/P01; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P02 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 2](../../data/raw/36-2024-qh15-part1.pdf#page=2); vị trí mẫu 1054; chunk `4aa34de6b07f5e77ebe7d0f187d27cda`.

Text giống hoàn toàn mẫu B/P02 ở trên.

**Lý do AI:** Ba định nghĩa ùn tắc, tai nạn và thiết bị an toàn đều trọn câu, tự hiểu được.

- [x] Đã tự đọc mẫu C/P02; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P03 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 3](../../data/raw/36-2024-qh15-part1.pdf#page=3); vị trí mẫu 1014; chunk `093711d60db1680f7d118fcaba05f15a`.

Text giống hoàn toàn mẫu B/P03 ở trên.

**Lý do AI:** Giữ trọn khoản 5-7 về phát hiện vi phạm, minh bạch và phối hợp quản lý.

- [x] Đã tự đọc mẫu C/P03; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P04 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 4](../../data/raw/36-2024-qh15-part1.pdf#page=4); vị trí mẫu 1229; chunk `d4b150ac8bfb9d67f60a95353ce8fbd1`.

Text giống hoàn toàn mẫu B/P04 ở trên.

**Lý do AI:** Khoản 5 giữ đủ đối tượng hỗ trợ, thành tích và các điều kiện bồi thường/chế độ.

- [x] Đã tự đọc mẫu C/P04; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P05 — đề xuất 2/2

Nguồn: [traffic-law-part1, PDF trang 5](../../data/raw/36-2024-qh15-part1.pdf#page=5); vị trí mẫu 1073; chunk `27947c86ed83a05960908b522ce947d4`.

Text giống hoàn toàn mẫu B/P05 ở trên.

**Lý do AI:** Khoản 5-7 giữ các chủ thể tuyên truyền, trách nhiệm gia đình và điều kiện chở trẻ.

- [x] Đã tự đọc mẫu C/P05; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P06 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 6](../../data/raw/36-2024-qh15-part1.pdf#page=6); vị trí mẫu 883; chunk `2861c372477031dbc6c3cad79bf66691`.

Text giống hoàn toàn mẫu B/P06 ở trên.

**Lý do AI:** Có Điều 7 và câu dẫn danh sách, nhưng chunk chỉ tới mục h, các mục i/k nằm chunk kế tiếp; chưa đủ toàn bộ danh mục.

- [x] Đã tự đọc mẫu C/P06; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P07 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 7](../../data/raw/36-2024-qh15-part1.pdf#page=7); vị trí mẫu 936; chunk `321f72fb15ca5a232068a5be8600247c`.

Text giống hoàn toàn mẫu B/P07 ở trên.

**Lý do AI:** Khoản 3 về cơ quan chủ trì đủ nội dung nhưng bắt đầu bằng mục e thiếu câu dẫn danh sách hợp tác quốc tế.

- [x] Đã tự đọc mẫu C/P07; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P08 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 8](../../data/raw/36-2024-qh15-part1.pdf#page=8); vị trí mẫu 1086; chunk `3f991c4b16e0392fac9de20e981d96bf`.

Text giống hoàn toàn mẫu B/P08 ở trên.

**Lý do AI:** Các khoản 8-11 trọn câu, nhưng thiếu tiêu đề Điều 9; người đọc không thấy rõ toàn bộ chúng là hành vi bị nghiêm cấm.

- [x] Đã tự đọc mẫu C/P08; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P09 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 9](../../data/raw/36-2024-qh15-part1.pdf#page=9); vị trí mẫu 1019; chunk `9308d00226440292caea4d1a017e64c6`.

Text giống hoàn toàn mẫu B/P09 ở trên.

**Lý do AI:** Các khoản 19-21 trọn câu nhưng thiếu tiêu đề xác định đây là các hành vi bị nghiêm cấm.

- [x] Đã tự đọc mẫu C/P09; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/P10 — đề xuất 1/2

Nguồn: [traffic-law-part1, PDF trang 10](../../data/raw/36-2024-qh15-part1.pdf#page=10); vị trí mẫu 1013; chunk `e0d6e6d7f23b212371d6ab55ee1f0b4e`.

Text giống hoàn toàn mẫu B/P10 ở trên.

**Lý do AI:** Khoản 27 đủ ngoại lệ và khoản 28 đủ dẫn chiếu, nhưng thiếu tiêu đề nghiêm cấm và nội dung Chương II được dẫn chiếu.

- [x] Đã tự đọc mẫu C/P10; đồng ý hoặc đã ghi nhãn/lý do khác.

## 2. Grounding — 15 câu/cấu hình với đủ top-3

### A/Q16 — đề xuất 1/2

**Câu hỏi:** Trên cao tốc, khi xe gặp sự cố và không thể vào làn dừng khẩn cấp, phải cảnh báo phía sau cách tối thiểu bao xa và cần làm gì?

**Đáp án cần bằng chứng:** Bật đèn khẩn cấp, đặt biển hoặc đèn cảnh báo sau xe ít nhất 150 mét và nhanh chóng báo Cảnh sát giao thông trên tuyến hoặc cơ quan quản lý cao tốc.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Rank 1:** [traffic-law-part2, trang 3, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=3); chunk `013207e2521f9de38321580edd648134`.

> chiều, các đường khác có thể đi được; riêng đối với đường cao tốc, chỉ được đi ngược chiều trên làn dừng xe khẩn cấp; phải tuân theo hiệu lệnh của người điều khiển giao thông, biển báo hiệu tạm thời.

**Rank 2:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `462bb7378193cfa190c0bfc29fc1a254`.

> cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.
> 
> 3. Xe máy chuyên dùng có tốc độ thiết kế nhỏ hơn tốc độ tối thiểu quy định đối với đường cao tốc, xe chở người bốn bánh có gắn động cơ, xe chở hàng bốn bánh có gắn động cơ, xe mô tô, xe gắn máy, các loại xe tương tự xe mô tô, xe gắn máy, xe thô sơ, người đi bộ không đ

**Rank 3:** [traffic-law-part2, trang 48, Chương VI](../../data/raw/36-2024-qh15-part2.pdf#page=48); chunk `7158164f2583235d8dccda3b18f9dc1a`.

> tình huống quy định tại khoản 1 Điều này kịp thời báo cho cơ quan Công an nơi gần nhất hoặc cơ quan quản lý đường bộ; trường hợp phát hiện vụ tai nạn giao thông đường bộ phải báo ngay cho

**Lý do AI:** Rank 2 có 150 mét và cơ quan cần báo nhưng mở đầu bằng cấp và đặt, mất điều kiện không thể vào làn khẩn cấp và phần bật đèn; rank 1 nói xe ưu tiên, rank 3 nói tình huống khác.

- [x] Đã tự đọc top-3 của A/Q16; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/Q17 — đề xuất 2/2

**Câu hỏi:** Khi đi trong hầm đường bộ, xe cơ giới, xe máy chuyên dùng và xe thô sơ phải sử dụng đèn thế nào?

**Đáp án cần bằng chứng:** Xe cơ giới, xe máy chuyên dùng bật đèn chiếu gần; xe thô sơ bật đèn hoặc có vật phát sáng báo hiệu.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Rank 1:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `8f2fbbf84eb8811bea87f3663e3c2e12`.

> mô tô, xe gắn máy, xe thô sơ, người đi bộ không được đi trên đường cao tốc, trừ người, phương tiện giao thông đường bộ và thiết bị phục vụ việc quản lý, bảo trì đường cao tốc.
> 
> Điều 26. Giao thông trong hầm đường bộ Người điều khiển phương tiện tham gia giao thông đường bộ khi điều khiển phương tiện trong hầm đường bộ phải tuân thủ quy tắc giao thông đường bộ sau đây:
> 
> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;
> 
> 2. Không dừng

**Rank 2:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `3ac85270d0ce885178c1091a6c62fc24`.

> đèn hoặc có vật phát sáng báo hiệu;
> 
> 2. Không dừng xe, đỗ xe trong hầm đường bộ; trường hợp gặp sự cố kỹ thuật hoặc bất khả kháng khác buộc phải dừng xe, đỗ xe, người lái xe, người điều khiển xe máy chuyên dùng phải đưa xe vào vị trí dừng xe, đỗ xe khẩn cấp, nếu không di chuyển được, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách bảo đảm an toàn, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trê

**Rank 3:** [traffic-law-part2, trang 5, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=5); chunk `c9551265c60b6b7880a1fbdbd8c1bef7`.

> b) Chỉ được qua đường ở những nơi có đèn tín hiệu, có vạch kẻ đường hoặc có cầu vượt, hầm dành cho người đi bộ và phải tuân thủ tín hiệu chỉ dẫn, báo hiệu đường bộ. Trường hợp không có đèn tín hiệu, vạch kẻ đường, cầu vượt, hầm dành cho người đi bộ thì phải quan sát các xe đang đi tới, chỉ qua đường khi bảo đảm an toàn, khi qua đường phải có tín hiệu bằng tay;
> 
> c) Không được vượt qua dải phân cách, đu, bám vào phương tiện giao thông đường bộ đang di chuyển; khi mang, vác vật cồng kềnh phải bảo đ

**Lý do AI:** Rank 1 có tiêu đề Điều 26 và trọn quy định đèn cho xe cơ giới, xe máy chuyên dùng, xe thô sơ; truy được phần 2 trang 2.

- [x] Đã tự đọc top-3 của A/Q17; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/Q18 — đề xuất 2/2

**Câu hỏi:** Trong Chương IV về người điều khiển phương tiện, thời gian lái xe ô tô kinh doanh vận tải và vận tải nội bộ tối đa mỗi ngày, mỗi tuần và liên tục là bao nhiêu?

**Đáp án cần bằng chứng:** Không quá 10 giờ/ngày, 48 giờ/tuần, liên tục không quá 04 giờ; bảo đảm quy định liên quan của Bộ luật Lao động.

**Gold:** [traffic-law-part2, PDF trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39).

**Evidence cần đủ:**

> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.

**Rank 1:** [traffic-law-part2, trang 39, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=39); chunk `12e297e437e92ff27b2d3e56146d6a53`.

> Điều 64. Thời gian làm việc của người lái xe ô tô kinh doanh vận tải và vận tải nội bộ
> 
> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.
> 
> 2. Đơn vị kinh doanh vận tải, đơn vị hoạt động vận tải nội bộ và người lái xe ô tô kinh doanh vận tải và vận tải nội bộ chịu trách nhiệm thực hiện các quy định tại Điều này.

**Rank 2:** [traffic-law-part2, trang 8, Chương III](../../data/raw/36-2024-qh15-part2.pdf#page=8); chunk `f1db5b28efa387d628c84467b1c3e517`.

> u kéo và có một phần đáng kể khối lượng toàn bộ đặt lên xe ô tô đầu kéo;
> 
> d) Xe chở người bốn bánh có gắn động cơ là xe có từ bốn bánh trở lên, chạy bằng động cơ, được thiết kế, sản xuất để hoạt động trên đường bộ, có kết cấu để chở người, vận tốc thiết kế không lớn hơn 30 km/h, số người cho phép chở tối đa 15 người (không kể người lái xe);
> 
> đ) Xe chở hàng bốn bánh có gắn động cơ là xe có từ bốn bánh trở lên, chạy bằng động cơ, được thiết kế, sản xuất để hoạt động trên đường bộ, có kết cấu để ch

**Rank 3:** [traffic-law-part2, trang 32, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=32); chunk `cb4a65a6bee1af066cf0e42d2f323b46`.

> 3. Người điều khiển xe chở hàng bốn bánh có gắn động cơ, xe chở người bốn bánh có gắn động cơ phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô tải hoặc xe ô tô chở người tương ứng.
> 
> 4. Người điều khiển xe ô tô có thiết kế, cải tạo với số chỗ ít hơn xe cùng loại, kích thước giới hạn tương đương phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô cùng loại, kích thước giới hạn tương đương và có số chỗ nhiều nhất.
> 
> 5. Thời hạn của giấy phép lái xe được quy định như sau:
> 
> a) Giấy phép

**Lý do AI:** Rank 1 giữ Điều 64, đủ 10 giờ/ngày, 48 giờ/tuần, 04 giờ liên tục và dẫn chiếu Bộ luật Lao động.

- [x] Đã tự đọc top-3 của A/Q18; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/Q19 — đề xuất 2/2

**Câu hỏi:** Trong Chương VII về giải quyết tai nạn, người gây tai nạn hoặc liên quan phải ở lại hiện trường đến khi nào, trường hợp nào được rời đi và phải trình báo ở đâu?

**Đáp án cần bằng chứng:** Ở lại đến khi Công an đến; được rời đi khi cấp cứu, đưa nạn nhân cấp cứu hoặc bị đe dọa tính mạng, sức khỏe, nhưng phải trình báo ngay Công an hoặc UBND gần nhất.

**Gold:** [traffic-law-part2, PDF trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51).

**Evidence cần đủ:**

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;

**Rank 1:** [traffic-law-part2, trang 52, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=52); chunk `fa5ab8279b2f09ce8185d11c2a9d32e4`.

> 3. Người được quy định tại khoản 1 và khoản 2 Điều này chỉ được sử dụng phương tiện liên quan đến vụ tai nạn giao thông đường bộ để đưa nạn nhân đi cấp cứu trong trường hợp không có phương tiện nào khác nhưng phải xác định vị trí phương tiện, vị trí nạn nhân tại hiện trường, không được làm thay đổi, mất dấu vết liên quan đến vụ tai nạn giao thông đường bộ. Trường hợp có người chết phải giữ nguyên hiện trường và che đậy thi thể.
> 
> 4. Người điều khiển phương tiện tham gia giao thông đường bộ khác k

**Rank 2:** [traffic-law-part2, trang 53, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=53); chunk `bea399bbaf97291a2201a66eeec8af38`.

> Điều 82. Cứu nạn, cứu hộ khi xảy ra vụ tai nạn giao thông đường bộ
> 
> 1. Cơ quan Công an chủ trì, phối hợp với các cơ quan, tổ chức, cá nhân có liên quan tổ chức lực lượng và công cụ, phương tiện nhanh chóng có mặt tại hiện trường để cứu nạn, cứu hộ. Căn cứ vào tính chất, mức độ, hậu quả vụ tai nạn giao thông đường bộ, cơ quan Công an có trách nhiệm báo cáo cơ quan có thẩm quyền để huy động lực lượng, phương tiện giải quyết vụ tai nạn giao thông đường bộ trong trường hợp cần thiết.
> 
> 2. Cơ sở khám

**Rank 3:** [traffic-law-part2, trang 51, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=51); chunk `b6dac0e5a7d263899494d2df30412175`.

> cảnh báo nguy hiểm, giữ nguyên hiện trường, trợ giúp người bị nạn và báo tin cho cơ quan Công an, cơ sở khám bệnh, chữa bệnh hoặc Ủy ban nhân dân nơi gần nhất;
> 
> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;
> 
> c) Cung cấp thông tin xác định danh tính về bản thân, ngườ

**Lý do AI:** Rank 3 giữ trọn điểm b: ở lại đến khi Công an tới, đủ ba ngoại lệ và nơi trình báo; nguồn phần 2 trang 51.

- [x] Đã tự đọc top-3 của A/Q19; đồng ý hoặc đã ghi nhãn/lý do khác.

### A/Q20 — đề xuất 2/2

**Câu hỏi:** Theo Chương IX về điều khoản thi hành, giấy phép lái xe cấp trước ngày luật này có hiệu lực có tiếp tục dùng được không và theo thời hạn nào?

**Đáp án cần bằng chứng:** Được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Gold:** [traffic-law-part2, PDF trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58).

**Evidence cần đủ:**

> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Rank 1:** [traffic-law-part2, trang 58, Chương IX](../../data/raw/36-2024-qh15-part2.pdf#page=58); chunk `6b48c2d05e64fc36605e0c1fe0d1f641`.

> hợp quy định tại các khoản 1, 2, 5 và 6 Điều 89 của Luật này.
> 
> 4. Nghị quyết số 73/2022/QH15 của Quốc hội về thí điểm đấu giá biển số xe ô tô hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ trường hợp quy định tại khoản 7 Điều 89 của Luật này.
> 
> Điều 89. Quy định chuyển tiếp
> 
> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.
> 
> 2. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành nếu chưa

**Rank 2:** [traffic-law-part2, trang 37, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=37); chunk `c29d87a9939ff6c974eb73ca52336fdf`.

> lái xe không thời hạn được cấp trước ngày 01 tháng 7 năm 2012 sang giấy phép lái xe theo quy định của Luật này.
> 
> 4. Chưa cấp, đổi, cấp lại giấy phép lái xe đối với người vi phạm pháp luật về trật tự, an toàn giao thông đường bộ khi người đó chưa thực hiện xong yêu cầu của cơ quan nhà nước có thẩm quyền về giải quyết vụ việc vi phạm hành chính trong lĩnh vực trật tự, an toàn giao thông đường bộ.
> 
> 5. Giấy phép lái xe bị thu hồi khi thuộc một trong các trường hợp sau đây:
> 
> a) Người được cấp giấy ph

**Rank 3:** [traffic-law-part2, trang 60, Chương IX](../../data/raw/36-2024-qh15-part2.pdf#page=60); chunk `16abbdbf87f8a110a37da2bd4e4fe743`.

> 3. Trường hợp người có giấy phép lái xe đã được cấp trước ngày Luật này có hiệu lực thi hành có nhu cầu đổi, cấp lại giấy phép lái xe thì thực hiện như sau:
> 
> a) Giấy phép lái xe hạng A1 được đổi, cấp lại sang giấy phép lái xe hạng A với điều kiện hạn chế là chỉ được điều khiển xe mô tô hai bánh có dung tích xi-lanh đến dưới 175 cm3 hoặc có công suất động cơ điện đến dưới 14 kW;
> 
> b) Giấy phép lái xe hạng A2 được đổi, cấp lại sang giấy phép lái xe hạng A;
> 
> c) Giấy phép lái xe hạng A3 được đổi, cấp

**Lý do AI:** Rank 1 có Điều 89 và khoản 1 đủ quy định giấy phép cũ tiếp tục dùng theo thời hạn trên giấy phép.

- [x] Đã tự đọc top-3 của A/Q20; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/Q16 — đề xuất 2/2

**Câu hỏi:** Trên cao tốc, khi xe gặp sự cố và không thể vào làn dừng khẩn cấp, phải cảnh báo phía sau cách tối thiểu bao xa và cần làm gì?

**Đáp án cần bằng chứng:** Bật đèn khẩn cấp, đặt biển hoặc đèn cảnh báo sau xe ít nhất 150 mét và nhanh chóng báo Cảnh sát giao thông trên tuyến hoặc cơ quan quản lý cao tốc.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Rank 1:** [traffic-law-part2, trang 1, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=1); chunk `c44d2f80f20c09981ec3c6be0ee130ee`.

> b) Khi chuẩn bị ra khỏi đường cao tốc phải quan sát biển báo hiệu chỉ dẫn, thực hiện chuyển dần sang làn đường sát bên phải, nếu có làn đường giảm tốc thì phải cho xe di chuyển trên làn đường đó trước khi ra khỏi đường cao tốc; Người ký: CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ Email: thongtinchinhphu@chinhphu.vn Cơ quan: VĂN PHÒNG CHÍNH PHỦ Thời gian ký: 28.08.2024 14:38:08 +07:00

**Rank 2:** [traffic-law-part2, trang 3, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=3); chunk `286f5d6914f4b50897aefcb09914216b`.

> c) Xe hộ đê đi làm nhiệm vụ; xe đi làm nhiệm vụ cứu nạn, cứu hộ, khắc phục sự cố thiên tai, dịch bệnh hoặc xe đi làm nhiệm vụ trong tình trạng khẩn cấp theo quy định của pháp luật có đèn nhấp nháy màu xanh.
> 
> 4. Xe ưu tiên quy định tại các điểm a, b, c và d khoản 2 Điều này không bị hạn chế tốc độ; được phép đi không phụ thuộc vào tín hiệu đèn giao thông, đi vào đường ngược chiều, các đường khác có thể đi được; riêng đối với đường cao tốc, chỉ được đi ngược chiều trên làn dừng xe khẩn cấp; phải tuân theo hiệu lệnh của người điều khiển giao thông, biển báo hiệu tạm thời.

**Rank 3:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `00a193da631c3af3ccd923828a0fbc07`.

> c) Không được cho xe chạy ở làn dừng xe khẩn cấp và phần lề đường;
> 
> d) Các quy tắc giao thông đường bộ khác quy định tại Chương này.
> 
> 2. Chỉ được dừng xe, đỗ xe ở nơi quy định; trường hợp gặp sự cố kỹ thuật hoặc bất khả kháng khác buộc phải dừng xe, đỗ xe thì được dừng xe, đỗ xe ở làn dừng khẩn cấp cùng chiều xe chạy và phải có báo hiệu bằng đèn khẩn cấp; trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Lý do AI:** Rank 3 giữ trọn khoản 2 về cao tốc, gồm điều kiện xe không thể vào làn khẩn cấp, bật đèn, khoảng cách 150 mét và cơ quan cần báo.

- [x] Đã tự đọc top-3 của B/Q16; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/Q17 — đề xuất 2/2

**Câu hỏi:** Khi đi trong hầm đường bộ, xe cơ giới, xe máy chuyên dùng và xe thô sơ phải sử dụng đèn thế nào?

**Đáp án cần bằng chứng:** Xe cơ giới, xe máy chuyên dùng bật đèn chiếu gần; xe thô sơ bật đèn hoặc có vật phát sáng báo hiệu.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Rank 1:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `11b3860c76e14dfbc6f5aba8d8144e79`.

> Điều 26. Giao thông trong hầm đường bộ Người điều khiển phương tiện tham gia giao thông đường bộ khi điều khiển phương tiện trong hầm đường bộ phải tuân thủ quy tắc giao thông đường bộ sau đây:
> 
> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Rank 2:** [traffic-law-part1, trang 19, Chương II](../../data/raw/36-2024-qh15-part1.pdf#page=19); chunk `566650d8f23fa05078cbbd7a33b8ccd9`.

> 2. Người lái xe, người điều khiển xe máy chuyên dùng phải tắt đèn chiếu xa, bật đèn chiếu gần trong các trường hợp sau đây:
> 
> a) Khi gặp người đi bộ qua đường;
> 
> b) Khi đi trên các đoạn đường qua khu đông dân cư có hệ thống chiếu sáng đang hoạt động;
> 
> c) Khi gặp xe đi ngược chiều, trừ trường hợp dải phân cách có khả năng chống chói;
> 
> d) Khi chuyển hướng xe tại nơi đường giao nhau.
> 
> 3. Người lái xe, người điều khiển xe máy chuyên dùng khi thực hiện công việc trên đường bộ phải bật sáng đèn cảnh báo màu vàng.

**Rank 3:** [traffic-law-part2, trang 23, Chương III](../../data/raw/36-2024-qh15-part2.pdf#page=23); chunk `b3dce73a4e5df08893a218429b8abb96`.

> đ) Khi vận chuyển hàng rời, vật liệu xây dựng, phế thải phải che đậy kín, không để rơi vãi xuống đường, gây ra tiếng ồn hoặc bụi bẩn trong suốt quá trình vận chuyển trên đường và chiều cao tối đa của hàng hóa phải thấp hơn mép trên thành thùng xe tối thiểu 10 cm;
> 
> e) Khi vận chuyển hàng hóa xếp vượt phía trước và phía sau xe thì ban ngày phải có báo hiệu màu đỏ tại điểm đầu và điểm cuối cùng của hàng hóa, ban đêm hoặc khi trời tối phải có đèn hoặc báo hiệu cho người tham gia giao thông đường bộ để nhận biết.
> 
> 2. Lực lượng Cảnh sát giao thông chịu trách nhiệm tổ chức tuần tra, kiểm soát, xử lý vi phạm pháp luật về trật tự, an toàn giao thông đường bộ đối với xe ô tô vận chuyển hàng hóa quá tải lưu hành trên đường bộ.

**Lý do AI:** Rank 1 có tiêu đề hầm đường bộ và đủ loại đèn cho cả ba loại phương tiện.

- [x] Đã tự đọc top-3 của B/Q17; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/Q18 — đề xuất 2/2

**Câu hỏi:** Trong Chương IV về người điều khiển phương tiện, thời gian lái xe ô tô kinh doanh vận tải và vận tải nội bộ tối đa mỗi ngày, mỗi tuần và liên tục là bao nhiêu?

**Đáp án cần bằng chứng:** Không quá 10 giờ/ngày, 48 giờ/tuần, liên tục không quá 04 giờ; bảo đảm quy định liên quan của Bộ luật Lao động.

**Gold:** [traffic-law-part2, PDF trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39).

**Evidence cần đủ:**

> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.

**Rank 1:** [traffic-law-part2, trang 39, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=39); chunk `e875f57b6a639b8c5653b2442959ff2a`.

> Điều 64. Thời gian làm việc của người lái xe ô tô kinh doanh vận tải và vận tải nội bộ
> 
> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.
> 
> 2. Đơn vị kinh doanh vận tải, đơn vị hoạt động vận tải nội bộ và người lái xe ô tô kinh doanh vận tải và vận tải nội bộ chịu trách nhiệm thực hiện các quy định tại Điều này.

**Rank 2:** [traffic-law-part2, trang 32, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=32); chunk `79db098ca401ed390c3fdfc7a27daa1e`.

> 3. Người điều khiển xe chở hàng bốn bánh có gắn động cơ, xe chở người bốn bánh có gắn động cơ phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô tải hoặc xe ô tô chở người tương ứng.
> 
> 4. Người điều khiển xe ô tô có thiết kế, cải tạo với số chỗ ít hơn xe cùng loại, kích thước giới hạn tương đương phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô cùng loại, kích thước giới hạn tương đương và có số chỗ nhiều nhất.
> 
> 5. Thời hạn của giấy phép lái xe được quy định như sau:
> 
> a) Giấy phép lái xe các hạng A1, A, B1 không thời hạn;
> 
> b) Giấy phép lái xe hạng B và hạng C1 có thời hạn 10 năm kể từ ngày cấp;
> 
> c) Giấy phép lái xe các hạng C, D1, D2, D, BE, C1E, CE, D1E, D2E và DE có thời hạn 05 năm kể từ ngày cấp.

**Rank 3:** [traffic-law-part2, trang 6, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=6); chunk `e67e071b9777caa45084e92590edf779`.

> 4. Người điều khiển xe thô sơ chỉ được cho xe đi hàng một, nơi có phần đường dành cho xe thô sơ thì phải đi đúng phần đường quy định; khi tham gia giao thông đường bộ trong thời gian từ 18 giờ ngày hôm trước đến 06 giờ ngày hôm sau phải sử dụng đèn hoặc có báo hiệu ở phía trước và phía sau xe.
> 
> 5. Hàng hóa xếp trên xe thô sơ phải bảo đảm an toàn, không gây cản trở giao thông và che khuất tầm nhìn của người điều khiển. Hàng hóa xếp trên xe không vượt quá 1/3 chiều dài thân xe và không vượt quá 01 mét phía trước và phía sau xe; không vượt quá 0,4 mét mỗi bên bánh xe.

**Lý do AI:** Rank 1 giữ trọn Điều 64, đủ các giới hạn ngày/tuần/liên tục và điều kiện lao động.

- [x] Đã tự đọc top-3 của B/Q18; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/Q19 — đề xuất 2/2

**Câu hỏi:** Trong Chương VII về giải quyết tai nạn, người gây tai nạn hoặc liên quan phải ở lại hiện trường đến khi nào, trường hợp nào được rời đi và phải trình báo ở đâu?

**Đáp án cần bằng chứng:** Ở lại đến khi Công an đến; được rời đi khi cấp cứu, đưa nạn nhân cấp cứu hoặc bị đe dọa tính mạng, sức khỏe, nhưng phải trình báo ngay Công an hoặc UBND gần nhất.

**Gold:** [traffic-law-part2, PDF trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51).

**Evidence cần đủ:**

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;

**Rank 1:** [traffic-law-part2, trang 51, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=51); chunk `9d5a2bea276301002af756e5e8d95871`.

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;
> 
> c) Cung cấp thông tin xác định danh tính về bản thân, người liên quan đến vụ tai nạn giao thông đường bộ và thông tin liên quan của vụ tai nạn giao thông đường bộ cho cơ quan có thẩm quyền.
> 
> 2. Người có mặt tại nơi xảy ra vụ tai nạn giao thông đường bộ có trách nhiệm sau đây:
> 
> a) Giúp đỡ, cứu chữa kịp thời người bị nạn;
> 
> b) Báo tin ngay cho cơ quan Công an, cơ sở khám bệnh, chữa bệnh hoặc Ủy ban nhân dân nơi gần nhất;
> 
> c) Tham gia bảo vệ hiện trường;
> 
> d) Tham gia bảo vệ tài sản của người bị nạn;

**Rank 2:** [traffic-law-part2, trang 53, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=53); chunk `59c2092fedc99d225d6589346e08b3f5`.

> Điều 82. Cứu nạn, cứu hộ khi xảy ra vụ tai nạn giao thông đường bộ
> 
> 1. Cơ quan Công an chủ trì, phối hợp với các cơ quan, tổ chức, cá nhân có liên quan tổ chức lực lượng và công cụ, phương tiện nhanh chóng có mặt tại hiện trường để cứu nạn, cứu hộ. Căn cứ vào tính chất, mức độ, hậu quả vụ tai nạn giao thông đường bộ, cơ quan Công an có trách nhiệm báo cáo cơ quan có thẩm quyền để huy động lực lượng, phương tiện giải quyết vụ tai nạn giao thông đường bộ trong trường hợp cần thiết.
> 
> 2. Cơ sở khám bệnh, chữa bệnh phải bố trí, phân công người, phương tiện sẵn sàng và nhanh chóng có mặt tại hiện trường để sơ cứu, vận chuyển, cấp cứu nạn nhân sau khi tiếp nhận tin báo vụ tai nạn giao thông đường bộ; hỗ trợ, cứu chữa nạn nhân bị tai nạn giao thông đường bộ trong mọi trường hợp.

**Rank 3:** [traffic-law-part2, trang 52, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=52); chunk `bc6aef49015f2fd134d26385eb3a10f4`.

> 3. Người được quy định tại khoản 1 và khoản 2 Điều này chỉ được sử dụng phương tiện liên quan đến vụ tai nạn giao thông đường bộ để đưa nạn nhân đi cấp cứu trong trường hợp không có phương tiện nào khác nhưng phải xác định vị trí phương tiện, vị trí nạn nhân tại hiện trường, không được làm thay đổi, mất dấu vết liên quan đến vụ tai nạn giao thông đường bộ. Trường hợp có người chết phải giữ nguyên hiện trường và che đậy thi thể.
> 
> 4. Người điều khiển phương tiện tham gia giao thông đường bộ khác khi đi qua nơi xảy ra vụ tai nạn giao thông đường bộ có trách nhiệm chở người bị thương đi cấp cứu. Xe ưu tiên, xe chở người được hưởng quyền ưu đãi, miễn trừ ngoại giao không bắt buộc thực hiện quy định tại khoản này.

**Lý do AI:** Rank 1 giữ trọn ngoại lệ rời hiện trường và nghĩa vụ trình báo, có nguồn trang 51.

- [x] Đã tự đọc top-3 của B/Q19; đồng ý hoặc đã ghi nhãn/lý do khác.

### B/Q20 — đề xuất 0/2

**Câu hỏi:** Theo Chương IX về điều khoản thi hành, giấy phép lái xe cấp trước ngày luật này có hiệu lực có tiếp tục dùng được không và theo thời hạn nào?

**Đáp án cần bằng chứng:** Được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Gold:** [traffic-law-part2, PDF trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58).

**Evidence cần đủ:**

> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Rank 1:** [traffic-law-part2, trang 33, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=33); chunk `b2d237ee5c7cb57a588b162c722e30c0`.

> 3. Trường hợp giấy phép lái xe bị trừ hết điểm thì người có giấy phép lái xe không được điều khiển phương tiện tham gia giao thông đường bộ theo giấy phép lái xe đó. Sau thời hạn ít nhất là 06 tháng kể từ ngày bị trừ hết điểm, người có giấy

**Rank 2:** [traffic-law-part2, trang 32, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=32); chunk `525fad8ea2120df3de83d7f979fcb89c`.

> 7. Giấy phép lái xe không có hiệu lực trong các trường hợp sau đây:
> 
> a) Giấy phép lái xe hết thời hạn sử dụng;
> 
> b) Giấy phép lái xe bị thu hồi theo quy định tại khoản 5 Điều 62 của Luật này.
> 
> 8. Giấy phép lái xe quốc tế được quy định như sau:
> 
> a) Giấy phép lái xe quốc tế là giấy phép lái xe do cơ quan nhà nước có thẩm quyền của quốc gia là thành viên của Công ước Viên cấp theo một mẫu thống nhất; có thời hạn không quá 03 năm kể từ ngày cấp và phải phù hợp với thời hạn còn hiệu lực của giấy phép lái xe quốc gia;

**Rank 3:** [traffic-law-part2, trang 37, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=37); chunk `94097cfffb7b0aefff9551b0b3cf39b9`.

> Điều 62. Cấp, đổi, cấp lại và thu hồi giấy phép lái xe
> 
> 1. Giấy phép lái xe được cấp cho người tham dự kỳ sát hạch lái xe có kết quả đạt yêu cầu.
> 
> 2. Người có giấy phép lái xe được đổi, cấp lại giấy phép lái xe trong các trường hợp sau đây:
> 
> a) Giấy phép lái xe bị mất;
> 
> b) Giấy phép lái xe bị hỏng không còn sử dụng được;
> 
> c) Trước thời hạn ghi trên giấy phép lái xe;
> 
> d) Thay đổi thông tin ghi trên giấy phép lái xe;
> 
> đ) Giấy phép lái xe nước ngoài do cơ quan có thẩm quyền của nước ngoài cấp còn giá trị sử dụng;
> 
> e) Giấy phép lái xe do Bộ Quốc phòng, Bộ Công an cấp khi có yêu cầu hoặc người được cấp không còn làm nhiệm vụ quốc phòng, an ninh.
> 
> 3. Khuyến khích đổi giấy phép lái xe không thời hạn được cấp trước ngày 01 tháng 7 năm 2012 sang giấy phép lái xe theo quy định của Luật này.

**Lý do AI:** Cả ba rank thuộc Chương IV: hết điểm, giấy phép quốc tế/hết hạn, cấp đổi. Không có quy định chuyển tiếp tại Điều 89 cho giấy phép cũ.

- [x] Đã tự đọc top-3 của B/Q20; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/Q16 — đề xuất 2/2

**Câu hỏi:** Trên cao tốc, khi xe gặp sự cố và không thể vào làn dừng khẩn cấp, phải cảnh báo phía sau cách tối thiểu bao xa và cần làm gì?

**Đáp án cần bằng chứng:** Bật đèn khẩn cấp, đặt biển hoặc đèn cảnh báo sau xe ít nhất 150 mét và nhanh chóng báo Cảnh sát giao thông trên tuyến hoặc cơ quan quản lý cao tốc.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Rank 1:** [traffic-law-part2, trang 1, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=1); chunk `c44d2f80f20c09981ec3c6be0ee130ee`.

> b) Khi chuẩn bị ra khỏi đường cao tốc phải quan sát biển báo hiệu chỉ dẫn, thực hiện chuyển dần sang làn đường sát bên phải, nếu có làn đường giảm tốc thì phải cho xe di chuyển trên làn đường đó trước khi ra khỏi đường cao tốc; Người ký: CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ Email: thongtinchinhphu@chinhphu.vn Cơ quan: VĂN PHÒNG CHÍNH PHỦ Thời gian ký: 28.08.2024 14:38:08 +07:00

**Rank 2:** [traffic-law-part2, trang 3, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=3); chunk `286f5d6914f4b50897aefcb09914216b`.

> c) Xe hộ đê đi làm nhiệm vụ; xe đi làm nhiệm vụ cứu nạn, cứu hộ, khắc phục sự cố thiên tai, dịch bệnh hoặc xe đi làm nhiệm vụ trong tình trạng khẩn cấp theo quy định của pháp luật có đèn nhấp nháy màu xanh.
> 
> 4. Xe ưu tiên quy định tại các điểm a, b, c và d khoản 2 Điều này không bị hạn chế tốc độ; được phép đi không phụ thuộc vào tín hiệu đèn giao thông, đi vào đường ngược chiều, các đường khác có thể đi được; riêng đối với đường cao tốc, chỉ được đi ngược chiều trên làn dừng xe khẩn cấp; phải tuân theo hiệu lệnh của người điều khiển giao thông, biển báo hiệu tạm thời.

**Rank 3:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `00a193da631c3af3ccd923828a0fbc07`.

> c) Không được cho xe chạy ở làn dừng xe khẩn cấp và phần lề đường;
> 
> d) Các quy tắc giao thông đường bộ khác quy định tại Chương này.
> 
> 2. Chỉ được dừng xe, đỗ xe ở nơi quy định; trường hợp gặp sự cố kỹ thuật hoặc bất khả kháng khác buộc phải dừng xe, đỗ xe thì được dừng xe, đỗ xe ở làn dừng khẩn cấp cùng chiều xe chạy và phải có báo hiệu bằng đèn khẩn cấp; trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Lý do AI:** Câu không filter; cùng B: rank 3 giữ đủ điều kiện sự cố, cảnh báo 150 mét, đèn khẩn cấp và báo cơ quan quản lý.

- [x] Đã tự đọc top-3 của C/Q16; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/Q17 — đề xuất 2/2

**Câu hỏi:** Khi đi trong hầm đường bộ, xe cơ giới, xe máy chuyên dùng và xe thô sơ phải sử dụng đèn thế nào?

**Đáp án cần bằng chứng:** Xe cơ giới, xe máy chuyên dùng bật đèn chiếu gần; xe thô sơ bật đèn hoặc có vật phát sáng báo hiệu.

**Gold:** [traffic-law-part2, PDF trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Evidence cần đủ:**

> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Rank 1:** [traffic-law-part2, trang 2, Chương II](../../data/raw/36-2024-qh15-part2.pdf#page=2); chunk `11b3860c76e14dfbc6f5aba8d8144e79`.

> Điều 26. Giao thông trong hầm đường bộ Người điều khiển phương tiện tham gia giao thông đường bộ khi điều khiển phương tiện trong hầm đường bộ phải tuân thủ quy tắc giao thông đường bộ sau đây:
> 
> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Rank 2:** [traffic-law-part1, trang 19, Chương II](../../data/raw/36-2024-qh15-part1.pdf#page=19); chunk `566650d8f23fa05078cbbd7a33b8ccd9`.

> 2. Người lái xe, người điều khiển xe máy chuyên dùng phải tắt đèn chiếu xa, bật đèn chiếu gần trong các trường hợp sau đây:
> 
> a) Khi gặp người đi bộ qua đường;
> 
> b) Khi đi trên các đoạn đường qua khu đông dân cư có hệ thống chiếu sáng đang hoạt động;
> 
> c) Khi gặp xe đi ngược chiều, trừ trường hợp dải phân cách có khả năng chống chói;
> 
> d) Khi chuyển hướng xe tại nơi đường giao nhau.
> 
> 3. Người lái xe, người điều khiển xe máy chuyên dùng khi thực hiện công việc trên đường bộ phải bật sáng đèn cảnh báo màu vàng.

**Rank 3:** [traffic-law-part2, trang 23, Chương III](../../data/raw/36-2024-qh15-part2.pdf#page=23); chunk `b3dce73a4e5df08893a218429b8abb96`.

> đ) Khi vận chuyển hàng rời, vật liệu xây dựng, phế thải phải che đậy kín, không để rơi vãi xuống đường, gây ra tiếng ồn hoặc bụi bẩn trong suốt quá trình vận chuyển trên đường và chiều cao tối đa của hàng hóa phải thấp hơn mép trên thành thùng xe tối thiểu 10 cm;
> 
> e) Khi vận chuyển hàng hóa xếp vượt phía trước và phía sau xe thì ban ngày phải có báo hiệu màu đỏ tại điểm đầu và điểm cuối cùng của hàng hóa, ban đêm hoặc khi trời tối phải có đèn hoặc báo hiệu cho người tham gia giao thông đường bộ để nhận biết.
> 
> 2. Lực lượng Cảnh sát giao thông chịu trách nhiệm tổ chức tuần tra, kiểm soát, xử lý vi phạm pháp luật về trật tự, an toàn giao thông đường bộ đối với xe ô tô vận chuyển hàng hóa quá tải lưu hành trên đường bộ.

**Lý do AI:** Câu không filter; cùng B: rank 1 giữ đủ quy tắc đèn trong hầm cho các loại xe.

- [x] Đã tự đọc top-3 của C/Q17; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/Q18 — đề xuất 2/2

**Câu hỏi:** Trong Chương IV về người điều khiển phương tiện, thời gian lái xe ô tô kinh doanh vận tải và vận tải nội bộ tối đa mỗi ngày, mỗi tuần và liên tục là bao nhiêu?

**Đáp án cần bằng chứng:** Không quá 10 giờ/ngày, 48 giờ/tuần, liên tục không quá 04 giờ; bảo đảm quy định liên quan của Bộ luật Lao động.

**Gold:** [traffic-law-part2, PDF trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39).

**Evidence cần đủ:**

> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.

**Rank 1:** [traffic-law-part2, trang 39, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=39); chunk `e875f57b6a639b8c5653b2442959ff2a`.

> Điều 64. Thời gian làm việc của người lái xe ô tô kinh doanh vận tải và vận tải nội bộ
> 
> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.
> 
> 2. Đơn vị kinh doanh vận tải, đơn vị hoạt động vận tải nội bộ và người lái xe ô tô kinh doanh vận tải và vận tải nội bộ chịu trách nhiệm thực hiện các quy định tại Điều này.

**Rank 2:** [traffic-law-part2, trang 32, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=32); chunk `79db098ca401ed390c3fdfc7a27daa1e`.

> 3. Người điều khiển xe chở hàng bốn bánh có gắn động cơ, xe chở người bốn bánh có gắn động cơ phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô tải hoặc xe ô tô chở người tương ứng.
> 
> 4. Người điều khiển xe ô tô có thiết kế, cải tạo với số chỗ ít hơn xe cùng loại, kích thước giới hạn tương đương phải sử dụng giấy phép lái xe có hạng phù hợp với xe ô tô cùng loại, kích thước giới hạn tương đương và có số chỗ nhiều nhất.
> 
> 5. Thời hạn của giấy phép lái xe được quy định như sau:
> 
> a) Giấy phép lái xe các hạng A1, A, B1 không thời hạn;
> 
> b) Giấy phép lái xe hạng B và hạng C1 có thời hạn 10 năm kể từ ngày cấp;
> 
> c) Giấy phép lái xe các hạng C, D1, D2, D, BE, C1E, CE, D1E, D2E và DE có thời hạn 05 năm kể từ ngày cấp.

**Rank 3:** [traffic-law-part2, trang 30, Chương IV](../../data/raw/36-2024-qh15-part2.pdf#page=30); chunk `d1bcf2fe6ee19da8e38b8710101fc0d9`.

> Điều 57. Giấy phép lái xe
> 
> 1. Giấy phép lái xe bao gồm các hạng sau đây:
> 
> a) Hạng A1 cấp cho người lái xe mô tô hai bánh có dung tích xi-lanh đến 125 cm3 hoặc có công suất động cơ điện đến 11 kW;
> 
> b) Hạng A cấp cho người lái xe mô tô hai bánh có dung tích xi-lanh trên 125 cm3 hoặc có công suất động cơ điện trên 11 kW và các loại xe quy định cho giấy phép lái xe hạng A1;
> 
> c) Hạng B1 cấp cho người lái xe mô tô ba bánh và các loại xe quy định cho giấy phép lái xe hạng A1;
> 
> d) Hạng B cấp cho người lái xe ô tô chở người đến 08 chỗ (không kể chỗ của người lái xe); xe ô tô tải và ô tô chuyên dùng có khối lượng toàn bộ theo thiết kế đến 3.500 kg; các loại xe ô tô quy định cho giấy phép lái xe hạng B kéo rơ moóc có khối lượng toàn bộ theo thiết kế đến 750 kg;

**Lý do AI:** Rank 1 giữ Điều 64 đủ mọi giới hạn; ba kết quả đều trong Chương IV theo phạm vi đầu vào.

- [x] Đã tự đọc top-3 của C/Q18; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/Q19 — đề xuất 2/2

**Câu hỏi:** Trong Chương VII về giải quyết tai nạn, người gây tai nạn hoặc liên quan phải ở lại hiện trường đến khi nào, trường hợp nào được rời đi và phải trình báo ở đâu?

**Đáp án cần bằng chứng:** Ở lại đến khi Công an đến; được rời đi khi cấp cứu, đưa nạn nhân cấp cứu hoặc bị đe dọa tính mạng, sức khỏe, nhưng phải trình báo ngay Công an hoặc UBND gần nhất.

**Gold:** [traffic-law-part2, PDF trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51).

**Evidence cần đủ:**

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;

**Rank 1:** [traffic-law-part2, trang 51, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=51); chunk `9d5a2bea276301002af756e5e8d95871`.

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;
> 
> c) Cung cấp thông tin xác định danh tính về bản thân, người liên quan đến vụ tai nạn giao thông đường bộ và thông tin liên quan của vụ tai nạn giao thông đường bộ cho cơ quan có thẩm quyền.
> 
> 2. Người có mặt tại nơi xảy ra vụ tai nạn giao thông đường bộ có trách nhiệm sau đây:
> 
> a) Giúp đỡ, cứu chữa kịp thời người bị nạn;
> 
> b) Báo tin ngay cho cơ quan Công an, cơ sở khám bệnh, chữa bệnh hoặc Ủy ban nhân dân nơi gần nhất;
> 
> c) Tham gia bảo vệ hiện trường;
> 
> d) Tham gia bảo vệ tài sản của người bị nạn;

**Rank 2:** [traffic-law-part2, trang 53, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=53); chunk `59c2092fedc99d225d6589346e08b3f5`.

> Điều 82. Cứu nạn, cứu hộ khi xảy ra vụ tai nạn giao thông đường bộ
> 
> 1. Cơ quan Công an chủ trì, phối hợp với các cơ quan, tổ chức, cá nhân có liên quan tổ chức lực lượng và công cụ, phương tiện nhanh chóng có mặt tại hiện trường để cứu nạn, cứu hộ. Căn cứ vào tính chất, mức độ, hậu quả vụ tai nạn giao thông đường bộ, cơ quan Công an có trách nhiệm báo cáo cơ quan có thẩm quyền để huy động lực lượng, phương tiện giải quyết vụ tai nạn giao thông đường bộ trong trường hợp cần thiết.
> 
> 2. Cơ sở khám bệnh, chữa bệnh phải bố trí, phân công người, phương tiện sẵn sàng và nhanh chóng có mặt tại hiện trường để sơ cứu, vận chuyển, cấp cứu nạn nhân sau khi tiếp nhận tin báo vụ tai nạn giao thông đường bộ; hỗ trợ, cứu chữa nạn nhân bị tai nạn giao thông đường bộ trong mọi trường hợp.

**Rank 3:** [traffic-law-part2, trang 52, Chương VII](../../data/raw/36-2024-qh15-part2.pdf#page=52); chunk `bc6aef49015f2fd134d26385eb3a10f4`.

> 3. Người được quy định tại khoản 1 và khoản 2 Điều này chỉ được sử dụng phương tiện liên quan đến vụ tai nạn giao thông đường bộ để đưa nạn nhân đi cấp cứu trong trường hợp không có phương tiện nào khác nhưng phải xác định vị trí phương tiện, vị trí nạn nhân tại hiện trường, không được làm thay đổi, mất dấu vết liên quan đến vụ tai nạn giao thông đường bộ. Trường hợp có người chết phải giữ nguyên hiện trường và che đậy thi thể.
> 
> 4. Người điều khiển phương tiện tham gia giao thông đường bộ khác khi đi qua nơi xảy ra vụ tai nạn giao thông đường bộ có trách nhiệm chở người bị thương đi cấp cứu. Xe ưu tiên, xe chở người được hưởng quyền ưu đãi, miễn trừ ngoại giao không bắt buộc thực hiện quy định tại khoản này.

**Lý do AI:** Rank 1 giữ đủ điểm b về ở lại, ngoại lệ và nơi trình báo; ba kết quả đều thuộc Chương VII.

- [x] Đã tự đọc top-3 của C/Q19; đồng ý hoặc đã ghi nhãn/lý do khác.

### C/Q20 — đề xuất 2/2

**Câu hỏi:** Theo Chương IX về điều khoản thi hành, giấy phép lái xe cấp trước ngày luật này có hiệu lực có tiếp tục dùng được không và theo thời hạn nào?

**Đáp án cần bằng chứng:** Được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Gold:** [traffic-law-part2, PDF trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58).

**Evidence cần đủ:**

> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Rank 1:** [traffic-law-part2, trang 58, Chương IX](../../data/raw/36-2024-qh15-part2.pdf#page=58); chunk `9831be38257692e7bd7dc9917e74e120`.

> Điều 88. Hiệu lực thi hành
> 
> 1. Luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2025, trừ trường hợp quy định tại khoản 2 Điều này.
> 
> 2. Khoản 3 Điều 10 của Luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2026.
> 
> 3. Luật Giao thông đường bộ số 23/2008/QH12 đã được sửa đổi, bổ sung một số điều theo Luật số 35/2018/QH14 và Luật số 44/2019/QH14 hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ trường hợp quy định tại các khoản 1, 2, 5 và 6 Điều 89 của Luật này.
> 
> 4. Nghị quyết số 73/2022/QH15 của Quốc hội về thí điểm đấu giá biển số xe ô tô hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ trường hợp quy định tại khoản 7 Điều 89 của Luật này.

**Rank 2:** [traffic-law-part2, trang 58, Chương IX](../../data/raw/36-2024-qh15-part2.pdf#page=58); chunk `07bac735b6bae35e7f1c92f18888328e`.

> Điều 89. Quy định chuyển tiếp
> 
> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.
> 
> 2. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành nếu chưa thực hiện đổi, cấp lại theo quy định của Luật này có hiệu lực sử dụng như sau:
> 
> a) Giấy phép lái xe hạng A1 được tiếp tục điều khiển xe mô tô hai bánh có dung tích xi-lanh từ 50 cm3 đến dưới 175 cm3 hoặc có công suất động cơ điện từ 04 kW đến dưới 14 kW;
> 
> b) Giấy phép lái xe hạng A2 được tiếp tục điều khiển xe mô tô hai bánh có dung tích xi-lanh từ 175 cm3 trở lên hoặc có công suất động cơ điện từ 14 kW trở lên và các loại xe quy định cho giấy phép lái xe hạng A1 quy định tại điểm a khoản này;

**Rank 3:** [traffic-law-part2, trang 60, Chương IX](../../data/raw/36-2024-qh15-part2.pdf#page=60); chunk `f395d93c6a59bcaab009f9cef1f9b97c`.

> 3. Trường hợp người có giấy phép lái xe đã được cấp trước ngày Luật này có hiệu lực thi hành có nhu cầu đổi, cấp lại giấy phép lái xe thì thực hiện như sau:
> 
> a) Giấy phép lái xe hạng A1 được đổi, cấp lại sang giấy phép lái xe hạng A với điều kiện hạn chế là chỉ được điều khiển xe mô tô hai bánh có dung tích xi-lanh đến dưới 175 cm3 hoặc có công suất động cơ điện đến dưới 14 kW;
> 
> b) Giấy phép lái xe hạng A2 được đổi, cấp lại sang giấy phép lái xe hạng A;
> 
> c) Giấy phép lái xe hạng A3 được đổi, cấp lại sang giấy phép lái xe hạng B1;
> 
> d) Giấy phép lái xe hạng A4 được đổi, cấp lại sang chứng chỉ điều khiển xe máy chuyên dùng cho người điều khiển máy kéo có trọng tải đến 1.000 kg và chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ cho người điều khiển xe máy chuyên dùng;

**Lý do AI:** Rank 2 giữ Điều 89 và khoản 1 đúng trường hợp giấy phép cấp trước luật; rank 1 giúp xác định ngày hiệu lực, tất cả thuộc Chương IX.

- [x] Đã tự đọc top-3 của C/Q20; đồng ý hoặc đã ghi nhãn/lý do khác.

## 3. Metadata — 45 bản ghi

Code đã đối chiếu URL, trang vật lý, text theo offsets, chương, số trang in và nhãn snapshot với PDF/manifest: **45/45 khớp**. Học viên đã xác nhận đối chiếu đủ 45 bản ghi với nguồn; cột tự động và xác nhận của học viên được ghi riêng.

| Strategy/câu/rank | PDF nguồn | Chương | URL/trang/text/chương khớp tự động | Học viên đã kiểm tra |
|---|---|---|---|---|
| A/Q16/1 | [traffic-law-part2, trang 3](../../data/raw/36-2024-qh15-part2.pdf#page=3) | II | Có | Đã xác nhận |
| A/Q16/2 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| A/Q16/3 | [traffic-law-part2, trang 48](../../data/raw/36-2024-qh15-part2.pdf#page=48) | VI | Có | Đã xác nhận |
| A/Q17/1 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| A/Q17/2 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| A/Q17/3 | [traffic-law-part2, trang 5](../../data/raw/36-2024-qh15-part2.pdf#page=5) | II | Có | Đã xác nhận |
| A/Q18/1 | [traffic-law-part2, trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39) | IV | Có | Đã xác nhận |
| A/Q18/2 | [traffic-law-part2, trang 8](../../data/raw/36-2024-qh15-part2.pdf#page=8) | III | Có | Đã xác nhận |
| A/Q18/3 | [traffic-law-part2, trang 32](../../data/raw/36-2024-qh15-part2.pdf#page=32) | IV | Có | Đã xác nhận |
| A/Q19/1 | [traffic-law-part2, trang 52](../../data/raw/36-2024-qh15-part2.pdf#page=52) | VII | Có | Đã xác nhận |
| A/Q19/2 | [traffic-law-part2, trang 53](../../data/raw/36-2024-qh15-part2.pdf#page=53) | VII | Có | Đã xác nhận |
| A/Q19/3 | [traffic-law-part2, trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51) | VII | Có | Đã xác nhận |
| A/Q20/1 | [traffic-law-part2, trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58) | IX | Có | Đã xác nhận |
| A/Q20/2 | [traffic-law-part2, trang 37](../../data/raw/36-2024-qh15-part2.pdf#page=37) | IV | Có | Đã xác nhận |
| A/Q20/3 | [traffic-law-part2, trang 60](../../data/raw/36-2024-qh15-part2.pdf#page=60) | IX | Có | Đã xác nhận |
| B/Q16/1 | [traffic-law-part2, trang 1](../../data/raw/36-2024-qh15-part2.pdf#page=1) | II | Có | Đã xác nhận |
| B/Q16/2 | [traffic-law-part2, trang 3](../../data/raw/36-2024-qh15-part2.pdf#page=3) | II | Có | Đã xác nhận |
| B/Q16/3 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| B/Q17/1 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| B/Q17/2 | [traffic-law-part1, trang 19](../../data/raw/36-2024-qh15-part1.pdf#page=19) | II | Có | Đã xác nhận |
| B/Q17/3 | [traffic-law-part2, trang 23](../../data/raw/36-2024-qh15-part2.pdf#page=23) | III | Có | Đã xác nhận |
| B/Q18/1 | [traffic-law-part2, trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39) | IV | Có | Đã xác nhận |
| B/Q18/2 | [traffic-law-part2, trang 32](../../data/raw/36-2024-qh15-part2.pdf#page=32) | IV | Có | Đã xác nhận |
| B/Q18/3 | [traffic-law-part2, trang 6](../../data/raw/36-2024-qh15-part2.pdf#page=6) | II | Có | Đã xác nhận |
| B/Q19/1 | [traffic-law-part2, trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51) | VII | Có | Đã xác nhận |
| B/Q19/2 | [traffic-law-part2, trang 53](../../data/raw/36-2024-qh15-part2.pdf#page=53) | VII | Có | Đã xác nhận |
| B/Q19/3 | [traffic-law-part2, trang 52](../../data/raw/36-2024-qh15-part2.pdf#page=52) | VII | Có | Đã xác nhận |
| B/Q20/1 | [traffic-law-part2, trang 33](../../data/raw/36-2024-qh15-part2.pdf#page=33) | IV | Có | Đã xác nhận |
| B/Q20/2 | [traffic-law-part2, trang 32](../../data/raw/36-2024-qh15-part2.pdf#page=32) | IV | Có | Đã xác nhận |
| B/Q20/3 | [traffic-law-part2, trang 37](../../data/raw/36-2024-qh15-part2.pdf#page=37) | IV | Có | Đã xác nhận |
| C/Q16/1 | [traffic-law-part2, trang 1](../../data/raw/36-2024-qh15-part2.pdf#page=1) | II | Có | Đã xác nhận |
| C/Q16/2 | [traffic-law-part2, trang 3](../../data/raw/36-2024-qh15-part2.pdf#page=3) | II | Có | Đã xác nhận |
| C/Q16/3 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| C/Q17/1 | [traffic-law-part2, trang 2](../../data/raw/36-2024-qh15-part2.pdf#page=2) | II | Có | Đã xác nhận |
| C/Q17/2 | [traffic-law-part1, trang 19](../../data/raw/36-2024-qh15-part1.pdf#page=19) | II | Có | Đã xác nhận |
| C/Q17/3 | [traffic-law-part2, trang 23](../../data/raw/36-2024-qh15-part2.pdf#page=23) | III | Có | Đã xác nhận |
| C/Q18/1 | [traffic-law-part2, trang 39](../../data/raw/36-2024-qh15-part2.pdf#page=39) | IV | Có | Đã xác nhận |
| C/Q18/2 | [traffic-law-part2, trang 32](../../data/raw/36-2024-qh15-part2.pdf#page=32) | IV | Có | Đã xác nhận |
| C/Q18/3 | [traffic-law-part2, trang 30](../../data/raw/36-2024-qh15-part2.pdf#page=30) | IV | Có | Đã xác nhận |
| C/Q19/1 | [traffic-law-part2, trang 51](../../data/raw/36-2024-qh15-part2.pdf#page=51) | VII | Có | Đã xác nhận |
| C/Q19/2 | [traffic-law-part2, trang 53](../../data/raw/36-2024-qh15-part2.pdf#page=53) | VII | Có | Đã xác nhận |
| C/Q19/3 | [traffic-law-part2, trang 52](../../data/raw/36-2024-qh15-part2.pdf#page=52) | VII | Có | Đã xác nhận |
| C/Q20/1 | [traffic-law-part2, trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58) | IX | Có | Đã xác nhận |
| C/Q20/2 | [traffic-law-part2, trang 58](../../data/raw/36-2024-qh15-part2.pdf#page=58) | IX | Có | Đã xác nhận |
| C/Q20/3 | [traffic-law-part2, trang 60](../../data/raw/36-2024-qh15-part2.pdf#page=60) | IX | Có | Đã xác nhận |

Text của từng hit nằm trong phần grounding ở trên, đối chiếu theo strategy/câu/rank. Các trường đầy đủ trong [metadata_samples.json](../run/metadata_samples.json).

## 4. Ghi nhận kết quả tự chấm

Điền nhãn, lý do, tên người chấm thật và `status=human_verified` trong [manual_coherence.csv](manual_coherence.csv), [manual_grounding.csv](manual_grounding.csv), [manual_metadata.csv](manual_metadata.csv). Giữ ID và nguồn của mẫu. Không tự thay reviewer của nhãn AI để coi là nhãn học viên.

Nếu đã tự đọc và đồng ý tất cả đề xuất, có thể phản hồi rõ phạm vi đã đối chiếu để Codex hỗ trợ nhập lại đúng những nhãn bạn xác nhận. Nếu khác, ghi ID và điểm/lý do mới. Việc xem đề xuất AI trước chấm cần được công bố như một nguồn thiên lệch.

Đã tổng hợp đủ 90/90 dòng `human_verified`; xem `manual_summary.json`. Nhãn AI gốc được giữ riêng; thay đổi sau này cần được review và ghi nhận rõ.
