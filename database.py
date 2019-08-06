
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column (Integer,primary_key=True)
	username = Column(String)
	passwors_hash = Column(String)
	isadmin = Column(Boolean)
	
	def hash_password(self, password):
	  self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
      return pwd_security.verify(password,self.password_hash)

class Item(Base):
	__tablename__ = 'items'
	id = Column(Integer,primary_key=True)
	pic = Column(String)
	price = Column(Integer)
	descrip = Column(String)


class cart_item(Base):
		"""docstring for cart_item"""
	id = Column(Integer,primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	item_id = Column(Integer, ForeignKey('items.id'))

	