
from model_final import Base, Article, User 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_article(title, content):
    print("Added an article!")
    article = Article(title=title, content=content)
    session.add(article)
    session.commit()

def get_all_articles():
    students = session.query(Article.all())
    return articles


def add_user(nationality, name, email, password):
    print("Added a user!")
    user = User(nationality=nationality, name=name, email=email, password=password)
    session.add(user)
    session.commit()

def get_all_users():
    users = session.query(User.all())
    return users










