from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from models.users import User
from utils.db import session

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
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
