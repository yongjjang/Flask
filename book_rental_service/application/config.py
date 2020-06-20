db = {
    'user': 'root',
    'password': 'q',
    'host': '113.198.235.226',
    'port': '15346',
    'database': 'bookrentalservice'
}
DB_URL = "mysql+mysqlconnector://" + db['user'] + ":" + db['password'] + "@" + db['host'] + ":" + db['port'] + "/" + db['database'] + "?charset=utf8"
