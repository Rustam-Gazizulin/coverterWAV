from flask import Flask
from flask_login import LoginManager

from models.users import addUser, User
from routs.auth import auth
from routs.users import users
from routs.start_page import start_page
from utils.db import engine, Base, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
# Base.metadata.drop_all(engine)  # удаление таблиц

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


Base.metadata.create_all(engine)  # создание таблиц

if __name__ == "__main__":
    app.run(debug=True)


