from sqlalchemy import Column, Integer, String, Date, Boolean
from book_rental_service.application.database import base, db_session


class Book(base):
    __tablename__ = 'book'
    isbn = Column(String(40), primary_key=True)
    name = Column(String(40))
    author = Column(String(40))
    price = Column(String(10))
    description = Column(String(40))
    link = Column(String(100))
    picturepath = Column(String(60))
    canrental = Column(Boolean(), default=True)

    def __init__(self, isbn, name, author, price, description, link, picture_path, canresntal):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.price = price
        self.description = description
        self.link = link
        self.picturepath = picture_path
        self.canrental = can_resntal

    def __repr__(self):
        return "<Book('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'>" % \
               (self.isbn, self.name, self.author, self.price
                , self.description, self.link, self.picturepath, self.canrental)


class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    birthday = Column(Date)
    gender = Column(String(2))
    email = Column(String(20))
    telno = Column(String(14))
    picturepath = Column(String(100))
    query = db_session.query_property()
    column_list = ['ID', 'Name', 'Birthday', 'Gender', 'E-Mail', 'Tel', 'Picture']

    def __init__(self, id, name, birthday, gender, email, telno, picturepath):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.email = email
        self.telno = telno
        self.picturepath = picturepath

    def __len__(self):
        return 7

    def __str__(self):
        return "%d,%s,%s,%s,%s,%s,%s" % \
               (self.id, self.name, self.birthday, self.gender, self.email
                , self.telno, self.picturepath)


class BookRental(base):
    __tablename__ = 'bookrental'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    isbn = Column(String(40))
    rental_date = Column(Date)
    return_date = Column(Date)
    isrental = Column(Boolean(), default=False)

    def __init__(self, id, user_id, isbn, rental_date, return_date, isrental):
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.user_birthday = user_birthday
        self.isbn = isbn
        self.rental_date = rental_date
        self.return_date = return_date
        self.isrental = isrental

    def __repr__(self):
        return "<BookRental('%d', '%d', '%s', '%s', '%s', '%s'>" % \
               (self.id, self.user_id, self.isbn, self.rental_date
                , self.return_date, self.isrental)
