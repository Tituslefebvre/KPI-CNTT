# Hướng dẫn Sử dụng - Hệ thống KPI ICTU

## Mục lục
1. [Đăng nhập](#đăng-nhập)
2. [Dashboard](#dashboard)
3. [Quản lý KPI](#quản-lý-kpi)
4. [Quy trình Đánh giá](#quy-trình-đánh-giá)
5. [Vai trò và Quyền hạn](#vai-trò-và-quyền-hạn)

---

## Đăng nhập

### Bước 1: Truy cập trang đăng nhập
Mở trình duyệt và truy cập: `http://localhost:3000`

### Bước 2: Nhập thông tin đăng nhập
- **Email**: Địa chỉ email của bạn trong hệ thống
- **Mật khẩu**: Mật khẩu đã được cấp

### Bước 3: Nhấn "Đăng nhập"
Sau khi đăng nhập thành công, bạn sẽ được chuyển đến trang Dashboard.

---

## Dashboard

Dashboard hiển thị tổng quan về KPI và đánh giá của bạn:

### Các chỉ số hiển thị:
- **Tổng số KPI**: Số lượng KPI được giao
- **Đánh giá của tôi**: Tổng số đánh giá cá nhân
- **Đã hoàn thành**: Số đánh giá đã hoàn tất
- **Chờ đánh giá**: Số đánh giá đang chờ xử lý

### Menu điều hướng:
- **Tổng quan**: Hiển thị thống kê tổng quan
- **Danh sách KPI**: Xem tất cả KPI áp dụng
- **Đánh giá của tôi**: Xem các đánh giá cá nhân
- **Quản lý KPI** (Trưởng khoa/Admin): Tạo và quản lý KPI
- **Báo cáo** (Trưởng khoa/Admin): Xem báo cáo tổng hợp

---

## Quản lý KPI

### Xem danh sách KPI

1. Nhấn vào **"Danh sách KPI"** trong menu
2. Hệ thống hiển thị bảng danh sách KPI với các thông tin:
   - Mã KPI
   - Tên KPI
   - Loại KPI (Giảng dạy, Nghiên cứu khoa học, Phục vụ cộng đồng, Quản lý)
   - Chỉ tiêu
   - Trọng số (%)
   - Trạng thái

### Tạo KPI mới (Trưởng khoa/Admin)

1. Nhấn vào **"Quản lý KPI"** trong menu
2. Nhấn nút **"Tạo KPI mới"**
3. Điền thông tin KPI:
   - Mã KPI (ví dụ: KPI-GD-001)
   - Tên KPI
   - Mô tả chi tiết
   - Loại KPI
   - Đơn vị đo (giờ, bài, đề tài, v.v.)
   - Chỉ tiêu (mục tiêu cần đạt)
   - Trọng số (%)
   - Năm học
4. Nhấn **"Lưu"**

### Chỉnh sửa KPI (Trưởng khoa/Admin)

1. Trong danh sách KPI, nhấn vào KPI cần chỉnh sửa
2. Nhấn nút **"Chỉnh sửa"**
3. Cập nhật thông tin cần thiết
4. Nhấn **"Lưu"**

---

## Quy trình Đánh giá

### Luồng đánh giá:
```
1. Tạo đánh giá (Admin/Trưởng khoa)
   ↓
2. Tự đánh giá (Nhân viên)
   ↓
3. Đánh giá của Trưởng bộ môn
   ↓
4. Đánh giá cuối cùng (Trưởng khoa)
   ↓
5. Hoàn thành
```

### 1. Tự đánh giá (Nhân viên)

**Bước 1:** Truy cập **"Đánh giá của tôi"**
- Xem danh sách các KPI cần đánh giá

**Bước 2:** Chọn KPI cần tự đánh giá
- Nhấn vào KPI trong danh sách

**Bước 3:** Điền thông tin tự đánh giá
- **Kết quả thực hiện**: Nhập số liệu thực tế đạt được
- **Điểm tự đánh giá**: Đánh giá điểm số (0-100)
- **Ghi chú**: Mô tả chi tiết về công việc đã thực hiện

**Bước 4:** Nhấn **"Gửi đánh giá"**

### 2. Đánh giá của Trưởng bộ môn

**Bước 1:** Truy cập danh sách đánh giá cần xem xét

**Bước 2:** Xem chi tiết đánh giá
- Xem thông tin tự đánh giá của nhân viên
- Xem kết quả thực hiện

**Bước 3:** Đưa ra đánh giá
- **Điểm đánh giá**: Nhập điểm (0-100)
- **Nhận xét**: Ghi nhận xét chi tiết

**Bước 4:** Nhấn **"Gửi đánh giá"**

### 3. Đánh giá cuối cùng (Trưởng khoa)

**Bước 1:** Xem tất cả đánh giá đã qua Trưởng bộ môn

**Bước 2:** Xem xét và đánh giá
- Xem điểm tự đánh giá
- Xem điểm của Trưởng bộ môn
- Xem nhận xét

**Bước 3:** Đưa ra đánh giá cuối cùng
- **Điểm cuối cùng**: Nhập điểm chính thức (0-100)
- **Nhận xét**: Ghi nhận xét cuối cùng

**Bước 4:** Nhấn **"Hoàn thành đánh giá"**

---

## Vai trò và Quyền hạn

### 1. Giảng viên / Nhân viên
**Quyền hạn:**
- Xem danh sách KPI được giao
- Tự đánh giá KPI của bản thân
- Xem kết quả đánh giá từ cấp trên
- Xem báo cáo cá nhân

**Không thể:**
- Tạo hoặc sửa KPI
- Đánh giá người khác
- Xóa đánh giá

### 2. Trưởng bộ môn
**Quyền hạn:**
- Tất cả quyền của Giảng viên
- Đánh giá KPI của giảng viên trong bộ môn
- Xem báo cáo bộ môn
- Đưa ra nhận xét và đề xuất

**Không thể:**
- Tạo hoặc sửa KPI
- Đánh giá cuối cùng
- Xóa dữ liệu

### 3. Trưởng khoa
**Quyền hạn:**
- Tất cả quyền của Trưởng bộ môn
- Tạo và quản lý KPI
- Đánh giá cuối cùng cho tất cả nhân viên
- Xem báo cáo toàn khoa
- Phê duyệt kết quả

**Không thể:**
- Xóa người dùng
- Sửa đổi quyền truy cập

### 4. Quản trị viên
**Quyền hạn:**
- Toàn quyền trên hệ thống
- Quản lý người dùng (thêm, sửa, xóa)
- Quản lý KPI (thêm, sửa, xóa)
- Quản lý đánh giá
- Xem tất cả báo cáo
- Cấu hình hệ thống

---

## Các loại KPI

### 1. Giảng dạy
- Số giờ giảng dạy
- Điểm đánh giá từ sinh viên
- Số môn học giảng dạy
- Hướng dẫn đồ án, khóa luận

### 2. Nghiên cứu khoa học
- Số bài báo khoa học
- Số đề tài nghiên cứu
- Sách, giáo trình xuất bản
- Tham gia hội nghị khoa học

### 3. Phục vụ cộng đồng
- Hoạt động đoàn thể
- Tư vấn, hướng dẫn sinh viên
- Tham gia công tác xã hội
- Các hoạt động ngoại khóa

### 4. Quản lý
- Công tác quản lý khoa, bộ môn
- Tổ chức sự kiện
- Phát triển chương trình đào tạo
- Hợp tác đối tác

---

## Thang điểm đánh giá

- **90-100**: Xuất sắc
- **80-89**: Tốt
- **70-79**: Khá
- **60-69**: Trung bình
- **Dưới 60**: Cần cải thiện

---

## Câu hỏi thường gặp (FAQ)

### Q: Làm thế nào để thay đổi mật khẩu?
A: Liên hệ với quản trị viên để được hỗ trợ thay đổi mật khẩu.

### Q: Tôi có thể sửa đánh giá đã gửi không?
A: Không, sau khi gửi đánh giá, bạn không thể tự sửa. Vui lòng liên hệ Trưởng khoa để được hỗ trợ.

### Q: Khi nào tôi cần hoàn thành tự đánh giá?
A: Thời hạn tự đánh giá sẽ được thông báo qua email hoặc trong hệ thống.

### Q: Ai có thể xem đánh giá của tôi?
A: Đánh giá của bạn có thể được xem bởi:
- Bản thân bạn
- Trưởng bộ môn
- Trưởng khoa
- Quản trị viên

---

## Hỗ trợ kỹ thuật

Nếu gặp vấn đề kỹ thuật, vui lòng liên hệ:
- **Email**: support@ictu.edu.vn
- **Điện thoại**: 024.xxxx.xxxx
- **Giờ làm việc**: 8:00 - 17:00 (Thứ 2 - Thứ 6)
