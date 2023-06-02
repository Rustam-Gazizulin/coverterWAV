from flask import Flask
from routs.users import users
from routs.start_page import start_page

app = Flask(__name__)


app.register_blueprint(users)
app.register_blueprint(start_page)
