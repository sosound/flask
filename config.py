USERNAME = 'star'
PASSWORD = 'star'
HOSTNAME = '59.110.228.104'
PORT = '3306'
DATABASE = 'database0814'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
ENV = 'DEVELOPMENT'
DEBUG = True
