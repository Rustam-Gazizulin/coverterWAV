from flask import Blueprint, render_template

start_page = Blueprint('start_page', __name__)


@start_page.route('/')
def index():
    return render_template('index.html')


@start_page.route('/profile')
def profile():
    return render_template('profile.html')
