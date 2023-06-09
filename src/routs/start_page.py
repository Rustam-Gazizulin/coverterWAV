from flask import Blueprint, render_template
from flask_login import login_required, current_user


start_page = Blueprint('start_page', __name__)


@start_page.route('/')
def index():
    return render_template('index.html')


@start_page.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


