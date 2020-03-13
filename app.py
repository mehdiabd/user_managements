__author__ = "Mehdi Abdullahi"

from functools import wraps
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, verify_jwt_in_request, create_access_token,
    get_jwt_claims
)
from user import User
from db import DB

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'sma97'
jwt = JWTManager(app)


def admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt_claims()
        if claim['roles'] != 'admin':
            return jsonify(msg='Just for Admins!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


@jwt.user_claims_loader
def add_access_token(id):
    if id == 'admin':
        return {'roles': 'admin'}
    else:
        return {'roles': 'peasant'}


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    access_token = create_access_token(username)
    return jsonify(access_token=access_token)


@app.route('/signup', methods=['POST'])
def signup():
    user = User.__init__()
    DB.add(user)


@app.route('/edit_pro', methods=['GET', 'POST'])
def edit():
    # User.update()
    DB.update()


@app.route('/delete', mehtods=['GET', 'POST'])
def delete():
    # User.__delete__()
    DB.remove()


@app.route('/ch_pass', methods=['GET', 'POST'])
def chpass():
    # User.chpass()
    DB.ch_pass()


@app.route('/protected', methods=['GET'])
@admin
def protected():
    return jsonify(secret_message="sorry!")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
