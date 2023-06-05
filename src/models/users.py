import uuid

from sqlalchemy import Column, String, update
from sqlalchemy.dialects.postgresql import UUID


from utils.db import Base, session


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    password = Column(String(100))

# INSERT
def addUser(name: str, email: str):
    session.add(User(name=name, email=email))  # добавление новых данных
    session.commit()


# DELETE by id
def deleteUser(id: int):
    session.query(User).filter(User.id == id).delete()  # поиск и удаление ряда
    session.commit()


# UPDATE name by id
def updateUser(id: int, new_name: str):
    session.execute(update(User).where(User.id == id).values(
            name=new_name))  # поиск и обновление значений
    session.commit()
