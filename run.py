"""
Entry point cho ứng dụng KPI
Application entry point
"""
from app import create_app, db
from app.models import User, Staff, KPICategory, KPIIndicator, Evaluation, EvaluationPeriod, EvaluationDetail

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Tạo context cho Flask shell"""
    return {
        'db': db,
        'User': User,
        'Staff': Staff,
        'KPICategory': KPICategory,
        'KPIIndicator': KPIIndicator,
        'Evaluation': Evaluation,
        'EvaluationPeriod': EvaluationPeriod,
        'EvaluationDetail': EvaluationDetail
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
