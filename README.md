# Hệ thống đánh giá VC-NLĐ thông qua KPIs tại Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU)

## Giới thiệu

Hệ thống quản lý và đánh giá hiệu suất làm việc của Viên chức - Người lao động (VC-NLĐ) thông qua các chỉ số KPI (Key Performance Indicators) tại Trường Đại học Công nghệ Thông tin và Truyền thông.

## Tính năng chính

### Cho Nhân viên / Giảng viên
- Xem danh sách KPI được giao
- Tự đánh giá hiệu suất công việc
- Theo dõi kết quả đánh giá từ cấp trên
- Xem báo cáo thống kê cá nhân

### Cho Trưởng bộ môn
- Đánh giá KPI của giảng viên trong bộ môn
- Xem báo cáo hiệu suất bộ môn
- Đưa ra nhận xét và đề xuất

### Cho Trưởng khoa
- Quản lý và thiết lập KPI cho toàn khoa
- Đánh giá cuối cùng KPI của nhân viên
- Xem báo cáo tổng hợp
- Phê duyệt kết quả đánh giá

### Cho Quản trị viên
- Quản lý người dùng hệ thống
- Thiết lập và quản lý KPI
- Quản lý quy trình đánh giá
- Xem báo cáo toàn trường
- Xuất báo cáo và thống kê

## Kiến trúc hệ thống

### Backend (Node.js/Express)
- **Framework**: Express.js
- **Database**: MongoDB
- **Authentication**: JWT (JSON Web Tokens)
- **API**: RESTful API

### Frontend (Next.js/React)
- **Framework**: Next.js 13
- **UI Library**: React 18
- **HTTP Client**: Axios
- **Styling**: CSS Modules

### Database Schema

#### User (Người dùng)
- Mã nhân viên
- Họ tên
- Email
- Mật khẩu (được mã hóa)
- Chức vụ (Giảng viên, Trưởng bộ môn, Trưởng khoa, Quản trị viên)
- Khoa
- Bộ môn
- Trạng thái

#### KPI
- Mã KPI
- Tên KPI
- Mô tả
- Loại KPI (Giảng dạy, Nghiên cứu khoa học, Phục vụ cộng đồng, Quản lý)
- Đơn vị đo
- Chỉ tiêu
- Trọng số (%)
- Năm học
- Trạng thái

#### DanhGia (Evaluation)
- Mã đánh giá
- Nhân viên
- KPI
- Năm học
- Kỳ đánh giá (Học kỳ 1, Học kỳ 2, Cả năm)
- Kết quả thực hiện
- Điểm tự đánh giá
- Điểm Trưởng bộ môn
- Điểm Trưởng khoa
- Điểm cuối cùng
- Ghi chú
- Trạng thái
- Lịch sử người đánh giá

## Cài đặt và Chạy

### Yêu cầu hệ thống
- Node.js >= 16.x
- MongoDB >= 5.x
- npm hoặc yarn

### Cài đặt Backend

```bash
cd backend
npm install
```

Tạo file `.env` từ `.env.example`:
```bash
cp .env.example .env
```

Cập nhật các biến môi trường trong file `.env`:
```
NODE_ENV=development
PORT=5000
MONGODB_URI=mongodb://localhost:27017/kpi-ictu
JWT_SECRET=your-secret-key
```

Chạy server:
```bash
npm run dev
```

Server sẽ chạy tại `http://localhost:5000`

### Cài đặt Frontend

```bash
cd frontend
npm install
```

Chạy ứng dụng:
```bash
npm run dev
```

Ứng dụng sẽ chạy tại `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Đăng ký tài khoản mới
- `POST /api/auth/login` - Đăng nhập
- `GET /api/auth/me` - Lấy thông tin người dùng hiện tại

### KPI Management
- `GET /api/kpis` - Lấy danh sách KPI
- `GET /api/kpis/:id` - Lấy chi tiết KPI
- `POST /api/kpis` - Tạo KPI mới (Admin, Trưởng khoa)
- `PUT /api/kpis/:id` - Cập nhật KPI (Admin, Trưởng khoa)
- `DELETE /api/kpis/:id` - Xóa KPI (Admin)

### Evaluation Management
- `GET /api/evaluations` - Lấy danh sách đánh giá
- `GET /api/evaluations/:id` - Lấy chi tiết đánh giá
- `POST /api/evaluations` - Tạo đánh giá mới (Admin, Trưởng khoa)
- `PUT /api/evaluations/:id/self` - Tự đánh giá
- `PUT /api/evaluations/:id/manager` - Đánh giá của quản lý (Trưởng bộ môn, Trưởng khoa)
- `DELETE /api/evaluations/:id` - Xóa đánh giá (Admin)

## Quy trình đánh giá

1. **Thiết lập KPI**: Trưởng khoa/Admin thiết lập KPI cho năm học mới
2. **Phân công**: Gán KPI cho từng nhân viên
3. **Tự đánh giá**: Nhân viên tự đánh giá hiệu suất công việc
4. **Đánh giá Trưởng bộ môn**: Trưởng bộ môn đánh giá và cho điểm
5. **Đánh giá Trưởng khoa**: Trưởng khoa đánh giá cuối cùng và cho điểm chính thức
6. **Hoàn thành**: Kết quả được lưu và tạo báo cáo

## Bảo mật

- Mật khẩu được mã hóa bằng bcrypt
- Xác thực bằng JWT tokens
- Phân quyền theo vai trò (Role-based access control)
- Bảo vệ các route API với middleware authentication

## Phát triển

### Cấu trúc thư mục Backend
```
backend/
├── src/
│   ├── config/         # Cấu hình database
│   ├── controllers/    # Controllers xử lý logic
│   ├── middleware/     # Middleware (auth, validation)
│   ├── models/         # Database models
│   ├── routes/         # API routes
│   └── server.js       # Entry point
├── package.json
└── .env.example
```

### Cấu trúc thư mục Frontend
```
frontend/
├── src/
│   ├── components/     # React components
│   ├── pages/          # Next.js pages
│   ├── services/       # API services
│   ├── styles/         # CSS modules
│   └── utils/          # Utility functions
├── package.json
└── next.config.js
```

## Đóng góp

Mọi đóng góp đều được chào đón. Vui lòng tạo Pull Request hoặc Issue để thảo luận về các thay đổi bạn muốn thực hiện.

## Giấy phép

MIT License

## Liên hệ

Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU)

---

© 2024 ICTU - Hệ thống đánh giá KPI