# Kiến trúc Hệ thống KPI ICTU

## Tổng quan

Hệ thống KPI ICTU được xây dựng theo kiến trúc 3-tier với việc tách biệt rõ ràng giữa Frontend, Backend và Database.

```
┌─────────────────────────────────────────────────────┐
│                    Client Layer                      │
│  (Next.js/React - Port 3000)                        │
│  - UI Components                                     │
│  - State Management                                  │
│  - API Integration                                   │
└─────────────────┬───────────────────────────────────┘
                  │ HTTP/REST API
                  │ JWT Authentication
┌─────────────────▼───────────────────────────────────┐
│                  Application Layer                   │
│  (Node.js/Express - Port 5000)                      │
│  - RESTful API                                      │
│  - Business Logic                                    │
│  - Authentication & Authorization                    │
│  - Data Validation                                   │
└─────────────────┬───────────────────────────────────┘
                  │ Mongoose ODM
                  │ MongoDB Driver
┌─────────────────▼───────────────────────────────────┐
│                   Data Layer                         │
│  (MongoDB - Port 27017)                             │
│  - Collections: Users, KPIs, DanhGias               │
│  - Indexes & Constraints                            │
│  - Data Persistence                                  │
└─────────────────────────────────────────────────────┘
```

---

## Frontend Architecture (Next.js/React)

### Cấu trúc thư mục
```
frontend/src/
├── pages/              # Next.js pages (routing)
│   ├── index.js       # Login page
│   ├── dashboard.js   # Main dashboard
│   └── _app.js        # App wrapper
├── components/         # Reusable React components
├── services/          # API integration layer
│   └── api.js        # Axios configuration & API calls
├── styles/            # CSS Modules
│   ├── globals.css
│   ├── Login.module.css
│   └── Dashboard.module.css
└── utils/             # Helper functions
```

### Công nghệ sử dụng
- **Next.js 13**: Framework React với SSR/SSG
- **React 18**: UI library
- **Axios**: HTTP client cho API calls
- **CSS Modules**: Scoped styling

### Luồng dữ liệu
```
User Action → Component → API Service → Backend API
                ↓
            State Update
                ↓
            Re-render UI
```

### Authentication Flow
```
1. User enters credentials
   ↓
2. POST /api/auth/login
   ↓
3. Backend validates & returns JWT
   ↓
4. Store token in localStorage
   ↓
5. Add token to all subsequent requests
   ↓
6. Redirect to dashboard
```

---

## Backend Architecture (Node.js/Express)

### Cấu trúc thư mục
```
backend/src/
├── config/
│   └── database.js      # MongoDB connection
├── models/              # Mongoose schemas
│   ├── User.js
│   ├── KPI.js
│   └── DanhGia.js
├── controllers/         # Business logic
│   ├── authController.js
│   ├── kpiController.js
│   └── danhGiaController.js
├── middleware/          # Express middleware
│   └── auth.js         # JWT verification
├── routes/             # API routes
│   ├── authRoutes.js
│   ├── kpiRoutes.js
│   └── danhGiaRoutes.js
└── server.js           # Entry point
```

### Layers Architecture

#### 1. Route Layer
- Định nghĩa endpoints
- Áp dụng middleware
- Phân quyền truy cập

#### 2. Controller Layer
- Xử lý business logic
- Validate input
- Gọi Model layer
- Format response

#### 3. Model Layer
- Định nghĩa schema
- Data validation
- Database operations
- Business rules

#### 4. Middleware Layer
- Authentication
- Authorization
- Error handling
- Request logging

### API Design Pattern

Sử dụng RESTful API với cấu trúc:
```
GET    /api/resource        # Get all
GET    /api/resource/:id    # Get one
POST   /api/resource        # Create
PUT    /api/resource/:id    # Update
DELETE /api/resource/:id    # Delete
```

### Response Format
```json
{
  "success": true/false,
  "data": { ... },
  "message": "Optional message",
  "count": 10  // For list endpoints
}
```

---

## Database Architecture (MongoDB)

### Collections

#### 1. Users Collection
```javascript
{
  _id: ObjectId,
  maNhanVien: String (unique),
  hoTen: String,
  email: String (unique),
  matKhau: String (hashed),
  chucVu: Enum,
  khoa: String,
  boMon: String,
  trangThai: Enum,
  createdAt: Date,
  updatedAt: Date
}
```

#### 2. KPIs Collection
```javascript
{
  _id: ObjectId,
  maKPI: String (unique),
  tenKPI: String,
  moTa: String,
  loaiKPI: Enum,
  donViDo: String,
  chiTieu: Number,
  trongSo: Number,
  namHoc: String,
  trangThai: Enum,
  nguoiTao: ObjectId (ref: User),
  createdAt: Date,
  updatedAt: Date
}
```

