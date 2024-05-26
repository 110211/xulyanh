

Matches
Trong xử lý ảnh, đặc biệt là khi sử dụng các thuật toán phát hiện và mô tả đặc trưng (như SIFT, SURF, ORB), "matches" (sự khớp) là các cặp điểm đặc trưng tương ứng giữa hai hình ảnh mà chúng ta tin rằng chúng thể hiện cùng một điểm trong không gian thực.

Keypoints (Điểm đặc trưng): Là các điểm đáng chú ý trong hình ảnh, như các góc, cạnh hoặc các chi tiết nổi bật mà thuật toán có thể phát hiện.
Descriptors (Mô tả đặc trưng): Là các vector số đại diện cho vùng xung quanh mỗi điểm đặc trưng, dùng để so sánh các điểm đặc trưng giữa các hình ảnh.
Khi so sánh hai hình ảnh, thuật toán sẽ tính toán sự tương đồng giữa các mô tả đặc trưng của các điểm đặc trưng trong hai hình ảnh và tìm ra các "matches" - những cặp điểm có mô tả đặc trưng tương tự nhau.

Lowe's Ratio Test
Lowe's Ratio Test là một phương pháp để lọc các matches tốt ra khỏi các matches không chính xác hoặc nhiễu. Phương pháp này được đề xuất bởi David Lowe, người phát minh ra thuật toán SIFT.

Cách hoạt động của Lowe's Ratio Test
Khi tìm kiếm các matches, thuật toán sẽ tìm hai điểm gần nhất trong không gian mô tả đặc trưng cho mỗi điểm đặc trưng. Chúng ta gọi chúng là best match (điểm khớp tốt nhất) và second best match (điểm khớp tốt thứ hai).

Lowe's Ratio Test so sánh khoảng cách (distance) giữa điểm đặc trưng và best match với khoảng cách giữa điểm đặc trưng và second best match. Tỷ lệ này giúp xác định xem điểm khớp tốt nhất có đủ khác biệt so với điểm khớp tốt thứ hai hay không.

Công thức để áp dụng Lowe's Ratio Test:

ratio=
distance(𝑏𝑒𝑠𝑡𝑚𝑎𝑡𝑐ℎ)distance(𝑠𝑒𝑐𝑜𝑛𝑑
 𝑏𝑒𝑠𝑡𝑚𝑎𝑡𝑐ℎ)ratio= distance(second best match)distance(best match)
​
 

Nếu tỷ lệ này nhỏ hơn một ngưỡng nào đó (thường là 0.7), match này được coi là tốt và được giữ lại. Nếu tỷ lệ này lớn hơn ngưỡng, match này có thể là nhiễu và bị loại bỏ.
