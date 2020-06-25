from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify

user = Blueprint('user', __name__, url_prefix='/user', template_folder='templates/user', static_folder='static')


@user.route('/search')
def search():
    item = get_tables(User)
    item_size = len(item[0])

    return render_template('user/user_search.html',
                           items=item, length_item=item_size,
                           table_head=User.column_list)


@user.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        name = request.form['name']
        # birthday = request.form['birthday']

        item = User.query.filter(User.name.ilike("%" + name + "%")).first()
        if not item:
            is_valid = False
        else:
            is_valid = True
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


@user.route('/check', methods=['POST'])
def check_valid():
    data = request.get_json()
    username = data['username']
    birthday = data['birthday']

    logging.debug("new name :" + username)
    result = User.query.filter_by(name=username).filter_by(birthday=birthday).first()

    if not result:
        logging.info(user_name + ' 사용가능')
        return jsonify({'existence': 'false'})
    else:
        logging.info(user_name + ' 사용불가')
        return jsonify({'existence': 'true'})


@user.route('/delete', methods=['POST'])
def delete():
    username = request.form['username']
    birthday = request.form['birthday']
    try:
        user = User.query.filter(User.name.like(username),
                                 User.birthday == birthday).first()
        add_entry(LeavedUser(user.id, user.name, user.birthday,
                             user.gender, user.email, user.telno, user.picturepath, str(datetime.date.today())))
        userid = user.id
        db_session.query(User).filter(User.id == userid).delete(synchronize_session=False)
        db_session.commit()
        return render_template('/success_or_failed.html', status="Success", description="사용자 삭제 성공!")
    except Exception as ex:
        logging.info(ex)
        return render_template('/success_or_failed.html', status="Failed", description="사용자 삭제 실패")


"""
TODO
도서 수정 소스 참고하여 유저 수정 기능 구현
반납 기능 구현
사용자 정보 검색 폼 구현

"""