db = {
    'user': 'root',
    'password': 'q',
    'host': 'localhost',
    'port': '3306',
    'database': 'pharmacy'
}
DB_URL = "mysql+mysqlconnector://" + db['user'] + ":" + db['password'] + "@" + db['host'] + ":" + db['port'] + "/" + db['database'] + "?charset=utf8"
