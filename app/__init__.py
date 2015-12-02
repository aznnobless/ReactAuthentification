from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, fields, marshal # RESTful
from flask.ext.sqlalchemy import SQLAlchemy # SQLAlchemy

#Create an instance of Flask
app = Flask(__name__, static_url_path="/static")
api = Api(app)

#Include config from config.py
app.config.from_object('config')
app.secret_key = 'some_secret'

#Create an instance of SQLAlchemy
db = SQLAlchemy(app)

from app import views, models

#Add your connection string
SQLALCHEMY_DATABASE_URI = 'mysql://root:test@localhost/NewBlog'