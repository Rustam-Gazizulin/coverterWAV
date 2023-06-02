from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

from utils.db import engine

engine.connect()  # подключение к бд
# функция, которая создает базовый класс для декларативных классов
Base = declarative_base()
session = Session(engine)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(50))


# INSERT
def addUser(id: int, name: str, email: str):
    session.add(User(id=id, name=name, email=email))  # добавление новых данных
    session.commit()
