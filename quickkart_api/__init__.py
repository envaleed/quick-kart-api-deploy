import os
from flask import Flask

#app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)
#app.config.from_pyfile('config.py')
uri = os.environ.get('DATABASE_URL')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SECRET_KET']=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']= uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

from quickkart_api import models, serializers, views, auth, errors