from app import app
from models.users import Base
from utils.db import engine

# Base.metadata.drop_all(engine)  # удаление таблиц
Base.metadata.create_all(engine)  # создание таблиц


if __name__ == "__main__":
    app.run(debug=True)

