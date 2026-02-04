# Quick Start Guide - Hệ thống KPI ICTU

## Khởi động nhanh trong 5 phút

### Điều kiện tiên quyết
- Node.js 16+ đã cài đặt
- MongoDB đã cài đặt và đang chạy
- Git đã cài đặt

---

## Bước 1: Clone repository (30 giây)

```bash
git clone https://github.com/Tituslefebvre/KPI-CNTT.git
cd KPI-CNTT
```

---

## Bước 2: Cài đặt Backend (1 phút)

```bash
cd backend
npm install
cp .env.example .env
```

Chỉnh sửa file `.env` nếu cần (mặc định đã OK):
```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/kpi-ictu
JWT_SECRET=ictu-kpi-secret-key-2024
```

---

## Bước 3: Seed dữ liệu mẫu (30 giây)

```bash
cd ..
node database/seed.js
```

Kết quả:
```
✓ Created users
✓ Created KPIs
✓ Created evaluations
```

---

## Bước 4: Khởi động Backend (30 giây)

```bash
cd backend
npm run dev
```

Thông báo thành công:
```
✓ Server đang chạy trên cổng 5000
✓ MongoDB Connected
```

Mở terminal mới cho bước tiếp theo.

---

## Bước 5: Cài đặt và chạy Frontend (1 phút 30 giây)

```bash
cd frontend
npm install
npm run dev
```

Thông báo thành công:
```
✓ ready - started server on 0.0.0.0:3000
```

---

## Bước 6: Truy cập ứng dụng (10 giây)

Mở trình duyệt và truy cập: **http://localhost:3000**

---

## Đăng nhập thử nghiệm

Sử dụng một trong các tài khoản sau:

### Tài khoản Admin
```
Email: admin@ictu.edu.vn
Password: admin123
```

### Tài khoản Giảng viên
```
Email: giangvien1@ictu.edu.vn
Password: gv123456
```

### Tài khoản Trưởng khoa
```
Email: truongkhoa@ictu.edu.vn
Password: tk123456
```

---

## Sử dụng Docker (Tùy chọn)

Nếu bạn có Docker và Docker Compose:

```bash
docker-compose up -d
```

Chờ vài phút để containers khởi động, sau đó truy cập:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

---

## Test API với Postman

1. Import file `docs/postman_collection.json` vào Postman
2. Đăng nhập để lấy token
3. Copy token vào biến môi trường
4. Test các endpoint

---

## Kiểm tra nhanh

### Test Backend
```bash
curl http://localhost:5000/api
```

Kết quả mong đợi:
```json
{
  "success": true,
  "message": "Hệ thống đánh giá KPI ICTU API",
  "version": "1.0.0"
}
```

### Test Frontend
Truy cập: http://localhost:3000
Bạn sẽ thấy trang đăng nhập.

---

## Tính năng chính cần thử

1. **Đăng nhập** với tài khoản giảng viên
2. **Xem Dashboard** - thống kê tổng quan
3. **Xem danh sách KPI** - tất cả KPI năm học 2024-2025
4. **Xem đánh giá của tôi** - các đánh giá đã được tạo

---

## Troubleshooting nhanh

### Backend không khởi động được?
```bash
# Kiểm tra MongoDB đang chạy
sudo systemctl status mongod

# Hoặc khởi động MongoDB
sudo systemctl start mongod
```

### Frontend không khởi động được?
```bash
# Xóa node_modules và cài lại
rm -rf node_modules package-lock.json
npm install
```

### Port đã được sử dụng?
```bash
# Kill process đang dùng port 5000
lsof -ti:5000 | xargs kill -9

# Kill process đang dùng port 3000
lsof -ti:3000 | xargs kill -9
```

---

## Tài liệu đầy đủ

Để biết thêm chi tiết, xem:
- [README.md](../README.md) - Tổng quan hệ thống
- [DEPLOYMENT.md](DEPLOYMENT.md) - Hướng dẫn triển khai
- [API.md](API.md) - Tài liệu API
- [USER_GUIDE.md](USER_GUIDE.md) - Hướng dẫn sử dụng

---

## Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra [Troubleshooting section](#troubleshooting-nhanh)
2. Xem [Issues trên GitHub](https://github.com/Tituslefebvre/KPI-CNTT/issues)
3. Liên hệ: support@ictu.edu.vn

---

**Chúc bạn sử dụng hệ thống thành công! 🎉**
