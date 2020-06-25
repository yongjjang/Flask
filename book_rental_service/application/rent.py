from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify

rent = Blueprint('rent', __name__, url_prefix='/rent', template_folder='templates/rent/', static_folder='static')


@rent.route('/register')
def register():

    return render_template('rent/rent_register.html')


@rent.route('/list')
def rent_list():
    rental_list = BookRental.query.all()
    logging.info(rental_list)
    list_column = BookRental.column_list
    return render_template('rent/rent_list.html',
                           items=rental_list, table_head=list_column)


@rent.route('/rental', methods=['POST'])
def rental():
    if request.method == 'POST':
        id = get_max_id(BookRental) + 1
        isbn = request.form['isbn']
        username = request.form['username']
        birthday = request.form['birthday']

        book = Book.query.filter_by(isbn=isbn).first()
        user = User.query.filter_by(name=username).filter_by(birthday=birthday).first()
        if book and user:
            logging.info("Book is rented Out? : " + str(book.isrentedout))
            logging.info("User can Rent? : " + str(user.canrent))
            try:
                if not book.isrentedout and user.canrent:
                    rental_date, return_date = get_rent_date()
                    user.canrent = False
                    book.isrentedout = True
                    add_entry(BookRental(id=id, userid=userid, bookid=bookid, rentaldate=rental_date,
                                     returndate=return_date, isrentout=is_rent_out))
                    db_session.commit()
                    return render_template('/success_or_failed.html', status="Success", description="도서 대출 실행 완료!")
            except Exception as ex:
                Logging.info(ex)
            finally:
                return render_template('/success_or_failed.html', status="Failed", description="대출할  수 없는 도서 또는 사용자입니다.")
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
