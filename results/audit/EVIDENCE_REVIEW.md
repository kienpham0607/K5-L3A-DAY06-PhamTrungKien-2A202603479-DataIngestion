# Đối chiếu 20 câu hỏi với PDF gốc

**Đã ghi nhận học viên Phạm Trung Kiên xác nhận:** “Đã đối chiếu 20 câu và đủ 90 mẫu; đồng ý các đề xuất”. Bản kiểm tra do AI hỗ trợ đã được học viên chấp nhận sau đối chiếu nguồn; không phải đánh giá mù. Xem [bản ghi xác nhận](human_confirmation.json) và [manual_evidence.csv](manual_evidence.csv).

Chỉ kiểm tra bản luật gốc trong corpus, không xác nhận pháp luật hiện hành. Bộ câu hỏi, evidence, split và metrics đã khóa được giữ nguyên.

Kết quả: **20/20 evidence có thật đúng trang; 20/20 đáp án được nguồn hỗ trợ theo nhận xét AI; 15 dev / 5 test; 7 câu filter khớp chương**.

Cách dùng: đọc câu hỏi, đáp án, evidence và ghi chú; mở liên kết PDF để đối chiếu. Đánh dấu ô sau mỗi câu chỉ khi chính bạn đã đọc và đồng ý; nếu khác, ghi ID và lý do để sửa bản review, không tự thay benchmark sau khi đã xem test.

## Q01 — Điều 9 khoản 2 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 7](../../data/raw/36-2024-qh15-part1.pdf#page=7).

**Câu hỏi:** Trong Chương I về những quy định chung, hành vi lái phương tiện có nồng độ cồn trong máu hoặc hơi thở có bị nghiêm cấm không?

**Đáp án:** Có. Điều 9 khoản 2 nghiêm cấm điều khiển phương tiện khi trong máu hoặc hơi thở có nồng độ cồn.

**Evidence nguyên văn:**

> 2. Điều khiển phương tiện tham gia giao thông đường bộ mà trong máu hoặc hơi thở có nồng độ cồn.

**Ngữ cảnh quanh evidence:**

> ác quốc tế về trật tự, an toàn giao thông đường bộ. Điều 9. Các hành vi bị nghiêm cấm 1. Điều khiển xe cơ giới tham gia giao thông đường bộ không có giấy phép lái xe theo quy định của pháp luật; điều khiển xe máy chuyên dùng tham gia giao thông đường bộ không có giấy phép lái xe hoặc chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ, bằng hoặc chứng chỉ điều khiển xe máy chuyên dùng. 2. Điều khiển phương tiện tham gia giao thông đường bộ mà trong máu hoặc hơi thở có nồng độ cồn. 3. Điều khiển phương tiện tham gia giao thông đường bộ mà trong cơ thể có chất ma túy hoặc chất kích thích khác mà pháp luật cấm sử dụng.

