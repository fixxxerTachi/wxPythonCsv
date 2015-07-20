from sqlalchemy import create_engine
engine=create_engine("sqlite:///c:\\Users\\hoshina\\sqlite\\test.db",echo=False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column,Integer,String
class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    del_flag = Column(Integer)

    def __repr__(self):
        return "<User(name='%s',fullname='%s',password='%s')>" % (
                self.name,self.fullname,self.password,self.del_flag)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
'''
jed_user = User(name='ed',fullname='Ed Jones',password='edspassword')
au_user = User(name='au',fullname='Au Aute',password='auspassword')
session.add(au_user)
our_user = session.query(User).filter_by(name='ed').first()
session.commit()
print our_user
'''

users = session.query(User)
for user in users:
    print user.name
