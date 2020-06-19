import logging

from book_rental_service.application.database import db_session, init_db
from book_rental_service.application.models import User, Book, BookRental
import logging

init_db()


def get_tables(db_table):
    """
        @author : TAEYONG LEE
        :param db_table: database table in model.py
        :type db_table: database model Object
        :return type: dict
    """
    entries = []
    queries = db_session.query(db_table)

    for q in queries:
        s = str(q).split(',')
        entries.append(s)

    return entries


def add_entry(db_table, *args):
    """
        @author : TAEYONG LEE
        :param db_table: database table in model.py
        :type db_table: database model Object

        :param args: what u want insert table row element
    """
    entry = db_table(args)
    db_session.add(entry)
    db_session.commit()


def delete_entry(db_table):
    """
            @author : TAEYONG LEE
            :param db_table: database table in model.py
            :type db_table: database model Object
    """
    db_session.query(db_table).filter(db_table.id == id).delete()
    db_session.commit()


if __name__ == "__main__":
    result = db_session.query(User).filter(User.name.in_(['D'])).all()
    # result = db_session.query(User).filter_by(id=1).all()

    for q in db_session.query(User).filter(User.name.like('%' + "A" + "%")):
        print(q)
        print(type(q))

