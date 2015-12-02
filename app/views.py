'''
ROUTER
'''

from flask import render_template, request, flash, redirect, session, url_for, jsonify, Response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from sqlalchemy.sql.expression import func
from app import app, db, api
from app.models import Post, User
import time
import datetime
import json
import jwt #pyjwt

app.secret_key = "techempower"

# Uncomment this to add an user entry manually
# @app.route('/kknd')
# def secretPage():
#   user = User(username = "blee")
#   user.hash_password("1234")
#   db.session.add(user)
#   db.session.commit()
#   redirect("/")

'''
  Main Page View
'''

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/posts', methods=['GET'])
def newPostPage():
  return render_template("index.html")

@app.route('/about', methods=['GET'])
def aboutPage():
  return render_template("index.html")

@app.route('/login', methods=['GET'])
def loginPage():
  return render_template("index.html")

'''
  JWT Authentication
'''

### Generate a JWT and return it
def createToken(user):
  encode = jwt.encode({"username":user.username}, 'secret', algorithm='HS256')
  print("***********")
  print(encode)
  print("***********")
  return encode

@app.route('/sessions/create', methods=['POST'])
def jwtAuth():
  
  print("JWT AUTH DEBUG")
  
  username = request.form.get("username");
  password = request.form.get("password");
  
  # TODO

  # Retrieve a user by username (Find user from db)
  user =  User.query.filter_by(username=username).first();

  # if username does not exist in DB,
  if user==None :
    print("NOT EXIST")
    return jsonify(result = "false")

  # if password does not match
  if user.verify_password(password) == False:
    print("PASSWORD DOES NOT MATCH")
    return jsonify(result = "false")
  # print("--- QUERY RESULT ---")
  # print(user)
  # print(user.id)
  # print("[username : %s , password: %s ]"  % (user.username, user.password_hash) )

  # if(user.verify_password(password))


  #print(user.username)
  #print(user.password_hash)

  '''
    At this username and password is matched.
    return id_token
  '''

  

  return jsonify(id_token = createToken(user))




