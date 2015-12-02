from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_DATABASE_URI
from app import app, db

'''
Flask-Migrate has two methods Migrate and MigrateCommand. 
Migrate is used to initialize the extension,
while Manager gives you access to command line options.

$ chmod +x db.py
#Initialize migrations support
$ python db.py db init
#Generate a migration
$ python db.py db migrate
$ python db.py db upgrade
'''

# sudo apt-get mysql-server
# sudo apt-get install libmysqlclient-dev

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()