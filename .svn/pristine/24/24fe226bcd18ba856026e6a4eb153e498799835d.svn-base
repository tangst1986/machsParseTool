from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, event
from sqlalchemy.exc import DisconnectionError

def checkout_listener(dbapi_con, con_record, con_proxy):
    try:
        try:
            dbapi_con.ping(False)
        except TypeError:
            dbapi_con.ping()
    except dbapi_con.OperationalError as exc:
        if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
            raise DisconnectionError()
        else:
            raise


engine = create_engine("mysql+pymysql://root:qwe@localhost:3306/pcmanager", echo=True)
event.listen(engine, 'checkout', checkout_listener)

Base = declarative_base()
class RunningTb(Base):
    __tablename__ = 'runningTb1'
    ip = Column(String(40), primary_key=True)
    type = Column(String(10))
    status = Column(String(40))
    username = Column(String(40))
    lastuser = Column(String(40))
    lastlogintime = Column(String(40))
    def __repr__(self):
        return "<RunningTb(ip='%s', type='%s', status='%s', username='%s',lastuser='%s', lastlogintime='%s')>"%(
            self.ip, self.type, self.status, self.username, self.lastuser, self.lastlogintime)