import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'student.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_PATH = basedir # base directory
    STATIC_FOLDER = os.path.join(basedir, 'app//view//static') # specify location of static folder
    TEMPLATE_FOLDER = os.path.join(basedir, 'app//View//templates') # specify location of templates folder