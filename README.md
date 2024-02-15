## Course
## Đệ quy
1. Khái niệm đệ quy
* Đệ quy là một function có thể gọi chính nó bên trong. Dùng để giải quết các bài toán có cấu trúc lặp lại.</br>
2. Ưu điểm cuả đệ quy:
* Kiến trúc dễ hiểu
* Code ngắn hơn While for
* Có cấu trúc lặp lại tương tự nhau</br>
3. Nhược điểm của đệ quy:
* Có thể có thời gian tính toán lâu hơn for while. Cái này e không chắc, Có thể mỗi lần gọi trong for while sẽ tốn ít tgian hơn gọi 1 function.....
* Có thể gặp lỗi đệ quy quá nhiều
* Tốn nhiều bộ nhớ hơn (có thể gấp 2), Vì mỗi vòng đệ quy sẽ stack thêm một ô nhớ. Điều này có thể sinh ra lỗi tràn ô nhớ
## Thuật toán sorted
## Bubble sorted
* Ý tưởng, đổi chỗ từng đôi một các giá trị trong chuỗi
* Độ phức tạp tính toán o(n^2)
## Selection sort
* Ý tưởng: tìm min rồi cho lên đầu chuỗi
* Độ phức tạp tính toán o(n^2)
## Insert sorted
* Ý tưởng, tìm vị trí lớn hơn bên trái nhỏ hơn bên phải rồi cho vào giữa
* độ phức tạp tính toán o(n**2)
## Merge sort
* Ý tưởng: Chia dãy ra làm 2 rồi sắp xếp hai dãy đó, so sánh từng giá trị của dãy bên này với dãy bên kia. Giá trị nào lớn hơn sẽ lưu vào dãy giá trị bên trái. Thuật toán có tính lặp lại nên ta nên viết theo phương pháp đệ quy.
* Độ phức tạp của thuật toán là o(n)