**Nhận xét AI:** Khoản 2 nằm dưới tiêu đề Các hành vi bị nghiêm cấm. Đáp án có nồng độ cồn là hành vi bị cấm, đúng phạm vi Chương I; cần đọc cả tiêu đề để hiểu tính cấm.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q02 — Điều 2 khoản 6 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 1](../../data/raw/36-2024-qh15-part1.pdf#page=1).

**Câu hỏi:** Làn đường được định nghĩa như thế nào?

**Đáp án:** Là phần của phần đường xe chạy được chia theo chiều dọc của đường, có đủ chiều rộng cho xe chạy an toàn.

**Evidence nguyên văn:**

> 6. Làn đường là một phần của phần đường xe chạy được chia theo chiều dọc của đường, có đủ chiều rộng cho xe chạy an toàn.

**Ngữ cảnh quanh evidence:**

>  bộ là phương tiện giao thông đường bộ tham gia giao thông trên đường bộ. 4. Đường ưu tiên là đường mà trên đó phương tiện tham gia giao thông đường bộ được các phương tiện tham gia giao thông đường bộ đến từ hướng khác nhường đường khi qua nơi đường giao nhau, được cắm biển báo hiệu đường ưu tiên. 5. Phần đường xe chạy là phần của đường bộ được sử dụng cho phương tiện giao thông đường bộ đi lại. 6. Làn đường là một phần của phần đường xe chạy được chia theo chiều dọc của đường, có đủ chiều rộng cho xe chạy an toàn. Người ký: CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ Email: thongtinchinhphu@chinhphu.vn Cơ quan: VĂN PHÒNG CHÍNH PHỦ Thời gian ký: 28.08.2024 14:37:29 +07:00

**Nhận xét AI:** Có đủ phần đường xe chạy, chia theo chiều dọc và chiều rộng cho xe chạy an toàn, khớp định nghĩa trong đáp án.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q03 — Điều 10 khoản 3 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 10](../../data/raw/36-2024-qh15-part1.pdf#page=10).

**Câu hỏi:** Theo bản luật gốc, khi chở trẻ dưới 10 tuổi và thấp hơn 1,35 mét trên ô tô, quy tắc về hàng ghế và thiết bị an toàn là gì, có ngoại lệ nào?

**Đáp án:** Không ngồi cùng hàng ghế người lái, trừ ô tô chỉ có một hàng ghế; người lái phải sử dụng và hướng dẫn sử dụng thiết bị an toàn phù hợp cho trẻ.

**Evidence nguyên văn:**

> 3. Khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 mét trên xe ô tô không được cho trẻ em ngồi cùng hàng ghế với người lái xe, trừ loại xe ô tô chỉ có một hàng ghế; người lái xe phải sử dụng, hướng dẫn sử dụng thiết bị an toàn phù hợp cho trẻ em.

**Ngữ cảnh quanh evidence:**

> . Chương II QUY TẮC GIAO THÔNG ĐƯỜNG BỘ Điều 10. Quy tắc chung 1. Người tham gia giao thông đường bộ phải đi bên phải theo chiều đi của mình, đi đúng làn đường, phần đường quy định, chấp hành báo hiệu đường bộ và các quy tắc giao thông đường bộ khác. 2. Người lái xe và người được chở trên xe ô tô phải thắt dây đai an toàn tại những chỗ có trang bị dây đai an toàn khi tham gia giao thông đường bộ. 3. Khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 mét trên xe ô tô không được cho trẻ em ngồi cùng hàng ghế với người lái xe, trừ loại xe ô tô chỉ có một hàng ghế; người lái xe phải sử dụng, hướng dẫn sử dụng thiết bị an toàn phù hợp cho trẻ em. Điều 11. Chấp hành báo hiệu đường bộ 1. Báo hiệu đường bộ bao gồm: hiệu lệnh của người điều khiển giao thông; đèn tín hiệu giao thông; biển báo hiệu đường bộ; vạch kẻ đường và các dấu hiệu khác trên 

**Nhận xét AI:** Nguồn dùng đồng thời hai điều kiện dưới 10 tuổi VÀ thấp hơn 1,35 mét; đủ quy tắc hàng ghế, ngoại lệ ô tô chỉ một hàng ghế và nghĩa vụ dùng/hướng dẫn thiết bị an toàn. Chỉ kiểm tra snapshot gốc.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q04 — Điều 11 khoản 2 điểm a–d (dev)

**Nguồn:** [traffic-law-part1, trang PDF 11](../../data/raw/36-2024-qh15-part1.pdf#page=11).

**Câu hỏi:** Hiệu lệnh người điều khiển giao thông, đèn giao thông, biển báo và vạch đường có thứ tự ưu tiên ra sao?

**Đáp án:** Theo thứ tự: hiệu lệnh người điều khiển giao thông, tín hiệu đèn, biển báo, rồi vạch kẻ đường và dấu hiệu khác trên mặt đường.

**Evidence nguyên văn:**

> 2. Người tham gia giao thông đường bộ phải chấp hành báo hiệu đường bộ theo thứ tự ưu tiên từ trên xuống dưới như sau: a) Hiệu lệnh của người điều khiển giao thông; b) Tín hiệu đèn giao thông; c) Biển báo hiệu đường bộ; d) Vạch kẻ đường và các dấu hiệu khác trên mặt đường;

**Ngữ cảnh quanh evidence:**

> 2. Người tham gia giao thông đường bộ phải chấp hành báo hiệu đường bộ theo thứ tự ưu tiên từ trên xuống dưới như sau: a) Hiệu lệnh của người điều khiển giao thông; b) Tín hiệu đèn giao thông; c) Biển báo hiệu đường bộ; d) Vạch kẻ đường và các dấu hiệu khác trên mặt đường; đ) Cọc tiêu, tường bảo vệ, rào chắn, đinh phản quang, tiêu phản quang, cột Km, cọc H; e) Thiết bị âm thanh báo hiệu đường bộ. 3. Hiệu lệnh của người điều khiển giao thông được quy định như sau: a) Ta

