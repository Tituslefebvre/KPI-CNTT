# Tài liệu Kiến trúc Hệ thống KPI

## Tổng quan

Hệ thống Đánh giá KPI cho Viên chức - Nhân lực đào tạo là một ứng dụng web được xây dựng bằng Python Flask, giúp quản lý và đánh giá hiệu suất làm việc của viên chức tại Trường Đại học Công nghệ Thông tin và Truyền thông.

## Kiến trúc hệ thống

### 1. Kiến trúc tổng thể

```
┌─────────────────────────────────────────────────────────────┐
│                    Trình duyệt Web                          │
│                    (Bootstrap 5 UI)                         │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/HTTPS
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Flask Application                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Routes/Controllers                       │  │
│  │  • auth.py    - Xác thực người dùng                  │  │
│  │  • main.py    - Trang chủ và dashboard              │  │
│  │  • staff.py   - Quản lý viên chức                    │  │
│  │  • kpi.py     - Quản lý KPI                          │  │
│  │  • evaluation.py - Quản lý đánh giá                  │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Business Logic                           │  │
│  │  • models.py  - Mô hình dữ liệu                      │  │
│  │  • Tính điểm tự động                                 │  │
│  │  • Phân quyền người dùng                             │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │ SQLAlchemy ORM
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Database Layer                            │
│                   (SQLite/PostgreSQL)                       │
│  • users, staff, kpi_categories, kpi_indicators            │
│  • evaluation_periods, evaluations, evaluation_details     │
└─────────────────────────────────────────────────────────────┘
```

### 2. Mô hình dữ liệu (Database Schema)

#### 2.1. User & Staff
```python
User (users)
├── id (PK)
├── username (unique)
├── email (unique)
├── password_hash
├── full_name
├── role (admin/manager/staff)
└── created_at

Staff (staff)
├── id (PK)
├── user_id (FK -> users.id)
├── staff_code (unique)
├── department
├── position
├── academic_rank
├── degree
├── phone
└── join_date
```

#### 2.2. KPI Structure
```python
KPICategory (kpi_categories)
├── id (PK)
├── name
├── description
├── weight (%)
└── created_at

KPIIndicator (kpi_indicators)
├── id (PK)
├── category_id (FK -> kpi_categories.id)
├── code (unique)
├── name
├── description
├── measurement_unit
├── weight (%)
├── target_value
├── max_score
└── created_at
```

#### 2.3. Evaluation System
```python
EvaluationPeriod (evaluation_periods)
├── id (PK)
├── name
├── start_date
├── end_date
├── is_active
└── created_at

Evaluation (evaluations)
├── id (PK)
├── staff_id (FK -> staff.id)
├── period_id (FK -> evaluation_periods.id)
├── total_score
├── status (draft/submitted/approved)
├── self_evaluation_date
├── manager_evaluation_date
├── created_at
└── updated_at

EvaluationDetail (evaluation_details)
├── id (PK)
├── evaluation_id (FK -> evaluations.id)
├── indicator_id (FK -> kpi_indicators.id)
├── actual_value
├── score
├── self_assessment
├── manager_comment
├── evidence
└── created_at
```

### 3. Quy trình nghiệp vụ

#### 3.1. Quy trình đánh giá KPI

```
1. Chuẩn bị
   ├── Admin/Manager tạo KPI Categories
   ├── Admin/Manager tạo KPI Indicators
   └── Admin/Manager tạo Evaluation Period

2. Tạo đánh giá
   ├── Manager tạo Evaluation cho Staff
   └── Hệ thống tạo EvaluationDetail cho từng KPI Indicator

3. Tự đánh giá
   ├── Staff đăng nhập
   ├── Staff nhập giá trị thực tế cho từng KPI
   ├── Staff viết tự đánh giá
   ├── Hệ thống tính điểm tự động
   │   Score = (actual_value / target_value) * max_score
   │   (Không vượt quá max_score)
   └── Staff nộp đánh giá (status: draft -> submitted)

4. Phê duyệt
   ├── Manager xem danh sách đánh giá đã nộp
   ├── Manager xem chi tiết và nhận xét
   └── Manager phê duyệt (status: submitted -> approved)

5. Báo cáo
   └── Xem tổng hợp kết quả đánh giá
```

#### 3.2. Công thức tính điểm

```python
# Công thức cơ bản
achievement_rate = actual_value / target_value
score = min(achievement_rate * max_score, max_score)

# Ví dụ:
# KPI: Số bài báo quốc tế
# - target_value = 2 (bài)
# - max_score = 60 (điểm)
# - actual_value = 3 (bài)
# 
# achievement_rate = 3 / 2 = 1.5 (150%)
# score = min(1.5 * 60, 60) = 60 (điểm)

# Tổng điểm đánh giá
total_score = sum(detail.score for detail in evaluation.details)
```

### 4. Phân quyền người dùng

| Role    | Quyền hạn                                                      |
|---------|----------------------------------------------------------------|
| Admin   | - Tất cả quyền của Manager<br>- Quản lý người dùng<br>- Cấu hình hệ thống |
| Manager | - Tạo/Sửa KPI Categories và Indicators<br>- Tạo Evaluation Periods<br>- Tạo đánh giá cho Staff<br>- Phê duyệt đánh giá<br>- Xem tất cả đánh giá |
| Staff   | - Tự đánh giá<br>- Xem đánh giá của mình<br>- Xem thông tin cá nhân |

