from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key = True)
    title = Column(String)
     content= Column(String)

    def __repr__(self):
        return ("article title: {}, article content:{}".format(self.title, self.content))