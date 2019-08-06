# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from database import *
from flask import session as login_session

# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
# Login route
# login func def
# check credentials
# set sesssion['user_id'] = user.id
# App routing code here
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/women')
def women_page():
	return render_template('women.html')

@app.route('/men')
def men_page():
	return render_template('men.html')

@app.route('/kids')
def kids_page():
	return render_template('kids.html')

@app.route('/product')
def product_page():
	return render_template('product.html')

@app.route('/cart.html')
def cart_page():
	items_dic = get_items(login_session['user_id'])
	print(login_session['user_id'],"user id",items_dic)
	items = []
	for item in items_dic:
		items.append(get_item(item['item_id']))
	return render_template("cart.html", items = items)

@app.route('/signup', methods=['POST',"GET"])
def signup():
	#check that username isn't already taken
	if request.method == 'POST':
		user = get_user(request.form['email'])
		if user == None:
			add_user(request.form['email'],request.form['psw'])
			return home()
	return render_template('singin.html')

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		print("Got inside if" + request.method)
		user = get_user(request.form['username'])
		if user != None and user.verify_password(request.form["password"]):
			login_session['name'] = user.username
			login_session['user_id'] = user.id
			login_session['logged_in'] = True
	 		return home()
	else:
		return render_template('login.html')





# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
