import functools
from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

user = Blueprint('user', __name__, url_prefix='/user', template_folder='templates/user', static_folder='static')


@user.route('/search')
def search():
    item = get_tables(User)
    item_size = len(item[0])

    return render_template('user/user_search.html', items=item, length_item=item_size, table_head=User.column_list)


@user.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        name = request.form['name']
        # birthday = request.form['birthday']
        item = search_entry(User, User.name, name)

        is_valid = item[0].__contains__("None")

        return render_template('user/user_info.html', entry=item, is_valid=is_valid)


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        id = get_max_id(User) + 1
        username = request.form['username']
        birthday = request.form['birthday']
        email = request.form['email']
        gender = request.form['gender']
        tel = request.form['tel']
        picture = request.form['picture']

        if add_entry(User(id, username, birthday, gender, email, tel, picture, True)):
            return "Success"
        else:
            return "Failed"
    else:
        return render_template('user/user_register.html')
