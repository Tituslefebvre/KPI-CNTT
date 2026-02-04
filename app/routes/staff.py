"""
Routes quản lý viên chức - Staff management routes
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Staff, User
from datetime import datetime

bp = Blueprint('staff', __name__, url_prefix='/staff')


@bp.route('/')
@login_required
def list():
    """Danh sách viên chức"""
    page = request.args.get('page', 1, type=int)
    staff_list = Staff.query.paginate(page=page, per_page=20, error_out=False)
    return render_template('staff/list.html', staff_list=staff_list)


@bp.route('/<int:id>')
@login_required
def detail(id):
    """Chi tiết viên chức"""
    staff = Staff.query.get_or_404(id)
    return render_template('staff/detail.html', staff=staff)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Tạo hồ sơ viên chức mới"""
    if current_user.role not in ['admin', 'manager']:
        flash('Bạn không có quyền thực hiện thao tác này.', 'danger')
        return redirect(url_for('staff.list'))
    
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        staff_code = request.form.get('staff_code')
        department = request.form.get('department')
        position = request.form.get('position')
        academic_rank = request.form.get('academic_rank')
        degree = request.form.get('degree')
        phone = request.form.get('phone')
        join_date_str = request.form.get('join_date')
        
        # Kiểm tra staff_code đã tồn tại
        if Staff.query.filter_by(staff_code=staff_code).first():
            flash('Mã viên chức đã tồn tại.', 'danger')
            return render_template('staff/create.html', users=User.query.all())
        
        # Chuyển đổi ngày
        join_date = None
        if join_date_str:
            try:
                join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass
        
        staff = Staff(
            user_id=user_id,
            staff_code=staff_code,
            department=department,
            position=position,
            academic_rank=academic_rank,
            degree=degree,
            phone=phone,
            join_date=join_date
        )
        
        db.session.add(staff)
        db.session.commit()
        
        flash('Tạo hồ sơ viên chức thành công!', 'success')
        return redirect(url_for('staff.detail', id=staff.id))
    
    users = User.query.all()
    return render_template('staff/create.html', users=users)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Chỉnh sửa thông tin viên chức"""
    staff = Staff.query.get_or_404(id)
    
    if current_user.role not in ['admin', 'manager']:
        flash('Bạn không có quyền thực hiện thao tác này.', 'danger')
        return redirect(url_for('staff.detail', id=id))
    
    if request.method == 'POST':
        staff.department = request.form.get('department')
        staff.position = request.form.get('position')
        staff.academic_rank = request.form.get('academic_rank')
        staff.degree = request.form.get('degree')
        staff.phone = request.form.get('phone')
        
        join_date_str = request.form.get('join_date')
        if join_date_str:
            try:
                staff.join_date = datetime.strptime(join_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass
        
        db.session.commit()
        flash('Cập nhật thông tin thành công!', 'success')
        return redirect(url_for('staff.detail', id=id))
    
    return render_template('staff/edit.html', staff=staff)
