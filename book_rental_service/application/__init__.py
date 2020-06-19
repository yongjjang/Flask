from flask import Flask, request, jsonify, current_app, render_template
from book_rental_service.application.process_data import *
import book_rental_service.application.models
import logging


logging.basicConfig()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/', methods=['POST'])
@app.route('/search/')
def search():
    user = models.User
    item = get_tables(user)
    item_size = len(item[0])

    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('search_table.html', items=item)

    return render_template('search_table.html', items=item, length_item=item_size, table_head=user.column_list)
