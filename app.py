__author__ = "Mehdi Abdullahi"

from functools import wraps
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, verify_jwt_in_request, create_access_token,
    get_jwt_claims
)
from user import User

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
    pword = request.json['password']
    confirm = request.json['repeat_password']
    if pword == confirm:
        return jsonify({'data': str(User().add(request.json))})


@app.route('/user/<id>', methods=['PUT'])
def edit(id):
    User.update(id, request.json)


@app.route('/user/<id>', methods=['DELETE'])
@admin
def delete(id):
    User.delete(id)


@app.route('/user/<user_id>/password', methods=['PATCH'])
@admin
def chpass(user_id):
    current = request.json('current_password')
    new = request.json('new_password')
    repeat = request.json('repeat_password')
    user = User.fetch(user_id)
    if user is None:
        return jsonify({'error': 'user not found'})
    elif new == repeat:
        return jsonify({'data': User().chpass(id, new)})
    elif new != repeat:
        return jsonify({'error': 'password confirmation failed.'})


@app.route('/protected', methods=['GET'])
@admin
def protected():
    return jsonify(secret_message="sorry!")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
