from flask import Flask, render_template, url_for, redirect, request, session

from databases_final import add_article, get_all_articles, add_user, get_all_users,query_by_username

app = Flask(__name__)
app.secret_key ="I love ido he is literally the best and i love him"

@app.route('/')
def home():
  return render_template('NEW_HOME.html')

# @app.route('/articles')
# def articles():
#    return render_template(#name of file '.html'
#     )     

@app.route('/add_article', methods=['GET', 'POST'])
def add_articles_route():
  if session['logged_in']==True:  
    if request.method == 'GET':
      return render_template('story.html')
    if request.method=="POST":
      print ('Received POST request for adding an article!')
      title = request.form['article_title']
      content = request.form['article_content']
      user_id=session['user_id']
      
      add_article(title, content,user_id)
      return render_template('story2.html')        
  else:
    return redirect(url_for('login_route'))
        

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

    g=query_by_username(name)

    if g!=None:
      print ('we already have a user with that name')
    else:   
      add_user(nationality, name, email, password)
    return render_template('NEW_HOME.html')


@app.route('/stories')
def stories_page():

  return render_template('stories_page.html', articles = get_all_articles())



@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if 'logged_in' in session and session['logged_in']==True:
    return redirect (url_for('home'))
  if request.method == 'POST':
    print('hey')
    user=query_by_username(request.form['name'])
    if user==None:
      return redirect (url_for('signup_route'))

    else:
      if request.form['password']==user.password:
        session['logged_in'] = True
        session['user_id']=user.id
        return render_template('login.html')

  else:
    return render_template('log_in.html') 

      


@app.route('/logout')
def logout_route():
  if 'user_id' in session:
    del session['user_id']
    session['logged_in']=False
  return redirect(url_for('home'))
  print('logged out')



if __name__ == "__main__":
  app.run(debug=True)

