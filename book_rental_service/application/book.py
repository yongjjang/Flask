from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify

book = Blueprint('book', __name__, url_prefix='/book', template_folder='templates/book/', static_folder='static')


@book.route('/search')
def search():
    item = get_tables(Book)
    item_size = len(item[0])

    return render_template('book/book_search.html', items=item, length_item=item_size, table_head=Book.column_list)


@book.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        isbn = request.form['isbn']
        item = search_entry(Book, Book.isbn, isbn)

        is_valid = item[0].__contains__("None")

        return render_template('book/book_info.html', entry=item, is_valid=is_valid)


@book.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = get_max_id(Book) + 1
        bookname = request.form['bookname']
        author = request.form['author']
        isbn = request.form['isbn']
        price = request.form['price']
        description = request.form['description']
        link = request.form['link']
        picture = request.form['Picture']

        if add_entry(Book(id, isbn, bookname, author, price, description, link, picture, True)):
            return "Success"
        else:
            return "Failed"
    else:
        return render_template('book/book_register.html')


@book.route('/check', methods=['POST'])
def check_valid():
    data = request.get_json()
    isbn = data['isbn']

    logging.info("new isbn :" + isbn)
    result = Book.query.filter_by(isbn=isbn).first()

    if not result:
        logging.info(isbn + ' 사용가능')
        return jsonify({'existence': 'false'})
    else:
        logging.info(isbn + ' 사용불가')
        return jsonify({'existence': 'true'})


@book.route('/get_json', methods=['POST'])
def get_json_book():
    data = request.get_json()
    isbn = data['isbn']

    result = search_entry(Book, Book.isbn, isbn)
    result = {'bookName': result[2], 'author': result[3]}

    if not result:
        return "false"
    else:
        return jsonify(result)

