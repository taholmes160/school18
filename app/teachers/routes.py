from flask import render_template
from app.teachers import teachers_bp

@teachers_bp.route('/')
def index():
    return render_template('teachers/index.html')