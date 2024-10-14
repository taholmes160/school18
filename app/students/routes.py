from flask import render_template
from app.students import students_bp

@students_bp.route('/')
def index():
    return render_template('students/index.html')