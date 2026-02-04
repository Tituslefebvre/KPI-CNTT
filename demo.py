"""
Script demo để tạo dữ liệu mẫu và kiểm tra hệ thống
Demo script to create sample data and test the system
"""
from app import create_app, db
from app.models import User, Staff, KPICategory, KPIIndicator, Evaluation, EvaluationDetail, EvaluationPeriod
from datetime import datetime

app = create_app()


def demo_create_evaluation():
    """Tạo một đánh giá mẫu với dữ liệu đầy đủ"""
    with app.app_context():
        print("=== Demo: Tạo và hoàn thành một đánh giá KPI ===\n")
        
        # Lấy staff và period
        staff = Staff.query.filter_by(staff_code='VC001').first()
        period = EvaluationPeriod.query.filter_by(is_active=True).first()
        
        if not staff or not period:
            print("❌ Không tìm thấy staff hoặc period. Vui lòng chạy init_db.py trước.")
            return
        
        print(f"📋 Viên chức: {staff.user.full_name} ({staff.staff_code})")
        print(f"📅 Kỳ đánh giá: {period.name}\n")
        
        # Kiểm tra đã có evaluation chưa
        existing = Evaluation.query.filter_by(
            staff_id=staff.id,
            period_id=period.id
        ).first()
        
        if existing:
            evaluation = existing
            print(f"✓ Sử dụng đánh giá có sẵn (ID: {evaluation.id})")
        else:
            # Tạo evaluation mới
            evaluation = Evaluation(
                staff_id=staff.id,
                period_id=period.id,
                status='draft'
            )
            db.session.add(evaluation)
            db.session.commit()
            print(f"✓ Đã tạo đánh giá mới (ID: {evaluation.id})")
            
            # Tạo details cho tất cả indicators
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
            print(f"✓ Đã tạo {len(indicators)} chi tiết đánh giá")
        
        print("\n--- Nhập dữ liệu đánh giá ---\n")
        
        # Nhập dữ liệu mẫu cho từng KPI
        sample_data = {
            'GD-01': {'actual': 220, 'assessment': 'Đã hoàn thành 220 giờ giảng dạy, vượt mục tiêu 10%'},
            'GD-02': {'actual': 4.2, 'assessment': 'Điểm đánh giá của sinh viên đạt 4.2/5.0'},
            'GD-03': {'actual': 6, 'assessment': 'Hướng dẫn 6 đề tài khóa luận tốt nghiệp và NCKH'},
            'NCKH-01': {'actual': 2, 'assessment': 'Công bố 2 bài báo trên tạp chí quốc tế ISI'},
            'NCKH-02': {'actual': 4, 'assessment': 'Công bố 4 bài báo trên tạp chí trong nước'},
            'NCKH-03': {'actual': 1, 'assessment': 'Tham gia 1 đề tài cấp trường'},
            'CT-01': {'actual': 12, 'assessment': 'Tham gia 12 lần họp hội đồng khoa và bộ môn'},
            'CT-02': {'actual': 3, 'assessment': 'Tham gia 3 hoạt động tình nguyện và phục vụ cộng đồng'},
            'CT-03': {'actual': 2, 'assessment': 'Hoàn thành 2 khóa bồi dưỡng về phương pháp giảng dạy'}
        }
        
        for detail in evaluation.details:
            code = detail.indicator.code
            if code in sample_data:
                data = sample_data[code]
                detail.actual_value = data['actual']
                detail.self_assessment = data['assessment']
                
                # Tính điểm
                if detail.indicator.target_value > 0:
                    achievement_rate = detail.actual_value / detail.indicator.target_value
                    detail.score = min(achievement_rate * detail.indicator.max_score, 
                                     detail.indicator.max_score)
                
                print(f"✓ {code}: {detail.actual_value} {detail.indicator.measurement_unit} → {detail.score:.2f} điểm")
        
        # Tính tổng điểm
        evaluation.calculate_total_score()
        evaluation.self_evaluation_date = datetime.utcnow()
        evaluation.status = 'submitted'
        
        db.session.commit()
        
        print(f"\n{'='*60}")
        print(f"🎯 TỔNG ĐIỂM: {evaluation.total_score:.2f} điểm")
        print(f"📊 Trạng thái: {evaluation.status}")
        print(f"{'='*60}\n")
        
        # Hiển thị chi tiết theo danh mục
        print("\n--- Chi tiết theo danh mục ---\n")
        categories = KPICategory.query.all()
        for category in categories:
            cat_score = sum(
                detail.score for detail in evaluation.details 
                if detail.indicator.category_id == category.id
            )
            print(f"📁 {category.name}")
            print(f"   Trọng số: {category.weight}%")
            print(f"   Điểm đạt được: {cat_score:.2f}")
            print()
        
        print("✅ Demo hoàn tất!")
        print(f"\nBạn có thể xem đánh giá này tại: http://localhost:5000/evaluation/{evaluation.id}")
        print("Đăng nhập bằng tài khoản 'admin' hoặc 'staff01' để xem chi tiết.\n")


def show_statistics():
    """Hiển thị thống kê hệ thống"""
    with app.app_context():
        print("=== Thống kê hệ thống ===\n")
        
        total_users = User.query.count()
        total_staff = Staff.query.count()
        total_categories = KPICategory.query.count()
        total_indicators = KPIIndicator.query.count()
        total_periods = EvaluationPeriod.query.count()
        total_evaluations = Evaluation.query.count()
        
        print(f"👥 Người dùng: {total_users}")
        print(f"👔 Viên chức: {total_staff}")
        print(f"📊 Danh mục KPI: {total_categories}")
        print(f"📈 Chỉ số KPI: {total_indicators}")
        print(f"📅 Kỳ đánh giá: {total_periods}")
        print(f"📝 Đánh giá: {total_evaluations}")
        print()
        
        # Thống kê đánh giá theo trạng thái
        draft_count = Evaluation.query.filter_by(status='draft').count()
        submitted_count = Evaluation.query.filter_by(status='submitted').count()
        approved_count = Evaluation.query.filter_by(status='approved').count()
        
        print("Đánh giá theo trạng thái:")
        print(f"  - Nháp: {draft_count}")
        print(f"  - Đã nộp: {submitted_count}")
        print(f"  - Đã phê duyệt: {approved_count}")
        print()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'stats':
        show_statistics()
    else:
        demo_create_evaluation()
        show_statistics()
