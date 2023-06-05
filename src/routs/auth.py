from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from models.users import User
from utils.db import session

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = session.query(User).filter_by(email=email).first()
        """Проверяем есть ли указанный email в БД и совпадает ли введенный пароль"""
        if not user or not check_password_hash(user.password, password):
            flash('Проверьте корректность пароля или вашего email и попробуйте снова!')
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)
        return redirect(url_for('start_page.profile'))
    return render_template('login.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = session.query(User).filter_by(email=email).first()
        if user:  # Проверяем если пользователь с таким email есть в БД отправляем на повторную регистрацию
            flash('Пользователь с таким email уже зарегистрирован')  # Функция флэш показывает уведомление
            return redirect(url_for('auth.signup_post'))
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        session.add(new_user)
        session.commit()

        return redirect(url_for('auth.login'))
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return 'logout'
