# Hướng dẫn Nhanh (Quick Start Guide)

## Cài đặt và Chạy (Installation & Setup)

### 1. Clone Repository
```bash
git clone https://github.com/Tituslefebvre/KPI-CNTT.git
cd KPI-CNTT
```

### 2. Tạo Virtual Environment
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Cài đặt Dependencies
```bash
pip install -r requirements.txt
```

### 4. Khởi tạo Database
```bash
python init_db.py
```

### 5. Chạy Demo (Tùy chọn)
```bash
# Tạo dữ liệu đánh giá mẫu
python demo.py

# Chỉ xem thống kê
python demo.py stats
```

### 6. Chạy Ứng dụng
```bash
python run.py
```

### 7. Truy cập
Mở trình duyệt và truy cập: **http://localhost:5000**

## Tài khoản Đăng nhập Mặc định

### Admin (Quản trị viên)
- **Username**: `admin`
- **Password**: `admin123`
- **Quyền**: Quản lý toàn bộ hệ thống

### Manager (Quản lý)
- **Username**: `manager`
- **Password**: `manager123`
- **Quyền**: Quản lý KPI và đánh giá

### Staff (Viên chức)
- **Username**: `staff01`
- **Password**: `staff123`
- **Quyền**: Tự đánh giá

⚠️ **Lưu ý**: Đổi mật khẩu sau khi đăng nhập lần đầu trong môi trường production!

## Cấu trúc Thư mục

```
KPI-CNTT/
├── app/                      # Mã nguồn ứng dụng
│   ├── __init__.py          # Khởi tạo Flask app
│   ├── models.py            # Database models
│   ├── routes/              # Routes/Controllers
│   │   ├── auth.py         # Xác thực
│   │   ├── main.py         # Trang chủ
│   │   ├── staff.py        # Quản lý viên chức
│   │   ├── kpi.py          # Quản lý KPI
│   │   └── evaluation.py   # Đánh giá
│   ├── templates/           # HTML templates
│   └── static/              # CSS, JS, images
├── config.py                # Cấu hình
├── run.py                   # Entry point
├── init_db.py              # Script khởi tạo DB
├── demo.py                  # Script demo
├── requirements.txt         # Dependencies
├── README.md                # Tài liệu chính
├── ARCHITECTURE.md          # Kiến trúc hệ thống
└── QUICKSTART.md           # Hướng dẫn này
```

## Các Chức năng Chính

### 1. Dashboard
- Xem tổng quan hệ thống
- Theo dõi đánh giá gần đây
- Thống kê số liệu

### 2. Quản lý Viên chức
- Thêm/Sửa/Xem thông tin viên chức
- Quản lý hồ sơ cá nhân
- Liên kết với tài khoản người dùng

### 3. Quản lý KPI
- **Danh mục KPI**: Tổ chức theo nhóm (Giảng dạy, Nghiên cứu, Công tác khác)
- **Chỉ số KPI**: Các chỉ số cụ thể với mục tiêu và trọng số

### 4. Quản lý Đánh giá
- **Kỳ đánh giá**: Tạo và quản lý theo học kỳ/năm
- **Tự đánh giá**: Viên chức nhập dữ liệu thực tế
- **Phê duyệt**: Quản lý xem xét và phê duyệt
- **Tính điểm tự động**: Hệ thống tính điểm dựa trên công thức

## Workflow Sử dụng

### Cho Admin/Manager

1. **Thiết lập KPI**
   - Đăng nhập → Menu "KPI" → "Danh mục KPI" → "Thêm danh mục"
   - Menu "KPI" → "Chỉ số KPI" → "Thêm chỉ số KPI"

2. **Tạo Kỳ đánh giá**
   - Menu "Đánh giá" → "Kỳ đánh giá" → "Tạo kỳ đánh giá mới"
   - Nhập tên, thời gian bắt đầu và kết thúc

3. **Tạo Đánh giá cho Viên chức**
   - Menu "Đánh giá" → "Danh sách đánh giá" → "Tạo đánh giá mới"
   - Chọn viên chức và kỳ đánh giá

4. **Phê duyệt Đánh giá**
   - Menu "Đánh giá" → "Danh sách đánh giá"
   - Click "Xem" → Click "Phê duyệt"

### Cho Staff

1. **Xem Đánh giá**
   - Đăng nhập → Dashboard → Xem "Đánh giá gần đây"
   - Hoặc Menu "Đánh giá" → "Danh sách đánh giá"

2. **Nhập dữ liệu Tự đánh giá**
   - Click "Sửa" trên đánh giá ở trạng thái "Nháp"
   - Nhập giá trị thực tế cho từng KPI
   - Viết tự đánh giá (tùy chọn)
   - Click "Lưu và Nộp đánh giá"

3. **Xem Kết quả**
   - Hệ thống tự động tính điểm
   - Xem tổng điểm và chi tiết từng KPI
   - Chờ quản lý phê duyệt

## Công thức Tính điểm

```
Tỷ lệ đạt = Giá trị thực tế / Giá trị mục tiêu
Điểm = MIN(Tỷ lệ đạt × Điểm tối đa, Điểm tối đa)
```

**Ví dụ:**
- Mục tiêu: 200 giờ giảng dạy (max 50 điểm)
- Thực tế: 220 giờ
- Tỷ lệ đạt: 220/200 = 110%
- Điểm: 1.1 × 50 = 55 → **50 điểm** (không vượt max)

## Tùy chỉnh

### Thay đổi Secret Key (Production)
Sửa file `config.py`:
```python
SECRET_KEY = 'your-secret-key-here'
```

### Chuyển sang PostgreSQL
1. Cài đặt: `pip install psycopg2-binary`
2. Sửa `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/kpi_db'
```

### Thêm KPI mới
1. Đăng nhập với quyền Manager/Admin
2. Menu KPI → Chỉ số KPI → Thêm chỉ số KPI
3. Điền đầy đủ thông tin và lưu

## Xử lý Sự cố

### Lỗi: "No module named 'flask'"
```bash
# Đảm bảo đã activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Cài lại dependencies
pip install -r requirements.txt
```

### Lỗi: Database không tồn tại
```bash
# Chạy lại script khởi tạo
python init_db.py
```

### Lỗi: Port 5000 đã được sử dụng
Sửa file `run.py`, thay đổi port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Reset Database
```bash
# Xóa database cũ
rm kpi_system.db

# Tạo lại
python init_db.py
python demo.py  # Tạo dữ liệu mẫu (tùy chọn)
```

## Hỗ trợ

- **Repository**: https://github.com/Tituslefebvre/KPI-CNTT
- **Issues**: Tạo issue trên GitHub
- **Documentation**: Xem README.md và ARCHITECTURE.md

## Các Lệnh Hữu ích

```bash
# Xem thống kê hệ thống
python demo.py stats

# Tạo dữ liệu đánh giá mẫu
python demo.py

# Chạy Flask shell để thao tác database
flask shell

# Kiểm tra phiên bản
python --version
pip list

# Export requirements mới
pip freeze > requirements.txt
```

## Next Steps

1. ✅ Hoàn thành cài đặt
2. ✅ Chạy thử với dữ liệu mẫu
3. 📚 Đọc ARCHITECTURE.md để hiểu rõ hệ thống
4. 🎨 Tùy chỉnh giao diện (templates)
5. 🔧 Thêm tính năng mới theo nhu cầu
6. 🚀 Deploy lên production

---

**Happy Coding!** 🎉

Nếu có câu hỏi, đừng ngần ngại tạo issue trên GitHub!
