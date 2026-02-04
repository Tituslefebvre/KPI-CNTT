"""
Script khởi tạo dữ liệu mẫu cho hệ thống KPI
Initialize sample data for KPI system
"""
from datetime import datetime, date
from app import create_app, db
from app.models import User, Staff, KPICategory, KPIIndicator, EvaluationPeriod

app = create_app()


def init_db():
    """Khởi tạo database và dữ liệu mẫu"""
    with app.app_context():
        # Tạo tất cả các bảng
        db.create_all()
        print("✓ Đã tạo các bảng database")
        
        # Kiểm tra xem đã có dữ liệu chưa
        if User.query.first():
            print("! Database đã có dữ liệu, bỏ qua khởi tạo")
            return
        
        # Tạo user admin
        admin = User(
            username='admin',
            email='admin@cntt.edu.vn',
            full_name='Quản trị viên',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Tạo user manager
        manager = User(
            username='manager',
            email='manager@cntt.edu.vn',
            full_name='Trưởng phòng Đào tạo',
            role='manager'
        )
        manager.set_password('manager123')
        db.session.add(manager)
        
        # Tạo user staff
        staff_user = User(
            username='staff01',
            email='staff01@cntt.edu.vn',
            full_name='Nguyễn Văn A',
            role='staff'
        )
        staff_user.set_password('staff123')
        db.session.add(staff_user)
        
        db.session.commit()
        print("✓ Đã tạo 3 user mẫu")
        
        # Tạo staff profile
        staff1 = Staff(
            user_id=staff_user.id,
            staff_code='VC001',
            department='Khoa Công nghệ Phần mềm',
            position='Giảng viên',
            degree='Tiến sĩ',
            phone='0123456789',
            join_date=date(2020, 1, 15)
        )
        db.session.add(staff1)
        
        staff2 = Staff(
            user_id=manager.id,
            staff_code='VC002',
            department='Phòng Đào tạo',
            position='Trưởng phòng',
            academic_rank='Phó Giáo sư',
            degree='Tiến sĩ',
            phone='0987654321',
            join_date=date(2015, 8, 1)
        )
        db.session.add(staff2)
        
        db.session.commit()
        print("✓ Đã tạo 2 hồ sơ viên chức mẫu")
        
        # Tạo danh mục KPI
        cat1 = KPICategory(
            name='Giảng dạy',
            description='Các chỉ số liên quan đến hoạt động giảng dạy',
            weight=40.0
        )
        db.session.add(cat1)
        
        cat2 = KPICategory(
            name='Nghiên cứu khoa học',
            description='Các chỉ số liên quan đến nghiên cứu khoa học',
            weight=35.0
        )
        db.session.add(cat2)
        
        cat3 = KPICategory(
            name='Công tác khác',
            description='Các hoạt động công tác khác',
            weight=25.0
        )
        db.session.add(cat3)
        
        db.session.commit()
        print("✓ Đã tạo 3 danh mục KPI")
        
        # Tạo chỉ số KPI cho Giảng dạy
        kpi1 = KPIIndicator(
            category_id=cat1.id,
            code='GD-01',
            name='Số giờ giảng dạy chuẩn',
            description='Số giờ giảng dạy theo quy định',
            measurement_unit='giờ',
            weight=50.0,
            target_value=200.0,
            max_score=50.0
        )
        db.session.add(kpi1)
        
        kpi2 = KPIIndicator(
            category_id=cat1.id,
            code='GD-02',
            name='Điểm đánh giá của sinh viên',
            description='Điểm trung bình đánh giá giảng viên của sinh viên',
            measurement_unit='điểm',
            weight=30.0,
            target_value=4.0,
            max_score=30.0
        )
        db.session.add(kpi2)
        
        kpi3 = KPIIndicator(
            category_id=cat1.id,
            code='GD-03',
            name='Số đề tài hướng dẫn',
            description='Số lượng đề tài NCKH, khóa luận hướng dẫn',
            measurement_unit='đề tài',
            weight=20.0,
            target_value=5.0,
            max_score=20.0
        )
        db.session.add(kpi3)
        
        # Tạo chỉ số KPI cho Nghiên cứu khoa học
        kpi4 = KPIIndicator(
            category_id=cat2.id,
            code='NCKH-01',
            name='Số bài báo quốc tế',
            description='Số bài báo đăng trên tạp chí quốc tế',
            measurement_unit='bài',
            weight=60.0,
            target_value=2.0,
            max_score=60.0
        )
        db.session.add(kpi4)
        
        kpi5 = KPIIndicator(
            category_id=cat2.id,
            code='NCKH-02',
            name='Số bài báo trong nước',
            description='Số bài báo đăng trên tạp chí trong nước',
            measurement_unit='bài',
            weight=25.0,
            target_value=3.0,
            max_score=25.0
        )
        db.session.add(kpi5)
        
        kpi6 = KPIIndicator(
            category_id=cat2.id,
            code='NCKH-03',
            name='Số đề tài nghiên cứu',
            description='Số đề tài nghiên cứu chủ trì/tham gia',
            measurement_unit='đề tài',
            weight=15.0,
            target_value=1.0,
            max_score=15.0
        )
        db.session.add(kpi6)
        
        # Tạo chỉ số KPI cho Công tác khác
        kpi7 = KPIIndicator(
            category_id=cat3.id,
            code='CT-01',
            name='Tham gia hội đồng/ban',
            description='Tham gia các hội đồng, ban chuyên môn',
            measurement_unit='lần',
            weight=40.0,
            target_value=10.0,
            max_score=40.0
        )
        db.session.add(kpi7)
        
        kpi8 = KPIIndicator(
            category_id=cat3.id,
            code='CT-02',
            name='Hoạt động phục vụ cộng đồng',
            description='Các hoạt động phục vụ cộng đồng, xã hội',
            measurement_unit='hoạt động',
            weight=30.0,
            target_value=3.0,
            max_score=30.0
        )
        db.session.add(kpi8)
        
        kpi9 = KPIIndicator(
            category_id=cat3.id,
            code='CT-03',
            name='Bồi dưỡng chuyên môn',
            description='Tham gia các khóa bồi dưỡng, nâng cao trình độ',
            measurement_unit='khóa',
            weight=30.0,
            target_value=2.0,
            max_score=30.0
        )
        db.session.add(kpi9)
        
        db.session.commit()
        print("✓ Đã tạo 9 chỉ số KPI")
        
        # Tạo kỳ đánh giá
        period1 = EvaluationPeriod(
            name='Học kỳ 1 năm học 2024-2025',
            start_date=date(2024, 9, 1),
            end_date=date(2025, 1, 31),
            is_active=True
        )
        db.session.add(period1)
        
        period2 = EvaluationPeriod(
            name='Học kỳ 2 năm học 2024-2025',
            start_date=date(2025, 2, 1),
            end_date=date(2025, 6, 30),
            is_active=False
        )
        db.session.add(period2)
        
        db.session.commit()
        print("✓ Đã tạo 2 kỳ đánh giá")
        
        print("\n=== Khởi tạo dữ liệu hoàn tất ===")
        print("\nThông tin đăng nhập:")
        print("- Admin: username='admin', password='admin123'")
        print("- Manager: username='manager', password='manager123'")
        print("- Staff: username='staff01', password='staff123'")


if __name__ == '__main__':
    init_db()
