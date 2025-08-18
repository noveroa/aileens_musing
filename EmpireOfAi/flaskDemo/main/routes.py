from functools import wraps
from flask import render_template, request, jsonify
from .auth import get_auth_token
from flaskDemo.main import bp
from functions.chatgptmodel import model


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


#Function to add a student
@bp.route('/storyPrompt',methods=['GET','POST'])
def storyPrompt():
   if request.method == 'POST':
    input_text = request.form['prompt']
    # Generate text using the model
    output = model(input_text, max_length=50)
    return render_template('newstory.html', input=input_text, output=[o['generated_text'] for o in output])
   else:
       return render_template('inititate.html')