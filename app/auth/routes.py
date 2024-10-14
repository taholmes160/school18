from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, login_required, logout_user
from app import db
from app.models import User
from app.auth import auth_bp
from app.forms import LoginForm

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('auth.dashboard'))  # Redirect to dashboard
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))

@auth_bp.route('/')
def home():
    return render_template('home.html')

@auth_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')