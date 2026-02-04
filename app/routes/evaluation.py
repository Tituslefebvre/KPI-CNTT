"""
Routes đánh giá - Evaluation routes
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Evaluation, EvaluationDetail, EvaluationPeriod, KPIIndicator, Staff
from datetime import datetime

bp = Blueprint('evaluation', __name__, url_prefix='/evaluation')


@bp.route('/periods')
@login_required
def periods():
    """Danh sách kỳ đánh giá"""
    periods = EvaluationPeriod.query.order_by(EvaluationPeriod.start_date.desc()).all()
    return render_template('evaluation/periods.html', periods=periods)


@bp.route('/periods/create', methods=['GET', 'POST'])
@login_required
def create_period():
    """Tạo kỳ đánh giá mới"""
    if current_user.role not in ['admin', 'manager']:
        flash('Bạn không có quyền thực hiện thao tác này.', 'danger')
        return redirect(url_for('evaluation.periods'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        period = EvaluationPeriod(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_active=True
        )
        
        db.session.add(period)
        db.session.commit()
        
        flash('Tạo kỳ đánh giá thành công!', 'success')
        return redirect(url_for('evaluation.periods'))
    
    return render_template('evaluation/create_period.html')


@bp.route('/list')
@login_required
def list():
    """Danh sách đánh giá"""
    page = request.args.get('page', 1, type=int)
    
    if current_user.role in ['admin', 'manager']:
        # Admin và manager xem tất cả đánh giá
        evaluations = Evaluation.query.paginate(page=page, per_page=20, error_out=False)
    else:
        # Staff chỉ xem đánh giá của mình
        if current_user.staff_profile:
            evaluations = Evaluation.query.filter_by(
                staff_id=current_user.staff_profile.id
            ).paginate(page=page, per_page=20, error_out=False)
        else:
            evaluations = []
    
    return render_template('evaluation/list.html', evaluations=evaluations)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Tạo đánh giá mới"""
    if request.method == 'POST':
        period_id = request.form.get('period_id')
        staff_id = request.form.get('staff_id')
        
        # Kiểm tra đã có đánh giá trong kỳ này chưa
        existing = Evaluation.query.filter_by(
            staff_id=staff_id,
            period_id=period_id
        ).first()
        
        if existing:
            flash('Đã tồn tại đánh giá cho viên chức này trong kỳ đánh giá này.', 'warning')
            return redirect(url_for('evaluation.detail', id=existing.id))
        
        evaluation = Evaluation(
            staff_id=staff_id,
            period_id=period_id,
            status='draft'
        )
        
        db.session.add(evaluation)
        db.session.commit()
        
        # Tạo chi tiết đánh giá cho tất cả các KPI indicators
        indicators = KPIIndicator.query.all()
        for indicator in indicators:
            detail = EvaluationDetail(
                evaluation_id=evaluation.id,
                indicator_id=indicator.id,
                actual_value=0,
                score=0
            )
            db.session.add(detail)
        
        db.session.commit()
        
        flash('Tạo đánh giá thành công!', 'success')
        return redirect(url_for('evaluation.detail', id=evaluation.id))
    
    periods = EvaluationPeriod.query.filter_by(is_active=True).all()
    staff_list = Staff.query.all()
    return render_template('evaluation/create.html', periods=periods, staff_list=staff_list)


@bp.route('/<int:id>')
@login_required
def detail(id):
    """Chi tiết đánh giá"""
    evaluation = Evaluation.query.get_or_404(id)
    
    # Kiểm tra quyền truy cập
    if current_user.role not in ['admin', 'manager']:
        if not current_user.staff_profile or current_user.staff_profile.id != evaluation.staff_id:
            flash('Bạn không có quyền xem đánh giá này.', 'danger')
            return redirect(url_for('evaluation.list'))
    
    return render_template('evaluation/detail.html', evaluation=evaluation)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Chỉnh sửa đánh giá"""
    evaluation = Evaluation.query.get_or_404(id)
    
    # Kiểm tra quyền
    if current_user.role not in ['admin', 'manager']:
        if not current_user.staff_profile or current_user.staff_profile.id != evaluation.staff_id:
            flash('Bạn không có quyền chỉnh sửa đánh giá này.', 'danger')
            return redirect(url_for('evaluation.list'))
    
    if request.method == 'POST':
        # Cập nhật các chi tiết đánh giá
        for detail in evaluation.details:
            actual_value = request.form.get(f'actual_value_{detail.id}')
            self_assessment = request.form.get(f'self_assessment_{detail.id}')
            
            if actual_value:
                detail.actual_value = float(actual_value)
                # Tính điểm dựa trên giá trị thực tế và mục tiêu
                if detail.indicator.target_value > 0:
                    achievement_rate = detail.actual_value / detail.indicator.target_value
                    detail.score = min(achievement_rate * detail.indicator.max_score, detail.indicator.max_score)
                else:
                    detail.score = 0
            
            if self_assessment:
                detail.self_assessment = self_assessment
        
        # Tính tổng điểm
        evaluation.calculate_total_score()
        evaluation.self_evaluation_date = datetime.utcnow()
        evaluation.status = 'submitted'
        
        db.session.commit()
        
        flash('Cập nhật đánh giá thành công!', 'success')
        return redirect(url_for('evaluation.detail', id=id))
    
    return render_template('evaluation/edit.html', evaluation=evaluation)


@bp.route('/<int:id>/approve', methods=['POST'])
@login_required
def approve(id):
    """Phê duyệt đánh giá"""
    if current_user.role not in ['admin', 'manager']:
        return jsonify({'success': False, 'message': 'Bạn không có quyền phê duyệt.'}), 403
    
    evaluation = Evaluation.query.get_or_404(id)
    evaluation.status = 'approved'
    evaluation.manager_evaluation_date = datetime.utcnow()
    
    db.session.commit()
    
    flash('Phê duyệt đánh giá thành công!', 'success')
    return redirect(url_for('evaluation.detail', id=id))