**Nhận xét AI:** Thứ tự bốn loại mà câu hỏi nêu là người điều khiển, đèn, biển báo, vạch đường. Nguồn còn các mục đ/e nhưng câu hỏi không yêu cầu liệt kê tất cả loại báo hiệu.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q05 — Điều 13 khoản 2 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 14](../../data/raw/36-2024-qh15-part1.pdf#page=14).

**Câu hỏi:** Trên đường nhiều làn cùng chiều có vạch phân làn, mỗi lần chuyển làn được chuyển mấy làn và phải bảo đảm những điều kiện nào?

**Đáp án:** Chỉ chuyển ở nơi cho phép, mỗi lần một làn liền kề, có tín hiệu báo trước và quan sát khoảng cách an toàn phía trước, sau, hai bên.

**Evidence nguyên văn:**

> 2. Trên đường có nhiều làn đường cho xe đi cùng chiều được phân biệt bằng vạch kẻ phân làn đường, người điều khiển phương tiện tham gia giao thông đường bộ phải cho xe đi trong một làn đường và chỉ được chuyển làn đường ở những nơi cho phép; mỗi lần chuyển làn đường chỉ được phép chuyển sang một làn đường liền kề; khi chuyển làn đường phải có tín hiệu báo trước; phải quan sát bảo đảm khoảng cách an toàn với xe phía trước, phía sau và hai bên mới được chuyển làn.

**Ngữ cảnh quanh evidence:**

> 4. Bộ trưởng Bộ Giao thông vận tải quy định chi tiết về tốc độ và khoảng cách an toàn của xe cơ giới, xe máy chuyên dùng tham gia giao thông đường bộ. Điều 13. Sử dụng làn đường 1. Phương tiện tham gia giao thông đường bộ di chuyển với tốc độ thấp hơn phải đi về bên phải theo chiều đi của mình. 2. Trên đường có nhiều làn đường cho xe đi cùng chiều được phân biệt bằng vạch kẻ phân làn đường, người điều khiển phương tiện tham gia giao thông đường bộ phải cho xe đi trong một làn đường và chỉ được chuyển làn đường ở những nơi cho phép; mỗi lần chuyển làn đường chỉ được phép chuyển sang một làn đường liền kề; khi chuyển làn đường phải có tín hiệu báo trước; phải quan sát bảo đảm khoảng cách an toàn với xe phía trước, phía sau và hai bên mới được chuyển làn. 3. Trên một chiều đường có vạch kẻ phân làn đường, xe thô sơ phải đi trên làn đường bên phải trong cùng, xe cơ giới, xe máy chuyên dùng đi trên làn đường bên trái. 4. Trên làn đường dành riêng cho mộ

**Nhận xét AI:** Giữ đủ nơi cho phép, mỗi lần một làn liền kề, tín hiệu báo trước và quan sát khoảng cách an toàn trước/sau/hai bên.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q06 — Điều 14 khoản 2 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 14](../../data/raw/36-2024-qh15-part1.pdf#page=14).

**Câu hỏi:** Vượt xe thường phải vượt bên nào và những trường hợp nào được vượt bên phải?

**Đáp án:** Vượt bên trái; được vượt phải khi xe trước có tín hiệu rẽ trái hoặc đang rẽ trái, hoặc xe chuyên dùng làm việc trên đường không thể vượt trái.

**Evidence nguyên văn:**

> 2. Khi vượt các xe phải vượt bên trái; trường hợp khi xe phía trước có tín hiệu rẽ trái hoặc đang rẽ trái hoặc khi xe chuyên dùng đang làm việc trên đường mà không thể vượt bên trái thì được vượt về bên phải.

**Ngữ cảnh quanh evidence:**

> uống giao thông trên đường mà mỗi chiều đường xe chạy chỉ có một làn đường dành cho xe cơ giới, xe đi phía sau di chuyển sang bên trái để di chuyển lên trước xe phía trước. Trên đường có từ hai làn đường dành cho xe cơ giới cùng chiều trở lên được phân biệt bằng vạch kẻ đường, xe đi phía sau di chuyển lên trước xe phía trước thì áp dụng quy tắc sử dụng làn đường quy định tại Điều 13 của Luật này. 2. Khi vượt các xe phải vượt bên trái; trường hợp khi xe phía trước có tín hiệu rẽ trái hoặc đang rẽ trái hoặc khi xe chuyên dùng đang làm việc trên đường mà không thể vượt bên trái thì được vượt về bên phải. 3. Xe xin vượt chỉ được vượt khi không có chướng ngại vật phía trước, không có xe chạy ngược chiều trong đoạn đường định vượt, xe chạy trước không có tín hiệu vượt xe khác, đã có tín hiệu rẽ phải và 

**Nhận xét AI:** Vượt trái là quy tắc; ngoại lệ vượt phải gồm xe trước báo rẽ trái/đang rẽ trái hoặc xe chuyên dùng làm việc không thể vượt trái. Không diễn giải là ngoại lệ cho mọi tình huống nhiều làn.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q07 — Điều 16 khoản 2 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 16](../../data/raw/36-2024-qh15-part1.pdf#page=16).

**Câu hỏi:** Luật cấm lùi xe ở những nơi nào?

**Đáp án:** Đường một chiều, khu vực cấm dừng, phần đường người đi bộ qua đường, nơi đường bộ giao nhau hoặc giao cùng mức đường sắt, nơi tầm nhìn bị che khuất, hầm đường bộ và cao tốc.

**Evidence nguyên văn:**

> 2. Không được lùi xe ở đường một chiều, khu vực cấm dừng, trên phần đường dành cho người đi bộ qua đường, nơi đường bộ giao nhau, đường bộ giao nhau cùng mức với đường sắt, nơi tầm nhìn bị che khuất, trong hầm đường bộ, trên đường cao tốc.

**Ngữ cảnh quanh evidence:**

> sắt, đường hẹp, đường dốc, đoạn đường cong tầm nhìn bị che khuất, trên đường cao tốc, trong hầm đường bộ, trên đường một chiều, trừ khi có hiệu lệnh của người điều khiển giao thông hoặc chỉ dẫn của biển báo hiệu tạm thời. Điều 16. Lùi xe 1. Khi lùi xe, người điều khiển phương tiện tham gia giao thông đường bộ phải quan sát hai bên và phía sau xe, có tín hiệu lùi và chỉ lùi xe khi bảo đảm an toàn. 2. Không được lùi xe ở đường một chiều, khu vực cấm dừng, trên phần đường dành cho người đi bộ qua đường, nơi đường bộ giao nhau, đường bộ giao nhau cùng mức với đường sắt, nơi tầm nhìn bị che khuất, trong hầm đường bộ, trên đường cao tốc. Điều 17. Tránh xe đi ngược chiều 1. Trên đường không phân chia thành hai chiều xe chạy riêng biệt, hai xe đi ngược chiều tránh nhau, người điều khiển phương tiện tham gia giao thông đường bộ phải giả

**Nhận xét AI:** Đáp án liệt kê đúng các địa điểm cấm lùi, gồm đường một chiều, nơi cấm dừng, chỗ người đi bộ, giao nhau, giao cùng mức đường sắt, tầm nhìn khuất, hầm và cao tốc.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q08 — Điều 17 khoản 2 điểm b (dev)

**Nguồn:** [traffic-law-part1, trang PDF 16](../../data/raw/36-2024-qh15-part1.pdf#page=16).

**Câu hỏi:** Khi tránh nhau trên dốc, xe đang xuống hay xe đang lên phải nhường?

**Đáp án:** Xe xuống dốc nhường đường cho xe lên dốc.

**Evidence nguyên văn:**

> b) Xe xuống dốc phải nhường đường cho xe lên dốc;

**Ngữ cảnh quanh evidence:**

> nh hai chiều xe chạy riêng biệt, hai xe đi ngược chiều tránh nhau, người điều khiển phương tiện tham gia giao thông đường bộ phải giảm tốc độ và cho xe đi về bên phải theo chiều xe chạy của mình. 2. Các trường hợp nhường đường khi tránh nhau bao gồm: a) Nơi đường hẹp chỉ đủ cho một xe chạy và có chỗ tránh xe thì xe nào ở gần chỗ tránh hơn phải vào vị trí tránh, nhường đường cho xe đi ngược chiều; b) Xe xuống dốc phải nhường đường cho xe lên dốc; c) Xe có chướng ngại vật phía trước phải nhường đường cho xe không có chướng ngại vật phía trước.

