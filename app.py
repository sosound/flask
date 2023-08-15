import config

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
# CORS(app, resources={r"*": {"origins": "*"}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'user5'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200))


# with app.app_context():
#     db.create_all()


@app.route('/api/')
def api():
    return 'separation'


@app.route('/')
def hello_world():  # put application's code here
    return 'flask+vue，阿里云服务器部署项目，20230811'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
