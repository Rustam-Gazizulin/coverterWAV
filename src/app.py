from flask import Flask

from models.users import addUser
from routs.auth import auth
from routs.users import users
from routs.start_page import start_page
from utils.db import engine, Base

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
# Base.metadata.drop_all(engine)  # удаление таблиц

app.register_blueprint(users)
app.register_blueprint(start_page)
app.register_blueprint(auth)

Base.metadata.create_all(engine)  # создание таблиц

if __name__ == "__main__":
    app.run(debug=True)


