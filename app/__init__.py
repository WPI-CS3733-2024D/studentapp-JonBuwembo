from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# configure application according to what is defined in config class
app = Flask(__name__)
app.config.from_object(Config)
# creates the database for communication
db = SQLAlchemy(app)

# package app
from app import routes, models, errors
