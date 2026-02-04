"""
Khởi tạo ứng dụng Flask
Flask application initialization
"""
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from app.models import db, User

login_manager = LoginManager()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    """Tải thông tin người dùng cho Flask-Login"""
    return User.query.get(int(user_id))


def create_app(config_class=Config):
    """Factory function để tạo và cấu hình ứng dụng Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Khởi tạo extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Vui lòng đăng nhập để truy cập trang này.'
    migrate.init_app(app, db)
    
    # Đăng ký blueprints
    from app.routes import auth, main, staff, kpi, evaluation
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(staff.bp)
    app.register_blueprint(kpi.bp)
    app.register_blueprint(evaluation.bp)
    
    return app
