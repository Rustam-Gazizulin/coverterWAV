from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/')
def start_page():
    return "Hello World"


@users.route('/users')
def add_user():
    return "User saving"
