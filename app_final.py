from flask import Flask, render_template, url_for, redirect, request, session

from databases_final import add_article, get_all_articles, add_user, get_all_users


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.    


@app.route('/add_article', methods=['GET', 'POST'])
def add_articles_route():
  if request.method == 'GET':
    return render_template('story.html')
  else:
    print ('Received POST request for adding an article!')
    title = request.form['article_title']
    content = request.form['article_content']

    add_article(title, content)        
    return render_template(#'name of the file.html',
      t = title,
      c = content)




@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template(#'name of file .html'
    	)
  else:
    print ('Received POST request for sign up!')
    nationality = request.form['user_nationality']
    name = request.form['user_name']
    email = request.form['user_email']

    add_user(nationality, name, email)        
    return render_template(#'name of the file.html',
      nat = nationality,
      nam= name,
      e = email)

    # i should check with the other group members if they what they want to happen after the user sign up 
    #(meaning: which html page should the user see once he is finshed signing up? )






if __name__ == "__main__":
    app.run(debug=True)