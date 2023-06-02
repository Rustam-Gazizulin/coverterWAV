from flask import Flask
from routs.users import users
from routs.start_page import start_page
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

SQLAlchemy(app)

app.register_blueprint(users)
app.register_blueprint(start_page)
