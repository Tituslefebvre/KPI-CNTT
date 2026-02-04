"""
Cấu hình ứng dụng Flask cho hệ thống KPI
Configuration for KPI evaluation system
"""
import os
from datetime import timedelta

class Config:
    """Cấu hình cơ bản cho ứng dụng"""
    
    # Secret key cho Flask session
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Cấu hình database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///kpi_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Cấu hình session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=8)
    
    # Cấu hình upload
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
