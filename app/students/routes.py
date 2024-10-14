from flask import render_template
from flask_login import login_required
from app import db
from app.models import User
from app.students import students_bp

@students_bp.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('students/users.html', users=users)