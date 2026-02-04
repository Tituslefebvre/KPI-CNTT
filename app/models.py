"""
Models cho hệ thống KPI
Database models for KPI evaluation system
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """Mô hình người dùng - User model"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='staff')  # staff, manager, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Quan hệ với bảng Staff
    staff_profile = db.relationship('Staff', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Mã hóa mật khẩu"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Kiểm tra mật khẩu"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'


class Staff(db.Model):
    """Mô hình Viên chức/Nhân lực đào tạo - Staff/Personnel model"""
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    staff_code = db.Column(db.String(20), unique=True, nullable=False)
    department = db.Column(db.String(200), nullable=False)  # Khoa/Phòng ban
    position = db.Column(db.String(100), nullable=False)  # Chức vụ
    academic_rank = db.Column(db.String(100))  # Học hàm (PGS, GS)
    degree = db.Column(db.String(100))  # Học vị (ThS, TS)
    phone = db.Column(db.String(20))
    join_date = db.Column(db.Date)
    
    # Quan hệ với bảng Evaluation
    evaluations = db.relationship('Evaluation', backref='staff', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Staff {self.staff_code}>'


class KPICategory(db.Model):
    """Mô hình danh mục KPI - KPI Category model"""
    __tablename__ = 'kpi_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    weight = db.Column(db.Float, default=0)  # Trọng số (%)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Quan hệ với bảng KPIIndicator
    indicators = db.relationship('KPIIndicator', backref='category', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<KPICategory {self.name}>'


class KPIIndicator(db.Model):
    """Mô hình chỉ số KPI - KPI Indicator model"""
    __tablename__ = 'kpi_indicators'
    
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('kpi_categories.id'), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    measurement_unit = db.Column(db.String(50))  # Đơn vị đo
    weight = db.Column(db.Float, default=0)  # Trọng số trong danh mục (%)
    target_value = db.Column(db.Float)  # Giá trị mục tiêu
    max_score = db.Column(db.Float, default=100)  # Điểm tối đa
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Quan hệ với bảng EvaluationDetail
    evaluation_details = db.relationship('EvaluationDetail', backref='indicator', lazy=True)
    
    def __repr__(self):
        return f'<KPIIndicator {self.code}>'


class EvaluationPeriod(db.Model):
    """Mô hình kỳ đánh giá - Evaluation Period model"""
    __tablename__ = 'evaluation_periods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)  # VD: "Học kỳ 1 năm 2024"
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Quan hệ với bảng Evaluation
    evaluations = db.relationship('Evaluation', backref='period', lazy=True)
    
    def __repr__(self):
        return f'<EvaluationPeriod {self.name}>'


class Evaluation(db.Model):
    """Mô hình đánh giá - Evaluation model"""
    __tablename__ = 'evaluations'
    
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    period_id = db.Column(db.Integer, db.ForeignKey('evaluation_periods.id'), nullable=False)
    total_score = db.Column(db.Float, default=0)
    status = db.Column(db.String(20), default='draft')  # draft, submitted, approved
    self_evaluation_date = db.Column(db.DateTime)
    manager_evaluation_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Quan hệ với bảng EvaluationDetail
    details = db.relationship('EvaluationDetail', backref='evaluation', lazy=True, cascade='all, delete-orphan')
    
    def calculate_total_score(self):
        """Tính tổng điểm đánh giá"""
        total = sum(detail.score for detail in self.details if detail.score)
        self.total_score = total
        return total
    
    def __repr__(self):
        return f'<Evaluation {self.id} - Staff {self.staff_id}>'


class EvaluationDetail(db.Model):
    """Mô hình chi tiết đánh giá - Evaluation Detail model"""
    __tablename__ = 'evaluation_details'
    
    id = db.Column(db.Integer, primary_key=True)
    evaluation_id = db.Column(db.Integer, db.ForeignKey('evaluations.id'), nullable=False)
    indicator_id = db.Column(db.Integer, db.ForeignKey('kpi_indicators.id'), nullable=False)
    actual_value = db.Column(db.Float)  # Giá trị thực tế đạt được
    score = db.Column(db.Float)  # Điểm số
    self_assessment = db.Column(db.Text)  # Tự đánh giá
    manager_comment = db.Column(db.Text)  # Nhận xét của quản lý
    evidence = db.Column(db.String(500))  # Đường dẫn file minh chứng
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<EvaluationDetail {self.id}>'
