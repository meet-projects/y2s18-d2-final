from flask import Flask, render_template, url_for, redirect, request, session

from databases_final import add_article, get_all_articles, add_user, get_all_users,query_by_username




app = Flask(__name__)







@app.route('/')
def home():
	return render_template('home.html')

# @app.route('/articles')
# def articles():
#    return render_template(#name of file '.html'
#    	)     

@app.route('/add_article', methods=['GET', 'POST'])
def add_articles_route():
  if session['logged_in']==True:  
      if request.method == 'GET':
        return render_template('story.html')
      if request.method=="POST":
        print ('Received POST request for adding an article!')
        title = request.form['article_title']

        content = request.form['article_content']
        print ('hey')
        add_article(title, content)
        return render_template('home.html')        
      else:
        print('not logged in')





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
		return render_template('home.html')


@app.route('/stories')
def stories_page():

  return render_template(#'name of page', g=get_all_articles() 
    )


@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if request.method == 'POST':
    user=query_by_username(request.form['name'])
    if user==None:
        return('not a user')
    else:
      if request.form['password']==user.password:
        session['logged_in'] = True
        sesion['user_id']=user.id
        return render_template('') 
      else:
        flash('wrong password!')
        return redirect(url_for('home'))



#   else:
#     return render_template(#'name of file .html'
#     	)
	



if __name__ == "__main__":

  app.run(debug=True)

