import os

from dotenv import load_dotenv

from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
# from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from backend.controller.events import BaseEvents
from backend.controller.users import BaseUsers

app = Flask(__name__, static_folder='build/', static_url_path='/')

load_dotenv(dotenv_path=".env")

CORS(app)

# NO NEED FOR A ROUTE TO HOME
# @app.route("/")
# def index():
#     return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/events")
def getEvents():
    return BaseEvents().getAllEvents()

@app.route("/profile/login", methods=['POST', 'GET'])
def login():
    # if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = BaseUsers().getUserByUsername(username)
    
    if user:
        if check_password_hash(user.json['password'], password):
            # login_user(user, remember=True)
            return user
        else:
            return jsonify(Error="Invalid Password"), 401
    else:
        return jsonify(Error="User Not Found"), 404

@app.route("/profile/register", methods=['POST', 'GET'])
def register():
    # if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')
    
    if BaseUsers().checkUserExists(username):
        return jsonify(Error="User Already Exists"), 409
    elif password != password_confirmation:
        return jsonify(Error="Passwords do not match"), 401
    else:
        new_user = BaseUsers().insertUser(username, generate_password_hash(password, method='sha256'), 0, 0, 0, False)
        # TODO: database connection implementation
        # login_user(new_user, remember=True)
        return jsonify(new_user), 200

# @app.route('/profile/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/profile')

if __name__ == "__main__":
    app.run()