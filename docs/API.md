# API Documentation - Hệ thống KPI ICTU

## Base URL
```
http://localhost:5000/api
```

## Authentication
Tất cả các endpoint được bảo vệ (trừ register và login) yêu cầu JWT token trong header:
```
Authorization: Bearer <token>
```

---

## Authentication Endpoints

### 1. Register User
Đăng ký tài khoản mới

**Endpoint:** `POST /auth/register`

**Request Body:**
```json
{
  "maNhanVien": "GV003",
  "hoTen": "Nguyễn Văn A",
  "email": "nguyenvana@ictu.edu.vn",
  "matKhau": "password123",
  "chucVu": "Giảng viên",
  "khoa": "Khoa Công nghệ Thông tin",
  "boMon": "Bộ môn Công nghệ Phần mềm"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "_id": "65f1a2b3c4d5e6f7g8h9i0j1",
    "maNhanVien": "GV003",
    "hoTen": "Nguyễn Văn A",
    "email": "nguyenvana@ictu.edu.vn",
    "chucVu": "Giảng viên",
    "khoa": "Khoa Công nghệ Thông tin",
    "boMon": "Bộ môn Công nghệ Phần mềm",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

### 2. Login
Đăng nhập vào hệ thống

**Endpoint:** `POST /auth/login`

**Request Body:**
```json
{
  "email": "giangvien1@ictu.edu.vn",
  "matKhau": "gv123456"
}
```

---

## KPI Management Endpoints

### Get All KPIs
Lấy danh sách tất cả KPI

**Endpoint:** `GET /kpis`

**Query Parameters:**
- `namHoc`: Năm học (optional)
- `loaiKPI`: Loại KPI (optional)
- `trangThai`: Trạng thái (optional)

---

## Evaluation Management Endpoints

### Self Evaluation
Tự đánh giá

**Endpoint:** `PUT /evaluations/:id/self`

**Request Body:**
```json
{
  "ketQuaThucHien": 280,
  "diemTuDanhGia": 95,
  "ghiChu": "Đã hoàn thành vượt chỉ tiêu"
}
```

---

## Test Data

Sau khi chạy seed script, bạn có thể sử dụng các tài khoản sau để test:

| Email | Password | Chức vụ |
|-------|----------|---------|
| admin@ictu.edu.vn | admin123 | Quản trị viên |
| truongkhoa@ictu.edu.vn | tk123456 | Trưởng khoa |
| truongbomon@ictu.edu.vn | tbm123456 | Trưởng bộ môn |
| giangvien1@ictu.edu.vn | gv123456 | Giảng viên |
| giangvien2@ictu.edu.vn | gv123456 | Giảng viên |
