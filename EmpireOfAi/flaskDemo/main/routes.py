from functools import wraps
from flask import render_template, request, jsonify
from .auth import get_auth_token
from flaskDemo.main import bp



# Example of using the decorator
@bp.route('/protected')
def protected():
    try:
        token_info, user_info, username = get_auth_token(request)
        return jsonify({'message': f'Welcome, {username}!'})
    except Exception as e:
        return jsonify({"message": f"Invalid token! /n {e}"}), 401

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/home')
def home():
    if request.method == "GET":
        token_info , user_info,  username = get_auth_token(request)
        return jsonify({"message": f"{username}"}), 200

    else:
        jsonify({"message": f"Invalid token! {request}"}), 401