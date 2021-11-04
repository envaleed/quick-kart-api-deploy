import os
from flask import Flask

#app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)
#app.config.from_pyfile('config.py')
os.environ.get('SECRET_KEY')
os.environ.get('DATABASE_URI')

from quickkart_api import models, serializers, views, auth, errors