'''
  TODO: This is dummy login. Recode it later.
  Login process : 
'''
@app.route('/api/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    print("DEBUG :::: POST IS CALLED")

    username = request.form['username'];
    password = request.form['password'];

    if username == "admin" and password =="1234":
      session['username'] = request.form['username']
      return jsonify(result="success");
    else:
      return jsonify(result="fail");


    print("USERNAME : %s , PASSWORD : %s" % (username, password) )


@app.route('/api/session', methods=['POST'])
def isLogin():
  if request.method == 'POST':
    if 'username' in session:
      return jsonify(result = "true")
    else:
      return jsonify(result = "false")

'''
  Temporary add post page
'''
@app.route('/test/add', methods=['POST', 'GET'])
def add():
  if request.method == 'POST':
    post=Post(request.form['title'], request.form['author'], request.form['body'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S'"))
    db.session.add(post)
    db.session.commit()
    flash('New entry was successfully posted')     
    return redirect('/')
 
  return render_template('add.html')

'''
  Temporary post list check page.
'''
@app.route('/test/view', methods=['POST', 'GET'])
def view():
  posts = Post.query.all()
  return render_template("look.html", posts=posts)

@app.route('/test/edit')
def edit():
  id = request.args.get('id', '')
  return "HERE IS EDIT PAGE. This is entry: %s" % id


class NewUserApi(Resource):
  def post(self):
    username = request.json.get('username')
    password = request.json.get('password')

    print('username %s' % username)

    # Validate form
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user

    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}

api.add_resource(NewUserApi, '/api/users', endpoint = 'users')

class BlogPostListApi(Resource):
  def get(self):
    posts = Post.query.order_by(Post.id.desc()).all() #result : a list contaning Post object

    # Create an empty list
    result = []

    for post in posts:
      #Create an empty dictionary
      temp = {}
      # add <title, value> to dictionary
      temp["title"] = post.title
      # add <body, value> to dictionary
      temp["body"] = post.body
      #
      temp["author"] = post.author
      #
      temp["timestamp"] = timeStampToString(post.timestamp)
      # add <id, value> to dictionary
      temp["id"] = post.id
      # append current dictionary to result list
      result.append(temp)

    return Response( json.dumps(result) )

  def put(self, id):
    pass
  def post(self):
    print(request.form['title'])
    print(request.form['author'])
    print(request.form['body'])
    post=Post(request.form['title'], request.form['author'], request.form['body'], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    db.session.add(post)
    db.session.commit()
    return jsonify(result="success");

  def delete(self, id):
    pass

api.add_resource(BlogPostListApi, '/api/blog/posts', endpoint = 'posts')

'''
  API to retrieve specific post
'''
class BlogPostApi(Resource):
  
  # READ 
  def get(self, id):
    post = Post.query.get(id)
    temp = {}
    temp['title'] = post.title
    temp['author'] = post.author
    temp['timestamp'] = timeStampToString(post.timestamp)
    temp['body'] = post.body
    temp['id'] = post.id
    return Response( json.dumps(temp) )

  # UPDATE  
  def put(self, id):
    # retrieve target post entry
    post = Post.query.get(id)
    # update post data
    post.title = request.form['title']
    post.author = request.form['author']
    post.body = request.form['body']
    post.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # update the modified data to db
    db.session.commit() 
    return jsonify(result="success")

  # DELETE
  def delete(self, id):
    targetPost = Post.query.get(id)
    db.session.delete(targetPost)
    db.session.commit()

api.add_resource(BlogPostApi, '/api/blog/posts/<int:id>', endpoint = 'post')

'''
  API to privide archive information on the view
'''
class BlogArchivesApi(Resource):
  def get(self):
    #Query all 
    posts = Post.query.order_by(Post.id.desc()).all()

    #print(posts) # DEBUG

    #print(type(posts)) # DEBUG

    #create empty list
    result = {}

    for post in posts:
      # retrive month data year part only from timestamp
      monthYearToken = timeStampToString(post.timestamp).split(' ')[0:3]
      # generate a key for dictionary using month and year part only
      key = monthYearToken[0] + ' ' + monthYearToken[2]
      # record information in a dictionary
      if key in result.keys():
        result[key] = result[key] + 1
      else:
        result[key] = 1

    #print(result.items()) # DEBUG
    
    return result

api.add_resource(BlogArchivesApi, '/api/blog/archives', endpoint ='archives')

class BlogQueryMonthYear(Resource):
  def get(self):
    
    year = request.args.get('year', '')
    
    month = getMonthStringToNumber(request.args.get('month', ''))

    posts = Post.query.filter(func.year(Post.timestamp) == year).filter(func.month(Post.timestamp) == month).order_by(Post.id.desc())
    result = []
    for post in posts:
      #Create an empty dictionary
      temp = {}
      # add <title, value> to dictionary
      temp["title"] = post.title
      # add <body, value> to dictionary
      temp["body"] = post.body
      #
      temp["author"] = post.author
      #
      temp["timestamp"] = timeStampToString(post.timestamp)
      # add <id, value> to dictionary
      temp["id"] = post.id
      # append current dictionary to result list
      result.append(temp)

    return Response( json.dumps(result) )

api.add_resource(BlogQueryMonthYear, '/test', endpoint ='test')


'''
  Below this line: Utility Code
'''

def timeStampToString(timestamp): #private
  str = timestamp.strftime("%m-%d-%Y %H:%M:%S")
  splitStr = str.split('-')
  splitStr[0] = getMonthString(splitStr[0]+"key")
  return " ".join(splitStr)

def getMonthString(key): # private
  monthDic = {
    "01key": "January",
    "02key": "February",
    "03key": "March",
    "04key": "April",
    "05key": "May",
    "06key": "June",
    "07key": "July",
    "08key": "August",
    "09key": "September",
    "10key" : "October",
    "11key" : "November",
    "12key" : "December"
  }
  return monthDic[key]

'''
  Convert month string to month number
'''
def getMonthStringToNumber(str):
  monthDic = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" :8, 
    "September" : 9, 
    "October" : 10,
    "November" : 11,
    "December" : 12
  }
  return monthDic[str]
