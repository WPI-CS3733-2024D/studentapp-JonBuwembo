from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


# configure application according to what is defined in config class
app = Flask(__name__)
app.config.from_object(Config)
# creates the database for communication
db = SQLAlchemy(app)

Bootstrap = Bootstrap(app)

login = LoginManager(app)
login.login_view = 'login'

moment = Moment(app)
# package app
from app import routes, models, errors