### 5. API Endpoints

#### Authentication
```
GET  /auth/login         - Hiển thị form đăng nhập
POST /auth/login         - Xử lý đăng nhập
GET  /auth/logout        - Đăng xuất
GET  /auth/register      - Hiển thị form đăng ký
POST /auth/register      - Xử lý đăng ký
```

#### Main
```
GET  /                   - Dashboard trang chủ
GET  /dashboard          - Dashboard chi tiết
```

#### Staff Management
```
GET  /staff/                    - Danh sách viên chức
GET  /staff/<id>                - Chi tiết viên chức
GET  /staff/create              - Form tạo viên chức
POST /staff/create              - Xử lý tạo viên chức
GET  /staff/<id>/edit           - Form sửa viên chức
POST /staff/<id>/edit           - Xử lý sửa viên chức
```

#### KPI Management
```
GET  /kpi/categories            - Danh sách danh mục KPI
GET  /kpi/categories/create     - Form tạo danh mục
POST /kpi/categories/create     - Xử lý tạo danh mục
GET  /kpi/indicators            - Danh sách chỉ số KPI
GET  /kpi/indicators/create     - Form tạo chỉ số
POST /kpi/indicators/create     - Xử lý tạo chỉ số
GET  /kpi/indicators/<id>       - Chi tiết chỉ số
```

#### Evaluation Management
```
GET  /evaluation/periods        - Danh sách kỳ đánh giá
GET  /evaluation/periods/create - Form tạo kỳ đánh giá
POST /evaluation/periods/create - Xử lý tạo kỳ đánh giá
GET  /evaluation/list           - Danh sách đánh giá
GET  /evaluation/create         - Form tạo đánh giá
POST /evaluation/create         - Xử lý tạo đánh giá
GET  /evaluation/<id>           - Chi tiết đánh giá
GET  /evaluation/<id>/edit      - Form sửa đánh giá
POST /evaluation/<id>/edit      - Xử lý sửa đánh giá
POST /evaluation/<id>/approve   - Phê duyệt đánh giá
```

### 6. Công nghệ và thư viện

| Thành phần | Công nghệ/Thư viện | Phiên bản |
|------------|-------------------|-----------|
| Backend Framework | Flask | 3.0.0 |
| Database ORM | SQLAlchemy | 2.0+ |
| Authentication | Flask-Login | 0.6.3 |
| Form Handling | Flask-WTF | 1.2.1 |
| Database Migration | Flask-Migrate | 4.0.5 |
| Frontend Framework | Bootstrap | 5.3.0 |
| Icons | Bootstrap Icons | 1.10.0 |
| Database | SQLite (dev)<br>PostgreSQL (prod) | - |

### 7. Bảo mật

#### 7.1. Xác thực và phiên làm việc
- Mật khẩu được mã hóa bằng `werkzeug.security.generate_password_hash`
- Sử dụng Flask-Login cho quản lý session
- Session timeout: 8 giờ
- CSRF protection với Flask-WTF

#### 7.2. Phân quyền
- Kiểm tra quyền trước khi thực hiện các thao tác nhạy cảm
- Staff chỉ có thể xem/sửa đánh giá của mình
- Manager/Admin có quyền quản lý toàn bộ

#### 7.3. Bảo mật dữ liệu
- SQL injection prevention qua SQLAlchemy ORM
- XSS protection qua Jinja2 auto-escaping
- Secret key cho session encryption

### 8. Khả năng mở rộng

#### 8.1. Tính năng có thể thêm
- Xuất báo cáo Excel/PDF
- Dashboard analytics với biểu đồ
- Email notification
- File upload cho minh chứng
- API REST cho mobile app
- Multi-language support
- Advanced reporting và analytics
- Integration với hệ thống nhân sự

#### 8.2. Scale infrastructure
- Chuyển từ SQLite sang PostgreSQL
- Thêm Redis cho session storage
- Load balancing với Nginx
- Docker containerization
- Cloud deployment (AWS/GCP/Azure)

### 9. Deployment

#### 9.1. Development
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python init_db.py
python run.py
```

#### 9.2. Production (với Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

#### 9.3. Production (với Nginx)
```nginx
server {
    listen 80;
    server_name kpi.cntt.edu.vn;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static {
        alias /path/to/app/static;
    }
}
```

### 10. Maintenance

#### 10.1. Database Backup
```bash
# SQLite
cp kpi_system.db kpi_system_backup_$(date +%Y%m%d).db

# PostgreSQL
pg_dump kpi_db > kpi_backup_$(date +%Y%m%d).sql
```

#### 10.2. Logs
```python
# Thêm logging trong config.py
import logging
logging.basicConfig(
    filename='kpi_system.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
```

#### 10.3. Monitoring
- Sử dụng Flask-Monitor để theo dõi performance
- Setup health check endpoint
- Monitor database size và performance

## Liên hệ và hỗ trợ

Để được hỗ trợ hoặc báo lỗi, vui lòng tạo issue trên GitHub repository.
