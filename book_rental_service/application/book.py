from .process_data import *
from .models import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

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


@book.route('/register', methods=['GET'])
def register():
    return render_template('book/book_register.html')
