from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import pyexcel as pe
import pyexcel.ext.xlsx
from pprint import pprint

records = pe.get_array(file_name="/home/lrlz/pcmanager/UP5&UP6_Lab_Equipment_2016.xlsx")
engine = create_engine("mysql+pymysql://root:qwe@localhost:3306/pcmanager", echo=True)
metadata = MetaData(engine)
pcinfor5 = Table('pcinfor5', metadata,
          Column('PC_IP', String(40), primary_key=True),
          Column('PC_user', String(40)),
          Column('PC_password', String(40)),
          Column('PC_name', String(40)),
          Column('PC_Rack', String(40)),
          Column('PC_OS', String(40)),
          Column('Type', String(40)),
          Column('BTS_Name', String(40)),
          Column('BTS_Rack', String(40)),
          Column('RF', String(40)),
          Column('RF_Rack', String(40)),
          Column(u'PC_name-1', String(40)),
          Column(u'PC_IP-1', String(40)),
          Column('APC_Power_breaker', String(40)),
          Column('APC_IP', String(40)),
          Column('PC_Ports(1to8)', String(40)),
          Column('Owner', String(40)),
          Column('Line', String(40)),
          Column('Cagegory', String(40)),
          Column('Release', String(40)),
          Column('Comment', String(40)))
conn = engine.connect()

def import_db():

    #create_db(title)
    metadata.create_all()
    ins = pcinfor5.insert()

    title = [u'PC IP', u'PC user', u'PC password', u'PC name', u'PC Rack', u'PC  OS', u'Type', u'BTS Name',
             u'BTS Rack', u'RF', u'RF Rack', u'PC name-1', u'PC IP-1', u'APC /Power breaker', u'APC   IP',
             u'APC Ports(1 to 8)', u'Owner', u'Line', u'Cagegory', u'Release', u'Comment']

    print str(ins)
    for record in records[2:]:
        if record[0] == "":
            continue
        ins = pcinfor5.insert().values(record)
        result = conn.execute(ins)
        print result

def select_db():
    from sqlalchemy.sql import select
    #s = select([pcinfor4])
    s = select([pcinfor5.c.PC_IP])
    result = conn.execute(s)

    hosts = [item[0] for item in result]
    return hosts

def create_runing_db():
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.sql import select

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
            return "<RunningTb(ip='%s', type='%s', status='%s', username='%s',lastuser='%s', self.lastlogintime)>"%(
                self.ip, self.type, self.status, self.username, self.lastuser, self.lastlogintime)

    print RunningTb.__table__
    #Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    """ select data from pcinfor, than insert the ip and type in RunningTb """
    s = select([pcinfor5.c.PC_IP, pcinfor5.c.Type])
    result = conn.execute(s)

    for item in result:
        session.add(RunningTb(ip=item[0],type=item[1]))
    session.commit()
    session.close()

select_db()