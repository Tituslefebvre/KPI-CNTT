# Hướng dẫn Triển khai - Hệ thống KPI ICTU

> **⚠️ Security Notice**: Ensure you install the latest dependencies to address known vulnerabilities. See [SECURITY.md](../SECURITY.md) for details.

## Yêu cầu Hệ thống

### Phần mềm cần thiết:
- **Node.js**: phiên bản 16.x trở lên
- **MongoDB**: phiên bản 5.x trở lên
- **npm** hoặc **yarn**: để quản lý packages
- **Git**: để clone repository

### Cấu hình khuyến nghị:
- RAM: 4GB trở lên
- Dung lượng đĩa: 2GB trở lên
- CPU: 2 cores trở lên

---

## Cài đặt MongoDB

### Trên Ubuntu/Debian:
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
```

### Trên macOS:
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### Trên Windows:
1. Tải MongoDB từ: https://www.mongodb.com/try/download/community
2. Cài đặt theo hướng dẫn
3. Khởi động MongoDB service

---

## Cài đặt Backend

### Bước 1: Clone repository
```bash
git clone https://github.com/Tituslefebvre/KPI-CNTT.git
cd KPI-CNTT
```

### Bước 2: Cài đặt dependencies cho Backend
```bash
cd backend
npm install
```

### Bước 3: Cấu hình môi trường
Tạo file `.env` từ `.env.example`:
```bash
cp .env.example .env
```

Chỉnh sửa file `.env`:
```env
NODE_ENV=development
PORT=5000
MONGODB_URI=mongodb://localhost:27017/kpi-ictu
JWT_SECRET=your-secret-key-here-change-this-in-production
```

### Bước 4: Seed dữ liệu mẫu (optional)
```bash
cd ..
node database/seed.js
```

### Bước 5: Chạy Backend server
```bash
cd backend
npm run dev
```

Server sẽ chạy tại: `http://localhost:5000`

---

## Cài đặt Frontend

### Bước 1: Cài đặt dependencies
```bash
cd frontend
npm install
```

### Bước 2: Cấu hình (nếu cần)
Tạo file `.env.local` (optional):
```env
API_URL=http://localhost:5000/api
```

### Bước 3: Chạy Frontend
```bash
npm run dev
```

Ứng dụng sẽ chạy tại: `http://localhost:3000`

---

## Kiểm tra Cài đặt

### Kiểm tra Backend:
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

### Kiểm tra Frontend:
Mở trình duyệt và truy cập: `http://localhost:3000`

Bạn sẽ thấy trang đăng nhập của hệ thống.

---

## Đăng nhập vào Hệ thống

Sử dụng tài khoản test (sau khi seed data):

**Admin:**
- Email: admin@ictu.edu.vn
- Password: admin123

**Giảng viên:**
- Email: giangvien1@ictu.edu.vn
- Password: gv123456

---

## Build cho Production

### Backend:
```bash
cd backend
npm start
```

### Frontend:
```bash
cd frontend
npm run build
npm start
```

---

## Troubleshooting

### Lỗi: Cannot connect to MongoDB
**Giải pháp:**
1. Kiểm tra MongoDB đã khởi động: `sudo systemctl status mongod`
2. Kiểm tra MONGODB_URI trong file .env
3. Đảm bảo MongoDB đang chạy trên port 27017

### Lỗi: Port already in use
**Giải pháp:**
1. Thay đổi PORT trong file .env
2. Hoặc stop process đang dùng port đó:
```bash
lsof -ti:5000 | xargs kill -9  # Backend
lsof -ti:3000 | xargs kill -9  # Frontend
```

### Lỗi: Module not found
**Giải pháp:**
```bash
rm -rf node_modules package-lock.json
npm install
```

---

## Cấu trúc Dự án

```
KPI-CNTT/
├── backend/
│   ├── src/
│   │   ├── config/
│   │   ├── controllers/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── routes/
│   │   └── server.js
│   ├── package.json
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── services/
│   │   └── styles/
│   ├── package.json
│   └── next.config.js
├── database/
│   └── seed.js
├── docs/
│   ├── API.md
│   └── DEPLOYMENT.md
└── README.md
```

---

## Bảo trì

### Backup Database
```bash
mongodump --db kpi-ictu --out /path/to/backup
```

### Restore Database
```bash
mongorestore --db kpi-ictu /path/to/backup/kpi-ictu
```

### Xem Logs
```bash
# Backend logs
cd backend
npm run dev

# MongoDB logs
sudo tail -f /var/log/mongodb/mongod.log
```

---

## Liên hệ Hỗ trợ

Nếu gặp vấn đề trong quá trình cài đặt, vui lòng liên hệ:
- Email: support@ictu.edu.vn
- GitHub Issues: https://github.com/Tituslefebvre/KPI-CNTT/issues
