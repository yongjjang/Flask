from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

rent = Blueprint('rent', __name__, url_prefix='/rent', template_folder='templates/rent/', static_folder='static')


@rent.route('/register')
def register():

    return render_template('rent/rent_register.html')


@rent.route('/return')
def book_return():
    return render_template('rent/rent_return.html')


@rent.route('/rental', methods=['POST'])
def rental():
    if request.method == 'POST':
        id = get_max_id(BookRental) + 1
        isbn = request.form['isbn']
        username = request.form['username']
        birthday = request.form['birthday']

        isbn = search_entry(Book, Book.isbn, isbn)[1]
        userid = int(search_entry(User, User.name, username)[0])

        rental_date, return_date = get_rent_date()
        is_rent_out = True
        if add_entry(BookRental(id=id, userid=userid, isbn=isbn, rentaldate=rental_date, returndate=return_date, isrentout=is_rent_out)):
            return "Success"
        else:
            return "Failed"


@rent.route('/check', methods=['POST'])
def check_valid():
    """
    :TODO
    도서 대출 시 대출이 가능한 책과 사용자인지 검증하는 기능 구현 마저 하기.

    """
    data = request.get_json()
    isbn = data['isbn']
    user_name = data['username']
    birthday = data['birthday']

    filtered_user = User.query.filter(user_name=user_name).filter(birthday=birthday).first()
    filtered_book = Book.query.filter(isbn=isbn).first()

    if not filtered_user or not filtered_book:
        return jsonify({'existence': 'false'})
    else:
        if filtered_user.canrent and not filtered_book.isrentedout:
            return jsonify({'existence': 'false'})
        else:
            logging.info(isbn + ' 사용불가')
            return jsonify({'existence': 'true'})
