# Hệ thống Đánh giá KPI cho Viên chức - Nhân lực đào tạo

Hệ thống đánh giá hiệu suất làm việc của viên chức và nhân lực đào tạo thông qua các chỉ số KPI (Key Performance Indicators) tại Trường Đại học Công nghệ Thông tin và Truyền thông.

## Tính năng chính

### 1. Quản lý người dùng và viên chức
- Đăng nhập/Đăng ký tài khoản
- Phân quyền người dùng (Admin, Manager, Staff)
- Quản lý hồ sơ viên chức với đầy đủ thông tin:
  - Mã viên chức
  - Khoa/Phòng ban
  - Chức vụ
  - Học hàm, học vị
  - Thông tin liên hệ

### 2. Quản lý KPI
- **Danh mục KPI**: Tổ chức các chỉ số KPI theo danh mục
  - Giảng dạy
  - Nghiên cứu khoa học
  - Công tác khác
- **Chỉ số KPI**: Quản lý chi tiết các chỉ số đánh giá
  - Mã chỉ số
  - Tên và mô tả
  - Đơn vị đo
  - Trọng số
  - Giá trị mục tiêu
  - Điểm tối đa

### 3. Quản lý đánh giá
- **Kỳ đánh giá**: Tạo và quản lý các kỳ đánh giá theo học kỳ/năm học
- **Quy trình đánh giá**:
  1. Viên chức tự đánh giá và nhập số liệu thực tế
  2. Hệ thống tự động tính điểm dựa trên giá trị thực tế và mục tiêu
  3. Quản lý phê duyệt và nhận xét
- **Trạng thái đánh giá**:
  - Nháp (Draft)
  - Đã nộp (Submitted)
  - Đã phê duyệt (Approved)

### 4. Dashboard và báo cáo
- Thống kê tổng quan
- Theo dõi đánh giá cá nhân
- Xem lịch sử đánh giá

## Công nghệ sử dụng

- **Backend**: Python Flask
- **Database**: SQLite (có thể chuyển sang PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5, HTML/CSS/JavaScript
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy

## Cài đặt

### Yêu cầu hệ thống
- Python 3.8 hoặc cao hơn
- pip (Python package manager)

### Các bước cài đặt

1. **Clone repository**
```bash
git clone https://github.com/Tituslefebvre/KPI-CNTT.git
cd KPI-CNTT
```

2. **Tạo môi trường ảo (Virtual Environment)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Cài đặt các thư viện cần thiết**
```bash
pip install -r requirements.txt
```

4. **Khởi tạo database và dữ liệu mẫu**
```bash
python init_db.py
```

5. **Chạy ứng dụng**
```bash
python run.py
```

6. **Truy cập ứng dụng**
Mở trình duyệt và truy cập: `http://localhost:5000`

## Thông tin đăng nhập mặc định

Sau khi khởi tạo database, bạn có thể đăng nhập với các tài khoản sau:

### Quản trị viên (Admin)
- **Username**: `admin`
- **Password**: `admin123`
- **Quyền**: Quản lý toàn bộ hệ thống

### Quản lý (Manager)
- **Username**: `manager`
- **Password**: `manager123`
- **Quyền**: Tạo KPI, tạo đánh giá, phê duyệt đánh giá

### Viên chức (Staff)
- **Username**: `staff01`
- **Password**: `staff123`
- **Quyền**: Tự đánh giá, xem đánh giá của mình

**Lưu ý**: Vui lòng đổi mật khẩu mặc định sau khi đăng nhập lần đầu trong môi trường production.

## Cấu trúc dự án

```
KPI-CNTT/
├── app/
│   ├── __init__.py           # Khởi tạo Flask app
│   ├── models.py             # Database models
│   ├── routes/               # Routes/Controllers
│   │   ├── auth.py          # Authentication
│   │   ├── main.py          # Main pages
│   │   ├── staff.py         # Staff management
│   │   ├── kpi.py           # KPI management
│   │   └── evaluation.py    # Evaluation management
│   ├── templates/            # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   ├── staff/
│   │   ├── kpi/
│   │   └── evaluation/
│   └── static/               # CSS, JS, images
│       ├── css/
│       └── js/
├── config.py                 # Configuration
├── run.py                    # Application entry point
├── init_db.py               # Database initialization
├── requirements.txt          # Python dependencies
└── README.md                # Documentation
```

## Hướng dẫn sử dụng

### Đối với Viên chức

1. **Đăng nhập** vào hệ thống
2. **Xem Dashboard** để theo dõi các đánh giá của mình
3. **Tạo/Chỉnh sửa đánh giá**:
   - Vào menu "Đánh giá" > "Danh sách đánh giá"
   - Chọn đánh giá cần thực hiện
   - Nhập số liệu thực tế cho từng chỉ số KPI
   - Thêm tự đánh giá (nếu cần)
   - Lưu và nộp đánh giá

### Đối với Quản lý

1. **Quản lý KPI**:
   - Tạo danh mục KPI mới
   - Thêm các chỉ số KPI cụ thể
   - Thiết lập trọng số và giá trị mục tiêu

2. **Quản lý Kỳ đánh giá**:
   - Tạo kỳ đánh giá mới cho học kỳ/năm học
   - Kích hoạt/Vô hiệu hóa kỳ đánh giá

3. **Đánh giá và Phê duyệt**:
   - Xem danh sách đánh giá đã nộp
   - Xem chi tiết và nhận xét
   - Phê duyệt đánh giá

### Đối với Admin

- Có tất cả quyền của Manager
- Quản lý người dùng
- Quản lý viên chức
- Cấu hình hệ thống

## Mở rộng và Tùy chỉnh

### Thêm chỉ số KPI mới
1. Đăng nhập với quyền Manager/Admin
2. Vào menu "KPI" > "Chỉ số KPI"
3. Click "Tạo chỉ số KPI mới"
4. Điền thông tin và lưu

### Tùy chỉnh công thức tính điểm
Chỉnh sửa phương thức trong file `app/routes/evaluation.py`:
```python
# Tính điểm dựa trên giá trị thực tế và mục tiêu
achievement_rate = detail.actual_value / detail.indicator.target_value
detail.score = min(achievement_rate * detail.indicator.max_score, detail.indicator.max_score)
```

### Xuất báo cáo
Có thể mở rộng thêm chức năng xuất báo cáo ra Excel/PDF bằng cách sử dụng các thư viện:
- `openpyxl` hoặc `pandas` cho Excel
- `reportlab` hoặc `weasyprint` cho PDF

## Bảo mật

- Mật khẩu được mã hóa bằng `werkzeug.security`
- Sử dụng Flask-Login cho session management
- CSRF protection với Flask-WTF
- Phân quyền rõ ràng theo role

**Khuyến nghị cho Production**:
- Đổi `SECRET_KEY` trong `config.py`
- Sử dụng PostgreSQL/MySQL thay vì SQLite
- Cấu hình HTTPS
- Thêm rate limiting
- Backup database định kỳ

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## Hỗ trợ

Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng tạo issue trên GitHub.

## License

Dự án này được phát triển cho mục đích giáo dục và quản lý nội bộ tại Trường Đại học Công nghệ Thông tin và Truyền thông.

---

**Phát triển bởi**: Trường Đại học Công nghệ Thông tin và Truyền thông  
**Năm**: 2024