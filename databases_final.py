# Database related imports
# Make sure to import your tables!
from model_final import Base, Article, User 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_article(article_title, article_content):
    print("Added an article!")
    article = Article(title=article_title, content=article_content)
    session.add(article)
    session.commit()

def get_all_articles():
    students = session.query(Article.all())
    return articles


def add_user(user_nationality, user_name, user_email):
    print("Added a user!")
    user = User(nationality=user_nationality, name=user_name, email=user_email)
    session.add(user)
    session.commit()

def get_all_users():
    users = session.query(User.all())
    return users




def add_student(title, content):
	
	article_object = Article(
		title=title,
		content=content)
	session.add(article_object)
	session.commit()    




