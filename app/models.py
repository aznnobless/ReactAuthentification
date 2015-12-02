from app import db 
from passlib.apps import custom_app_context as pwd_context #passlib

'''
The db SQLAlchemy object contains a 'db.Model' and 'db.Column" method to map tables and columns to classes and objects respectively.
'''

class Post(db.Model):
  
  __tablename__ = 'post'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  author = db.Column(db.String(128))
  body = db.Column(db.Text)
  timestamp = db.Column(db.DateTime)

  def __init__(self, title, author, body, timestamp):
    self.title = title
    self.author = author
    self.body = body
    self.timestamp = timestamp

  def __repr__(self):
    return '<Post %r>' % self.title

class User(db.Model):

  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(32), index = True)
  password_hash = db.Column(db.String(128));

  # takes a plain password as argument and stores a hash of it with the user.
  # This method is called when a new user is registering with the server, or when the user changes the password.
  def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

  # takes a plain password as argument and returns True if the password is correct or False if not
  def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)
