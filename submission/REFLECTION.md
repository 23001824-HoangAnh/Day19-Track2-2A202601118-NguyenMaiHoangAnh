# Reflection — Lab 19

**Tên:** Nguyễn Mai Hoàng Anh
**Cohort:** _Chưa cung cấp_
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

Trên golden set, hybrid đạt Precision@10 trung bình cao nhất (78,6%), so với
BM25 77,8% và vector 73,2%. Với `exact`, BM25 và hybrid cùng đạt 96,7% vì từ
khóa kỹ thuật xuất hiện trực tiếp trong corpus. Với `mixed`, hybrid thắng rõ
(100%), nhờ kết hợp tín hiệu từ khóa của BM25 và ngữ nghĩa của vector. Ở
`paraphrase`, BM25 đạt 33,3%, hybrid 32,0% và vector 24,0%. Vector không thắng
slice này vì model Lite `bge-small-en-v1.5` thiên về tiếng Anh, nên biểu diễn
các diễn đạt lại bằng tiếng Việt còn yếu; đây là lý do cần thử `bge-m3` và
re-index khi chuyển backend.

Tôi không dùng hybrid khi truy vấn cần exact match, mã lỗi hoặc tên định danh
(BM25 đơn giản, nhanh hơn), hoặc khi corpus/query hoàn toàn ngữ nghĩa và model
embedding đã được đánh giá tốt cho ngôn ngữ miền dữ liệu (pure vector giảm chi
phí vận hành hai index).

---

## Điều ngạc nhiên nhất khi làm lab này

Hybrid P99 giảm từ 74,9 ms xuống 3,7 ms sau khi cache vector của query lặp,
trong khi Precision@10 không đổi.

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _<tên đồng đội nếu có>_
