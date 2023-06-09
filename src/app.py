import os

from flask import Flask, request, flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user
from werkzeug.utils import secure_filename

from models.users import User
from routs.auth import auth
from routs.users import users
from routs.start_page import start_page
from utils.db import engine, Base, session


# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__)


# папка для сохранения загруженных файлов
app.config['UPLOAD_FOLDER'] = 'static/uploads'

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Ограничение на размер загружаемого файла

app.secret_key = 'your_secret_key_here'

app.register_blueprint(users)
app.register_blueprint(start_page)
app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return session.query(User).get(user_id)


def allowed_file(filename):
    """ Функция проверки расширения файла """
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        file = request.files['file']
        # Если файл не выбран, то браузер может
        # отправить пустой файл без имени.
        if file.filename == '':
            return render_template("profile.html", name=current_user.name)
        if file and allowed_file(file.filename):
            # безопасно извлекаем оригинальное имя файла
            filename = secure_filename(file.filename)
            # сохраняем файл
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename))
            # если все прошло успешно, то перенаправляем
            # на функцию-представление `download_file`
            # для скачивания файла
            return render_template("success_upload.html", name=filename)
    return render_template('profile.html', name=current_user.name)





Base.metadata.create_all(engine)  # создание таблиц

# Base.metadata.drop_all(engine)  # удаление таблиц

if __name__ == "__main__":
    app.run(debug=True)
