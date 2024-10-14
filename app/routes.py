from flask import render_template, request, redirect, url_for, flash, Blueprint
from app import db
from app.models import User, StudentProfile

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/home')
def home_redirect():
    return render_template('home.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users/list.html', users=users)

@main_bp.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        grade = request.form['grade']
        age = request.form['age']
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        new_profile = StudentProfile(user_id=new_user.id, grade=grade, age=age)
        db.session.add(new_profile)
        db.session.commit()
        flash('User created successfully!', 'success')
        return redirect(url_for('main.list_users'))
    return render_template('users/new.html')

@main_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.username = request.form['username']
        user.email = request.form['email']
        user.student_profile.grade = request.form['grade']
        user.student_profile.age = request.form['age']
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.list_users'))
    return render_template('users/edit.html', user=user)

@main_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('main.list_users'))
