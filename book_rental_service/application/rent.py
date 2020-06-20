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

