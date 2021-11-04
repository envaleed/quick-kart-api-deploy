import os
from flask import Flask

#app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)
#app.config.from_pyfile('config.py')
app.config['SECRET KET']=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

from quickkart_api import models, serializers, views, auth, errors