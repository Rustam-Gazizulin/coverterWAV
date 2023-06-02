from flask import Blueprint, render_template

start_page = Blueprint('start_page', __name__)


@start_page.route('/')
def index():
    return render_template('start_page.html')
