# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

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
	return render_template("cart.html")


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
