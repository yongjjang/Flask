from sqlalchemy import Column, Integer, String
from application.database import base


class TbTest(base):
    __tablename__ = 'mask_stock'
    id = Column(Integer, primary_key=True)
    name = Column(String(70))
    addr = Column(String(110))
    lat = Column(String(13))
    lng = Column(String(15))
    stock_at = Column(String(20))
    remain_stat = Column(String(10))

    def __init__(self, id, name, addr, lat, lng, stock_at, remain_stat):
        self.id = id
        self.name = name
        self.addr = addr
        self.lat = lat
        self.lng = lng
        self.stock_at = stock_at
        self.remain_stat = remain_stat

    def __repr__(self):
        return "<TbTest('%d', '%s', '%s', '%s', '%s', '%s', '%s'>" % \
               (self.id, self.name, self.addr, self.lat, self.lng, self.stock_at, self.remain_stat)
