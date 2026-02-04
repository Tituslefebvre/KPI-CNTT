"""
Routes chính - Main routes
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Staff, Evaluation, KPICategory, EvaluationPeriod

bp = Blueprint('main', __name__)


@bp.route('/')
@login_required
def index():
    """Trang chủ - Dashboard"""
    # Lấy thông tin cơ bản
    total_staff = Staff.query.count()
    total_categories = KPICategory.query.count()
    active_periods = EvaluationPeriod.query.filter_by(is_active=True).count()
    
    # Lấy đánh giá gần nhất của user hiện tại
    recent_evaluations = []
    if current_user.staff_profile:
        recent_evaluations = Evaluation.query.filter_by(
            staff_id=current_user.staff_profile.id
        ).order_by(Evaluation.created_at.desc()).limit(5).all()
    
    return render_template('index.html',
                         total_staff=total_staff,
                         total_categories=total_categories,
                         active_periods=active_periods,
                         recent_evaluations=recent_evaluations)


@bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard chi tiết"""
    return render_template('dashboard.html')
