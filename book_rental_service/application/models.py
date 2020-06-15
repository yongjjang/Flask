from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import base


class Book(base):
    __tablename__ = 'book'
    isbn = Column(String(40), primary_key=True)
    name = Column(String(40))
    author = Column(String(40))
    price = Column(String(10))
    description = Column(String(40))
    link = Column(String(100))
    picture_path = Column(String(60))
    can_rental = Column(Boolean(), default=True)

    def __init__(self, isbn, name, author, price, description, link, picture_path, can_resntal):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.price = price
        self.description = description
        self.link = link
        self.picture_path = picture_path
        self.can_rental = can_resntal

    def __repr__(self):
        return "<TbTest('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'>" % \
               (self.isbn, self.name, self.author, self.price
                , self.description, self.link, self.picture_path, self.can_rental)


class User(base):
    __tablename__ = 'user'
    name = Column(String(40), primary_key=True)
    birthday = Column(Date, primary_key=True)
    gender = Column(String(2))
    email = Column(String(20))
    telno = Column(String(14))
    picture_path = Column(String(100))

    def __init__(self, name, birthday, gender, email, telno, picture_path):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.email = email
        self.telno = telno
        self.picture_path = picture_path

    def __repr__(self):
        return "<TbTest('%s', '%s', '%s', '%s', '%s', '%s'>" % \
               (self.name, self.birthday, self.gender, self.email
                , self.telno, self.picture_path)


class BookRental(base):
    __tablename__ = 'bookrental'

    user_name = Column(String(40))
    user_birthday = Column(Date)
    isbn = Column(String(40))
    rental_date = Column(Date)
    return_date = Column(Date)
    is_rental = Column(Boolean(), default=False)

    def __init__(self, user_name, user_birthday, isbn, rental_date, return_date, is_rental):
        self.user_name = user_name
        self.user_birthday = user_birthday
        self.isbn = isbn
        self.rental_date = rental_date
        self.return_date = return_date
        self.is_rental = is_rental

    def __repr__(self):
        return "<TbTest('%s', '%s', '%s', '%s', '%s', '%s'>" % \
               (self.user_name, self.user_birthday, self.isbn, self.rental_date
                , self.return_date, self.is_rental)
