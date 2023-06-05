from sqlalchemy import create_engine
from decouple import config
from sqlalchemy.orm import declarative_base

user = config('POSTGRES_USER')
password = config('POSTGRES_PASSWORD')
db_name = config('POSTGRES_DB')
host = config('POSTGRES_HOST')

engine = create_engine(f'postgresql://{user}:{password}@{host}/{db_name}')

engine.connect()  # подключение к бд

# функция, которая создает базовый класс для декларативных классов
Base = declarative_base()