**Nhận xét AI:** Câu về xe xuống dốc nhường xe lên dốc đúng nguyên văn, đặt trong ngữ cảnh tránh xe đi ngược chiều.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q09 — Điều 20 khoản 1 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 18](../../data/raw/36-2024-qh15-part1.pdf#page=18).

**Câu hỏi:** Người lái xe phải bật đèn chiếu sáng phía trước vào khung giờ nào và khi thời tiết ra sao?

**Đáp án:** Từ 18 giờ hôm trước đến 06 giờ hôm sau hoặc khi sương mù, khói, bụi, trời mưa, thời tiết xấu hạn chế tầm nhìn.

**Evidence nguyên văn:**

> 1. Người lái xe, người điều khiển xe máy chuyên dùng tham gia giao thông đường bộ phải bật đèn chiếu sáng phía trước trong thời gian từ 18 giờ ngày hôm trước đến 06 giờ ngày hôm sau hoặc khi có sương mù, khói, bụi, trời mưa, thời tiết xấu làm hạn chế tầm nhìn.

**Ngữ cảnh quanh evidence:**

> bằng đèn khẩn cấp hoặc đặt biển cảnh báo về phía sau xe để người điều khiển phương tiện tham gia giao thông đường bộ khác biết. Điều 19. Mở cửa xe 1. Chỉ được mở cửa xe khi xe đã dừng, đỗ. 2. Trước khi mở cửa xe, người mở cửa phải quan sát phía trước, phía sau và bên phía mở cửa xe, khi thấy an toàn mới được mở cửa xe, ra khỏi xe; không để cửa xe mở nếu không bảo đảm an toàn. Điều 20. Sử dụng đèn 1. Người lái xe, người điều khiển xe máy chuyên dùng tham gia giao thông đường bộ phải bật đèn chiếu sáng phía trước trong thời gian từ 18 giờ ngày hôm trước đến 06 giờ ngày hôm sau hoặc khi có sương mù, khói, bụi, trời mưa, thời tiết xấu làm hạn chế tầm nhìn.

**Nhận xét AI:** Đáp án giữ đủ mốc 18 giờ–06 giờ và điều kiện sương mù/khói/bụi/mưa/thời tiết xấu làm hạn chế tầm nhìn.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q10 — Điều 21 khoản 2 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 19](../../data/raw/36-2024-qh15-part1.pdf#page=19).

**Câu hỏi:** Trong khu đông dân cư và khu vực cơ sở khám chữa bệnh, không được dùng còi vào thời gian nào, trừ xe nào?

**Đáp án:** Từ 22 giờ hôm trước đến 05 giờ hôm sau, trừ xe ưu tiên.

**Evidence nguyên văn:**

> 2. Không sử dụng còi liên tục; không sử dụng còi có âm lượng không đúng quy định; không sử dụng còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau trong khu đông dân cư, khu vực cơ sở khám bệnh, chữa bệnh, trừ xe ưu tiên.

**Ngữ cảnh quanh evidence:**

> Người lái xe, người điều khiển xe máy chuyên dùng khi thực hiện công việc trên đường bộ phải bật sáng đèn cảnh báo màu vàng. Điều 21. Sử dụng tín hiệu còi 1. Chỉ được sử dụng tín hiệu còi của phương tiện tham gia giao thông đường bộ trong các trường hợp sau đây: a) Báo hiệu cho người tham gia giao thông đường bộ khi xuất hiện tình huống có thể mất an toàn giao thông; b) Báo hiệu chuẩn bị vượt xe. 2. Không sử dụng còi liên tục; không sử dụng còi có âm lượng không đúng quy định; không sử dụng còi trong thời gian từ 22 giờ ngày hôm trước đến 05 giờ ngày hôm sau trong khu đông dân cư, khu vực cơ sở khám bệnh, chữa bệnh, trừ xe ưu tiên. Điều 22. Nhường đường tại nơi đường giao nhau Khi đến gần đường giao nhau, người điều khiển phương tiện tham gia giao thông đường bộ phải quan sát, giảm tốc độ và nhường đường theo quy định sau đây: 