#### 3. DanhGias Collection
```javascript
{
  _id: ObjectId,
  maDanhGia: String (unique),
  nhanVien: ObjectId (ref: User),
  kpi: ObjectId (ref: KPI),
  namHoc: String,
  kyDanhGia: Enum,
  ketQuaThucHien: Number,
  diemTuDanhGia: Number,
  diemTruongBoMon: Number,
  diemTruongKhoa: Number,
  diemCuoiCung: Number,
  ghiChu: String,
  trangThai: Enum,
  nguoiDanhGia: Array,
  createdAt: Date,
  updatedAt: Date
}
```

### Relationships

```
User (1) ──────── (N) KPI
  │                    │
  │                    │
  │                    │
  └──── (N) DanhGia ───┘
        (N)          (N)
```

### Indexes
```javascript
// Users
- email: unique
- maNhanVien: unique

// KPIs
- maKPI: unique
- namHoc: indexed
- nguoiTao: indexed

// DanhGias
- maDanhGia: unique
- nhanVien: indexed
- kpi: indexed
- namHoc: indexed
```

---

## Security Architecture

### 1. Authentication
- **JWT (JSON Web Tokens)**
- Token expiry: 30 days
- Stored in localStorage (client)
- Sent in Authorization header

### 2. Password Security
- Hashed using bcrypt (10 rounds)
- Never stored in plain text
- Salt per password

### 3. Authorization
- Role-based access control (RBAC)
- 4 roles: Giảng viên, Trưởng bộ môn, Trưởng khoa, Quản trị viên
- Middleware checks on protected routes

### 4. API Security
```
Request → CORS Check → JWT Verify → Role Check → Controller
```

### 5. Input Validation
- express-validator for request validation
- Mongoose schema validation
- Sanitize user inputs

---

## Deployment Architecture

### Development Environment
```
Developer Machine
├── Frontend (localhost:3000)
├── Backend (localhost:5000)
└── MongoDB (localhost:27017)
```

### Production Environment (Docker)
```
Docker Host
├── Container: Frontend (Nginx + Next.js)
├── Container: Backend (Node.js)
├── Container: MongoDB
└── Network: kpi-network (bridge)
```

### CI/CD Pipeline (Khuyến nghị)
```
GitHub → GitHub Actions → Build → Test → Deploy → Production
```

---

## Performance Considerations

### Backend Optimization
1. **Database Indexing**: Indexes trên các trường thường query
2. **Pagination**: Limit results per page
3. **Caching**: Redis cho session và frequently accessed data
4. **Connection Pooling**: MongoDB connection pool

### Frontend Optimization
1. **Code Splitting**: Next.js automatic code splitting
2. **Lazy Loading**: Components và images
3. **Static Generation**: Pre-render pages khi có thể
4. **API Response Caching**: Cache API responses

---

## Scalability

### Horizontal Scaling
```
Load Balancer
    │
    ├─── Backend Instance 1
    ├─── Backend Instance 2
    └─── Backend Instance 3
           │
           ├─── MongoDB Primary
           └─── MongoDB Replicas
```

### Vertical Scaling
- Tăng resources cho containers
- Upgrade database server

---

## Monitoring & Logging

### Recommended Tools
1. **Application Monitoring**: PM2, New Relic
2. **Database Monitoring**: MongoDB Atlas, Compass
3. **Logs**: Winston, Morgan
4. **Error Tracking**: Sentry

### Health Check Endpoints
```
GET /api/health        # API health
GET /api/db-health     # Database connection
```

---

## Technology Stack Summary

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend | Next.js | 13.x |
| Frontend | React | 18.x |
| Backend | Node.js | 16+ |
| Backend | Express | 4.x |
| Database | MongoDB | 5+ |
| Auth | JWT | 9.x |
| ODM | Mongoose | 7.x |
| Encryption | bcrypt | 2.x |

---

## Future Enhancements

1. **Real-time notifications**: WebSocket/Socket.io
2. **File uploads**: AWS S3/MinIO for attachments
3. **Advanced reporting**: Chart.js, D3.js
4. **Export functionality**: PDF, Excel exports
5. **Email notifications**: SendGrid, Nodemailer
6. **Mobile app**: React Native
7. **API Gateway**: Kong, Express Gateway
8. **Microservices**: Break into smaller services

---

## Liên hệ

Để biết thêm thông tin về kiến trúc hệ thống:
- Email: dev@ictu.edu.vn
- GitHub: https://github.com/Tituslefebvre/KPI-CNTT
