import MySQLdb
import logging
import process_data
import sys

logging.basicConfig(level=logging.INFO)

service_key = "z78AYjaYuuQ8e58v4VEYfL95N4Gf74fK%2FiJHHKns6tvcPv77DsZZzDZ0uuxE5y33xLhzkLYcJKifHI8bb3c4zg%3D%3D"
pharmacy_url = "http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey=" + service_key + \
               "&pageNo=1&numOfRows=22500"


class Database:
    def __init__(self):
        self.db = db = MySQLdb.connect("localhost", "root", "q", use_unicode=True, charset="utf8")
        self.cur = db.cursor()

    def init_database(self):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        self.cur.execute("TRUNCATE pharmacy.pharmacy_phonebook")
        items = process_data.get_item(pharmacy_url)
        index = 1

        for item in items:
            try:
                sql = "insert into pharmacy.pharmacy_phonebook(id, name, telno, address, lan, lng) " \
                      "values (%d, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" % (index, item['yadmNm'], item['telno'], item['addr'], str(item['YPos']), str(item['XPos']))

                self.cur.execute(sql.encode('utf-8'))

                index += 1
            except KeyError:
                continue
            finally:
                self.db.commit()

    def fetch_all_data(self):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        self.cur.execute("select * from pharmacy.pharmacy_phonebook")
        item = self.cur.fetchall()
        return item

    def fetch_filter_data(self, name):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        sql = "select * from pharmacy.pharmacy_phonebook where name like \'%" + name +"%\';"
        self.cur.execute(sql)
        item = self.cur.fetchall()
        return item

    def insert_data(self, name, telno, address):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        try:
            sql = "select max(id) from pharmacy.pharmacy_phonebook"
            self.cur.execute(sql)
            data_id = self.cur.fetchone()[0] + 1
            lan = "no data"
            lng = "no data"
            sql = "insert into pharmacy.pharmacy_phonebook(id, name, telno, address, lan, lng) " \
                  "values (%d, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" % (data_id, name, telno, address, lan, lng)
            self.cur.execute(sql)
        except KeyError:
            return "Insert Error, Type Invalid Value!"
        except self.db.Error as error:
            return "Insert Error : {0}", error
        finally:
            self.db.commit()
            return "Success!!"

    def delete_data(self, index):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        try:
            sql = "delete from pharmacy.pharmacy_phonebook where id=" + index + ";"
            self.cur.execute(sql)
        except self.db.Error as error:
            return "Delete Error : {0}", error
        except BaseException:
            return "Error Occurred!!"
        finally:
            self.db.commit()
            return "Success!!"

    def close_database(self):
        logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
        self.cur.close()
        self.db.close()


if __name__ == "__main__":
    database = Database()
    database.init_database()
    # database.fetch_all_data()
    # database.fetch_filter_data("약국")
    # database.insert_data("test", "test", "test")
    database.close_database()