**Nhận xét AI:** Đúng khung giờ 22 giờ–05 giờ, khu đông dân cư/khu vực cơ sở khám chữa bệnh và ngoại lệ xe ưu tiên.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q11 — Điều 22 khoản 3 (dev)

**Nguồn:** [traffic-law-part1, trang PDF 19](../../data/raw/36-2024-qh15-part1.pdf#page=19).

**Câu hỏi:** Tại giao lộ có báo hiệu đi theo vòng xuyến thì nhường xe tới từ bên nào?

**Đáp án:** Nhường xe đi đến từ bên trái.

**Evidence nguyên văn:**

> 3. Tại nơi đường giao nhau có báo hiệu đi theo vòng xuyến, phải nhường đường cho xe đi đến từ bên trái.

**Ngữ cảnh quanh evidence:**

>  độ và nhường đường theo quy định sau đây: 1. Tại nơi đường giao nhau giữa đường không ưu tiên với đường ưu tiên hoặc giữa đường nhánh với đường chính thì xe đi từ đường không ưu tiên hoặc đường nhánh phải nhường đường cho xe đi trên đường ưu tiên hoặc đường chính từ bất kỳ hướng nào tới; 2. Tại nơi đường giao nhau không có báo hiệu đi theo vòng xuyến, phải nhường đường cho xe đi đến từ bên phải; 3. Tại nơi đường giao nhau có báo hiệu đi theo vòng xuyến, phải nhường đường cho xe đi đến từ bên trái.

**Nhận xét AI:** Có báo hiệu vòng xuyến thì nhường xe từ trái, không nhầm với quy tắc không có báo hiệu vòng xuyến ở khoản 2.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q12 — Điều 30 khoản 1 điểm a (dev)

**Nguồn:** [traffic-law-part2, trang PDF 5](../../data/raw/36-2024-qh15-part2.pdf#page=5).

**Câu hỏi:** Nếu đường không có vỉa hè, lề đường hay lối riêng cho người đi bộ thì người đi bộ phải đi ở đâu?

**Đáp án:** Đi sát mép đường bên phải theo chiều đi của mình.

**Evidence nguyên văn:**

> a) Phải đi trên vỉa hè, lề đường, đường dành riêng cho người đi bộ; trường hợp đường không có vỉa hè, lề đường, đường dành riêng cho người đi bộ thì người đi bộ phải đi sát mép đường bên phải theo chiều đi của mình;

**Ngữ cảnh quanh evidence:**

>  phải bảo đảm chắc chắn, an toàn. 3. Không được chở người trên xe được kéo, trừ người điều khiển; xe kéo rơ moóc, xe ô tô đầu kéo kéo sơ mi rơ moóc không được kéo thêm rơ moóc, sơ mi rơ moóc hoặc xe khác. Điều 30. Người đi bộ; trẻ em, phụ nữ mang thai, người già yếu, người khuyết tật, người mất năng lực hành vi dân sự tham gia giao thông đường bộ 1. Người đi bộ phải tuân thủ các quy định sau đây: a) Phải đi trên vỉa hè, lề đường, đường dành riêng cho người đi bộ; trường hợp đường không có vỉa hè, lề đường, đường dành riêng cho người đi bộ thì người đi bộ phải đi sát mép đường bên phải theo chiều đi của mình; b) Chỉ được qua đường ở những nơi có đèn tín hiệu, có vạch kẻ đường hoặc có cầu vượt, hầm dành cho người đi bộ và phải tuân thủ tín hiệu chỉ dẫn, báo hiệu đường bộ. Trường hợp không có đèn tín hiệu, 

