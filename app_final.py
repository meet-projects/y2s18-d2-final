from flask import Flask, render_template, url_for, redirect, request, session

from databases_final import add_article, get_all_articles, add_user, get_all_users

import os  


app = Flask(__name__)


# login_manager = LoginManager()
# login_manager.init_app(app)



@app.route('/')
def home():
    return render_template('home.html')

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 
=======
=======
>>>>>>> 74e1558ff89ccf3264e929f8c7f9434f987c2881
=======
>>>>>>> 74e1558ff89ccf3264e929f8c7f9434f987c2881
# @app.route('/articles')
# def articles():
#    return render_template(#name of file '.html'
#    	)     
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 74e1558ff89ccf3264e929f8c7f9434f987c2881
=======
>>>>>>> 74e1558ff89ccf3264e929f8c7f9434f987c2881
=======
>>>>>>> 74e1558ff89ccf3264e929f8c7f9434f987c2881


@app.route('/add_article', methods=['GET', 'POST'])
def add_articles_route():
  if request.method == 'GET':
    return render_template('story.html')
  else:
    print ('Received POST request for adding an article!')
    title = request.form['article_title']
    content = request.form['article_content']

    add_article(title, content)        
    




@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template('sign-up.html')
  else:
    print ('Received POST request for sign up!')
    nationality = request.form['nationality']
    name = request.form['name']
    email = request.form['email']
    password= request.form['password']

    add_user(nationality, name, email, password)        
    

    # i should check with the other group members if they what they want to happen after the user sign up 
    #(meaning: which html page should the user see once he is finshed signing up? )

# @app.route('/login', methods=['GET', 'POST'])
# def login_route():
#   if request.method == 'POST':
#     if request.form['password']=='password':

#   else:
#     return render_template(#'name of file .html'
#     	)
    





if __name__ == "__main__":
    app.run(debug=True)