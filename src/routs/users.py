from flask import Blueprint, render_template

users = Blueprint('users', __name__, url_prefix='/usr')


@users.route('/add')
def add_user():
    return render_template('base.html')


@users.route('/list')
def list_users():
    return render_template('base.html')


@users.route('/update')
def update_user():
    return render_template('base.html')


@users.route('/delete')
def delete_user():
    return render_template('base.html')