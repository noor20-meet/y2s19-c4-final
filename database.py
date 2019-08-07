from model import Base, User, Item, CartItem

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):

	user = User(username=name)
	user.hash_password(secret_word)
	session.add(user)
	session.commit()

def add_item(item_id,user_id):
	cart_item = CartItem(item_id=item_id , user_id=user_id)
	session.add(cart_item)
	session.commit()


def get_user(username):
	"""Find the first user in the DB, by their username."""
	return session.query(User).filter_by(username=username).first()

def delet_all_users():
	session.query(User).delete()
	session.commit()


def get_items(user_id):
	print(CartItem)
	if len(session.query(CartItem).filter_by(user_id = user_id).all()) == 0:
		return "Hello"
	else:
		return session.query(CartItem).filter_by(user_id = user_id).all()

def get_item(item_id):
	return session.query(Item).filter_by(id = item_id).first()