**Nhận xét AI:** Đáp án đi sát mép đường bên phải đúng ngoại lệ khi không có vỉa hè/lề đường/đường riêng cho người đi bộ.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q13 — Điều 31 khoản 1 (dev)

**Nguồn:** [traffic-law-part2, trang PDF 6](../../data/raw/36-2024-qh15-part2.pdf#page=6).

**Câu hỏi:** Trong Chương II về quy tắc giao thông, xe đạp và xe đạp máy được chở bao nhiêu người, ngoại lệ khi chở thêm trẻ nhỏ là gì?

**Đáp án:** Chở một người; nếu chở thêm một trẻ dưới 07 tuổi thì chở tối đa hai người.

**Evidence nguyên văn:**

> 1. Người điều khiển xe đạp, xe đạp máy chỉ được chở một người, trừ trường hợp chở thêm một trẻ em dưới 07 tuổi thì được chở tối đa hai người.

**Ngữ cảnh quanh evidence:**

> Điều 31. Người điều khiển, người được chở, hàng hóa xếp trên xe thô sơ 1. Người điều khiển xe đạp, xe đạp máy chỉ được chở một người, trừ trường hợp chở thêm một trẻ em dưới 07 tuổi thì được chở tối đa hai người. 2. Người điều khiển xe đạp, xe đạp máy không được thực hiện các hành vi quy định tại khoản 3 Điều 33 của Luật này; người được chở trên xe đạp, xe đạp máy khi tham gia giao thông đường bộ không được t

**Nhận xét AI:** Đủ quy tắc chở một người và ngoại lệ chở thêm một trẻ dưới 07 tuổi, tối đa hai người. Áp dụng xe đạp/xe đạp máy, không suy rộng sang xe mô tô.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q14 — Điều 58 khoản 2 (dev)

**Nguồn:** [traffic-law-part2, trang PDF 33](../../data/raw/36-2024-qh15-part2.pdf#page=33).

**Câu hỏi:** Theo Chương IV về người điều khiển phương tiện, giấy phép chưa bị trừ hết điểm được phục hồi đủ 12 điểm khi nào?

**Đáp án:** Nếu không bị trừ điểm trong 12 tháng kể từ lần bị trừ điểm gần nhất.

**Evidence nguyên văn:**

> 2. Giấy phép lái xe chưa bị trừ hết điểm và không bị trừ điểm trong thời hạn 12 tháng từ ngày bị trừ điểm gần nhất thì được phục hồi đủ 12 điểm.

**Ngữ cảnh quanh evidence:**

> liệu về trật tự, an toàn giao thông đường bộ, bao gồm 12 điểm. Số điểm trừ mỗi lần vi phạm tùy thuộc tính chất, mức độ của hành vi vi phạm pháp luật về trật tự, an toàn giao thông đường bộ. Dữ liệu về điểm trừ giấy phép lái xe của người vi phạm sẽ được cập nhật vào hệ thống cơ sở dữ liệu ngay sau khi quyết định xử phạt có hiệu lực thi hành và thông báo cho người bị trừ điểm giấy phép lái xe biết. 2. Giấy phép lái xe chưa bị trừ hết điểm và không bị trừ điểm trong thời hạn 12 tháng từ ngày bị trừ điểm gần nhất thì được phục hồi đủ 12 điểm. 3. Trường hợp giấy phép lái xe bị trừ hết điểm thì người có giấy phép lái xe không được điều khiển phương tiện tham gia giao thông đường bộ theo giấy phép lái xe đó. Sau thời hạn ít nhất là 06 tháng 

**Nhận xét AI:** Điều kiện giấy phép chưa bị trừ hết điểm có ngay trong câu hỏi; đáp án giữ đủ 12 tháng không bị trừ tiếp, tính từ lần bị trừ gần nhất.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q15 — Điều 59 khoản 1 điểm a (dev)

**Nguồn:** [traffic-law-part2, trang PDF 34](../../data/raw/36-2024-qh15-part2.pdf#page=34).

**Câu hỏi:** Trong Chương IV về người điều khiển phương tiện, bao nhiêu tuổi mới được điều khiển xe gắn máy?

**Đáp án:** Đủ 16 tuổi trở lên.

**Evidence nguyên văn:**

> a) Người đủ 16 tuổi trở lên được điều khiển xe gắn máy;

**Ngữ cảnh quanh evidence:**

>  6. Chính phủ quy định chi tiết khoản 1 Điều này; quy định trình tự, thủ tục, thẩm quyền trừ điểm, phục hồi điểm giấy phép lái xe; quy định lộ trình thực hiện Điều này. Bộ trưởng Bộ Công an quy định chi tiết khoản 3 Điều này. Điều 59. Tuổi, sức khỏe của người điều khiển phương tiện tham gia giao thông đường bộ 1. Độ tuổi của người lái xe, người điều khiển xe máy chuyên dùng được quy định như sau: a) Người đủ 16 tuổi trở lên được điều khiển xe gắn máy; b) Người đủ 18 tuổi trở lên được cấp giấy phép lái xe hạng A1, A, B1, B, C1, được cấp chứng chỉ bồi dưỡng kiến thức pháp luật về giao thông đường bộ để điều khiển xe máy chuyên dùng tham gia giao thô

