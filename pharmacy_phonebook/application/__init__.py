from flask import Flask, request, Response, redirect, abort, make_response, url_for, session, render_template
import database


app = Flask(__name__)
app.secret_key = 'A1Zr51j/3yX R~X@H!jmN]kAX/,?UT'

database = database.Database()
# database.init_database()


@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/phonebook')
def phonebook_index():
    return render_template('PhoneBook_Index.html')


@app.route('/phonebook/insert')
@app.route('/phonebook/insert', methods=['POST'])
def phonebook_insert():
    if request.method == 'POST':
        name = request.form.get('name')
        telno = request.form.get('telno')
        address = request.form.get('address')
        is_success = database.insert_data(name, telno, address)
        return is_success + "<br> <a href=\'/phonebook\'>Go To Main Page!</a>"
    return render_template('PhoneBook_Insert.html')


@app.route('/phonebook/search')
@app.route('/phonebook/search', methods=['POST'])
def show_whole_phonebook():
    if request.method == 'POST':
        name = request.form.get('name')
        item = database.fetch_filter_data(name)
        if item:
            return render_template('PhoneBook_Search.html', items=item)
    item = database.fetch_all_data()
    if item:
        return render_template('PhoneBook_Search.html', items=item)


@app.route('/phonebook/delete')
@app.route('/phonebook/delete', methods=['POST'])
def phonebook_delete():
    if request.method == 'POST':
        index = request.form.get('index')
        is_success = database.delete_data(index)
        return is_success + "<br> <a href=\'/phonebook\'>Go To Main Page!</a>"
    item = database.fetch_all_data()
    if item:
        return render_template('PhoneBook_Delete.html', items=item)
