# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
# from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product_page():
	return render_template('product.html')

@app.route('/cart')
def cart_page():
	return render_template("cart.html")


@app.route('/contact')
def contact_page():
	return render_template("contact.html")

@app.route('/about')
def about_page():
	return render_template("about.html")


@app.route('/checkout')
def checkout_page():
	return render_template("checkout.html")

@app.route('/category')
def category_page():
	return render_template("category.html")



# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
