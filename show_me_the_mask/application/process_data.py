import logging
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import numpy

from application.database import db_session, init_db
from application.models import TbTest
import json


def make_url(lat, lon, meter):
    mask_stock_url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json"
    lat, lon, meter = lat, lon, meter
    url = mask_stock_url + '?lat=' + str(lat) + '&lng=' + str(lon) + '&m=' + str(meter)
    return url


def get_json_data(url):
    u = urlopen(url)
    try:
        data = u.read()
        json_data = json.loads(data.decode('utf-8'))
        return json_data

    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])


def get_item(key, json_data):
    try:
        item = json_data[key]
        return item
    except KeyError as err:
        logging.info(err)


def get_tables():
    queries = db_session.query(TbTest)
    entries = [dict(id=q.id, name=q.name, addr=q.addr, lat=q.lat, lng=q.lng, stock_at=q.stock_at, remain_stat=q.remain_stat) for q in queries]
    return entries


def add_entry(id, name, addr, lat, lng, stock_at, remain_stat):
    t = TbTest(id, name, addr, lat, lng, stock_at, remain_stat)
    db_session.add(t)
    db_session.commit()


def delete_entry(id):
    db_session.query(TbTest).filter(TbTest.id == id).delete()
    db_session.commit()


def init_tables():
    for lat in numpy.arange(33.0, 43.0, 0.1):
        for lng in numpy.arange(124.0, 132.0, 0.1):
            items = (get_item('stores', get_json_data(make_url(lat, lng, 5000))))
            for item in items:
                try:
                    add_entry(item['code'], item['name'], item['addr'], item['lat'], str(item['lng']), str(item['stock_at']), str(item['remain_stat']))
                except KeyError:
                    continue
    db_session.close()


if __name__ == "__main__":
    test = get_tables()
    print(type(test[0]))
    print(len(test))

# if __name__ == "__main__":
#     insert_data()
#     items = get_item('stores', get_json_data(make_url(35.2, 129.1, 500)))
#     for item in items:
#       print(item)
