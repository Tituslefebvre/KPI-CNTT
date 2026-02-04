"""
Routes quản lý KPI - KPI management routes
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, KPICategory, KPIIndicator

bp = Blueprint('kpi', __name__, url_prefix='/kpi')


@bp.route('/categories')
@login_required
def categories():
    """Danh sách danh mục KPI"""
    categories = KPICategory.query.all()
    return render_template('kpi/categories.html', categories=categories)


@bp.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create_category():
    """Tạo danh mục KPI mới"""
    if current_user.role not in ['admin', 'manager']:
        flash('Bạn không có quyền thực hiện thao tác này.', 'danger')
        return redirect(url_for('kpi.categories'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        weight = float(request.form.get('weight', 0))
        
        category = KPICategory(
            name=name,
            description=description,
            weight=weight
        )
        
        db.session.add(category)
        db.session.commit()
        
        flash('Tạo danh mục KPI thành công!', 'success')
        return redirect(url_for('kpi.categories'))
    
    return render_template('kpi/create_category.html')


@bp.route('/indicators')
@login_required
def indicators():
    """Danh sách chỉ số KPI"""
    page = request.args.get('page', 1, type=int)
    indicators = KPIIndicator.query.paginate(page=page, per_page=20, error_out=False)
    return render_template('kpi/indicators.html', indicators=indicators)


@bp.route('/indicators/create', methods=['GET', 'POST'])
@login_required
def create_indicator():
    """Tạo chỉ số KPI mới"""
    if current_user.role not in ['admin', 'manager']:
        flash('Bạn không có quyền thực hiện thao tác này.', 'danger')
        return redirect(url_for('kpi.indicators'))
    
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        code = request.form.get('code')
        name = request.form.get('name')
        description = request.form.get('description')
        measurement_unit = request.form.get('measurement_unit')
        weight = float(request.form.get('weight', 0))
        target_value = float(request.form.get('target_value', 0))
        max_score = float(request.form.get('max_score', 100))
        
        # Kiểm tra code đã tồn tại
        if KPIIndicator.query.filter_by(code=code).first():
            flash('Mã chỉ số KPI đã tồn tại.', 'danger')
            categories = KPICategory.query.all()
            return render_template('kpi/create_indicator.html', categories=categories)
        
        indicator = KPIIndicator(
            category_id=category_id,
            code=code,
            name=name,
            description=description,
            measurement_unit=measurement_unit,
            weight=weight,
            target_value=target_value,
            max_score=max_score
        )
        
        db.session.add(indicator)
        db.session.commit()
        
        flash('Tạo chỉ số KPI thành công!', 'success')
        return redirect(url_for('kpi.indicators'))
    
    categories = KPICategory.query.all()
    return render_template('kpi/create_indicator.html', categories=categories)


@bp.route('/indicators/<int:id>')
@login_required
def indicator_detail(id):
    """Chi tiết chỉ số KPI"""
    indicator = KPIIndicator.query.get_or_404(id)
    return render_template('kpi/indicator_detail.html', indicator=indicator)