**Nhận xét AI:** Đúng đủ 16 tuổi trở lên cho xe gắn máy; không nhầm với điều kiện cấp giấy phép các hạng khác.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q16 — Điều 25 khoản 2 (test)

**Nguồn:** [traffic-law-part2, trang PDF 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Câu hỏi:** Trên cao tốc, khi xe gặp sự cố và không thể vào làn dừng khẩn cấp, phải cảnh báo phía sau cách tối thiểu bao xa và cần làm gì?

**Đáp án:** Bật đèn khẩn cấp, đặt biển hoặc đèn cảnh báo sau xe ít nhất 150 mét và nhanh chóng báo Cảnh sát giao thông trên tuyến hoặc cơ quan quản lý cao tốc.

**Evidence nguyên văn:**

> trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc.

**Ngữ cảnh quanh evidence:**

> c) Không được cho xe chạy ở làn dừng xe khẩn cấp và phần lề đường; d) Các quy tắc giao thông đường bộ khác quy định tại Chương này. 2. Chỉ được dừng xe, đỗ xe ở nơi quy định; trường hợp gặp sự cố kỹ thuật hoặc bất khả kháng khác buộc phải dừng xe, đỗ xe thì được dừng xe, đỗ xe ở làn dừng khẩn cấp cùng chiều xe chạy và phải có báo hiệu bằng đèn khẩn cấp; trường hợp xe không thể di chuyển được vào làn dừng khẩn cấp, phải có báo hiệu bằng đèn khẩn cấp và đặt biển hoặc đèn cảnh báo về phía sau xe khoảng cách tối thiểu 150 mét, nhanh chóng báo cho cơ quan Cảnh sát giao thông thực hiện nhiệm vụ bảo đảm trật tự, an toàn giao thông trên tuyến hoặc cơ quan quản lý đường cao tốc. 3. Xe máy chuyên dùng có tốc độ thiết kế nhỏ hơn tốc độ tối thiểu quy định đối với đường cao tốc, xe chở người bốn bánh có gắn động cơ, xe chở hàng bốn bánh có gắn động cơ, xe mô tô, xe gắn máy, các 

**Nhận xét AI:** Đúng trường hợp xe không vào được làn khẩn cấp: bật đèn khẩn cấp, đặt biển HOẶC đèn cảnh báo sau xe tối thiểu 150 mét, nhanh chóng báo CSGT trên tuyến HOẶC cơ quan quản lý cao tốc.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q17 — Điều 26 khoản 1 (test)

