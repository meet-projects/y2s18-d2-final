
from model_final import Base, Article, User 
    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_article(title, content, user_id,image):
    print("Added an article!")
    article = Article(title=title, content=content, user_id=user_id, image=image)
    session.add(article)
    session.commit()

def get_all_articles():
  articles = session.query(Article).all()
  return articles


def add_user(nationality, name, email, password):
    print("Added a user!")
    user = User(nationality=nationality, name=name, email=email, password=password)
    session.add(user)
    session.commit()

def get_all_users():
  users = session.query(User).all()
  return users


def query_by_username(name):
  users= session.query(
    User).filter_by(
    name=name).first()
  return users 

def query_by_password(password):
  users= session.query(
    User).filter_by(
    password=password).all()
  return users   



# print(get_all_articles())
#(get_all_users())   
#print(query_by_password('s'))









