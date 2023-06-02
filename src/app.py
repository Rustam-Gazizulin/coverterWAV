from flask import Flask
from routs.users import users

app = Flask(__name__)

app.register_blueprint(users)



