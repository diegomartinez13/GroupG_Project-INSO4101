import os

from dotenv import load_dotenv

from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from backend.controller.events import BaseEvents
from backend.controller.users import BaseUsers

app = Flask(__name__, static_folder='build/', static_url_path='/')

load_dotenv(dotenv_path=".env")

CORS(app)

@app.route("/")
def index():
    return {'message' : 'Welcome!'}

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/events")
def getEvents():
    return BaseEvents().getAllEvents()

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.json)
        username = request.json['username']
        password = request.json['password']
        
        user = BaseUsers().getUserByUsername(username)

        if user:
            if check_password_hash(user.json['password'], password):
                return user
            else:
                return jsonify(Error="Invalid Password"), 401
        else:
            return jsonify(Error="User Not Found"), 404
    elif request.method == 'GET':
        #TODO: Connect flask app to react app
        return {'message': 'Welcome to the login page'}, 200
    return 400

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        password_confirmation = request.json['password_confirmation']
        
        if BaseUsers().checkUserExists(username):
            return jsonify(Error="User Already Exists"), 409
        elif password != password_confirmation:
            return jsonify(Error="Passwords do not match"), 401
        else:
            print(generate_password_hash(password, method='sha256'))
            result = BaseUsers().insertUser(username, generate_password_hash(password, method='sha256'), 0, 0, 0, False)
            
            return result
    elif request.method == 'GET':
        #TODO: Connect flask app to react app
        return {'message': 'Welcome to the registration page'}
    return 400
    
if __name__ == "__main__":
    app.run()