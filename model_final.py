from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy import create_engine

Base = declarative_base()


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    content= Column(String)
    image= Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship("User") 





    def __repr__(self):
        return ("article title: {}, article content:{}".format(self.title, self.content))




class User(Base):
  __tablename__="user"
  id=Column(Integer, primary_key=True)
  nationality=Column(String)
  name=Column(String, unique=True )
  email=Column(String)
  password=Column(String)
 
  


  def __repr__(self):
    return ("user nationality: {}, user name:{}, user email:{} user password:{}".format(self.nationality, self.name, self.email,self.password))
       