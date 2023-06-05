from flask import Flask

from models.users import addUser
from routs.users import users
from routs.start_page import start_page
from utils.db import engine, Base

app = Flask(__name__)

# Base.metadata.drop_all(engine)  # удаление таблиц
Base.metadata.create_all(engine)  # создание таблиц

app.register_blueprint(users)
app.register_blueprint(start_page)


if __name__ == "__main__":
    app.run(debug=True)

