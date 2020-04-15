from flask import Flask, request, jsonify, current_app, render_template
from application.process_data import get_tables
import logging


logging.basicConfig()

app = Flask(__name__)


whole_items = get_tables()


@app.route('/')
def index():
    return render_template('index.html', items=whole_items)
    #
    # item = get_item('stores', get_json_data(make_url(35.145501, 129.036820, 5000)))
    # return render_template('index.html', items=item)
