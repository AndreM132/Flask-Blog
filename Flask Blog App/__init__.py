from flask import Flask
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASK_BLOG_URI')

from application import routes

~                                     