**Nguồn:** [traffic-law-part2, trang PDF 2](../../data/raw/36-2024-qh15-part2.pdf#page=2).

**Câu hỏi:** Khi đi trong hầm đường bộ, xe cơ giới, xe máy chuyên dùng và xe thô sơ phải sử dụng đèn thế nào?

**Đáp án:** Xe cơ giới, xe máy chuyên dùng bật đèn chiếu gần; xe thô sơ bật đèn hoặc có vật phát sáng báo hiệu.

**Evidence nguyên văn:**

> 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu;

**Ngữ cảnh quanh evidence:**

>  máy, các loại xe tương tự xe mô tô, xe gắn máy, xe thô sơ, người đi bộ không được đi trên đường cao tốc, trừ người, phương tiện giao thông đường bộ và thiết bị phục vụ việc quản lý, bảo trì đường cao tốc. Điều 26. Giao thông trong hầm đường bộ Người điều khiển phương tiện tham gia giao thông đường bộ khi điều khiển phương tiện trong hầm đường bộ phải tuân thủ quy tắc giao thông đường bộ sau đây: 1. Xe cơ giới, xe máy chuyên dùng phải bật đèn chiếu gần; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu; 2. Không dừng xe, đỗ xe trong hầm đường bộ; trường hợp gặp sự cố kỹ thuật hoặc bất khả kháng khác buộc phải dừng xe, đỗ xe, người lái xe, người điều khiển xe máy chuyên dùng phải đưa xe vào vị trí dừ

**Nhận xét AI:** Đủ đèn chiếu gần cho xe cơ giới/xe máy chuyên dùng và đèn hoặc vật phát sáng báo hiệu cho xe thô sơ trong hầm.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q18 — Điều 64 khoản 1 (test)

**Nguồn:** [traffic-law-part2, trang PDF 39](../../data/raw/36-2024-qh15-part2.pdf#page=39).

**Câu hỏi:** Trong Chương IV về người điều khiển phương tiện, thời gian lái xe ô tô kinh doanh vận tải và vận tải nội bộ tối đa mỗi ngày, mỗi tuần và liên tục là bao nhiêu?

**Đáp án:** Không quá 10 giờ/ngày, 48 giờ/tuần, liên tục không quá 04 giờ; bảo đảm quy định liên quan của Bộ luật Lao động.

**Evidence nguyên văn:**

> 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động.

**Ngữ cảnh quanh evidence:**

> Điều 64. Thời gian làm việc của người lái xe ô tô kinh doanh vận tải và vận tải nội bộ 1. Thời gian lái xe của người lái xe ô tô không quá 10 giờ trong một ngày và không quá 48 giờ trong một tuần; lái xe liên tục không quá 04 giờ và bảo đảm các quy định có liên quan của Bộ luật Lao động. 2. Đơn vị kinh doanh vận tải, đơn vị hoạt động vận tải nội bộ và người lái xe ô tô kinh doanh vận tải và vận tải nội bộ chịu trách nhiệm thực hiện các quy định tại Điều này. Chương V TUẦN TRA, KIỂM S

**Nhận xét AI:** Tiêu đề Điều 64 xác định phạm vi kinh doanh vận tải/vận tải nội bộ; đáp án giữ đủ 10 giờ/ngày, 48 giờ/tuần, 04 giờ liên tục và quy định liên quan của Bộ luật Lao động.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q19 — Điều 80 khoản 1 điểm b (test)

**Nguồn:** [traffic-law-part2, trang PDF 51](../../data/raw/36-2024-qh15-part2.pdf#page=51).

**Câu hỏi:** Trong Chương VII về giải quyết tai nạn, người gây tai nạn hoặc liên quan phải ở lại hiện trường đến khi nào, trường hợp nào được rời đi và phải trình báo ở đâu?

**Đáp án:** Ở lại đến khi Công an đến; được rời đi khi cấp cứu, đưa nạn nhân cấp cứu hoặc bị đe dọa tính mạng, sức khỏe, nhưng phải trình báo ngay Công an hoặc UBND gần nhất.

**Evidence nguyên văn:**

> b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất;

**Ngữ cảnh quanh evidence:**

> iện trường vụ tai nạn giao thông đường bộ 1. Người điều khiển phương tiện tham gia giao thông đường bộ gây ra tai nạn giao thông đường bộ, người liên quan đến vụ tai nạn giao thông đường bộ có trách nhiệm sau đây: a) Dừng ngay phương tiện, cảnh báo nguy hiểm, giữ nguyên hiện trường, trợ giúp người bị nạn và báo tin cho cơ quan Công an, cơ sở khám bệnh, chữa bệnh hoặc Ủy ban nhân dân nơi gần nhất; b) Ở lại hiện trường vụ tai nạn giao thông đường bộ cho đến khi người của cơ quan Công an đến, trừ trường hợp phải đi cấp cứu, đưa người bị nạn đi cấp cứu hoặc xét thấy bị đe dọa đến tính mạng, sức khỏe nhưng phải đến trình báo ngay cơ quan Công an, Ủy ban nhân dân nơi gần nhất; c) Cung cấp thông tin xác định danh tính về bản thân, người liên quan đến vụ tai nạn giao thông đường bộ và thông tin liên quan của vụ tai nạn giao thông đường bộ cho cơ quan có thẩm quyền. 2. Người 

**Nhận xét AI:** Đủ mốc Công an đến, ba ngoại lệ cấp cứu/đưa người bị nạn cấp cứu/bị đe dọa tính mạng sức khỏe và nghĩa vụ trình báo ngay Công an HOẶC UBND gần nhất.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

## Q20 — Điều 89 khoản 1 (test)

**Nguồn:** [traffic-law-part2, trang PDF 58](../../data/raw/36-2024-qh15-part2.pdf#page=58).

**Câu hỏi:** Theo Chương IX về điều khoản thi hành, giấy phép lái xe cấp trước ngày luật này có hiệu lực có tiếp tục dùng được không và theo thời hạn nào?

**Đáp án:** Được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Evidence nguyên văn:**

> 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe.

**Ngữ cảnh quanh evidence:**

> theo Luật số 35/2018/QH14 và Luật số 44/2019/QH14 hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ trường hợp quy định tại các khoản 1, 2, 5 và 6 Điều 89 của Luật này. 4. Nghị quyết số 73/2022/QH15 của Quốc hội về thí điểm đấu giá biển số xe ô tô hết hiệu lực kể từ ngày Luật này có hiệu lực thi hành, trừ trường hợp quy định tại khoản 7 Điều 89 của Luật này. Điều 89. Quy định chuyển tiếp 1. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành được tiếp tục sử dụng theo thời hạn ghi trên giấy phép lái xe. 2. Giấy phép lái xe được cấp trước ngày Luật này có hiệu lực thi hành nếu chưa thực hiện đổi, cấp lại theo quy định của Luật này có hiệu lực sử dụng như sau: a) Giấy phép lái xe hạng A1 được tiếp tục

**Nhận xét AI:** Đúng trường hợp giấy phép cấp trước ngày luật có hiệu lực, tiếp tục dùng theo thời hạn trên giấy phép; không nhầm với trừ điểm, giấy phép quốc tế hay thủ tục cấp đổi.

- [x] Tôi đã đối chiếu câu này với PDF và đồng ý / đã ghi rõ điểm cần sửa.

