from quickkart_api import app
from quickkart_api.models import Users
from flask_jwt import JWT, jwt_required, current_identity
from flask import abort

def authenticate(username, password):
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return abort(500, "Authentication failed")

def identity(payload):
    return Users.query.filter(Users.id == payload['identity']).scalar()

jwt = JWT(app,authenticate,identity)