import os

from dotenv import load_dotenv

from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.controller.events import BaseEvents
from backend.controller.users import BaseUsers

app = Flask(__name__, static_folder='build/', static_url_path='/')

load_dotenv(dotenv_path=".env")

CORS(app)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/events")
def getEvents():
    return BaseEvents().getAllEvents()

@app.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = BaseUsers().getUserByUsername(username)
    if user:
        if user.json['password'] == password:
            return user
        else:
            return jsonify(Error="Invalid Password"), 401
    else:
        return jsonify(Error="User Not Found"), 404

@app.route("/register", methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    if BaseUsers().checkUserExists(username):
        return jsonify(Error="User Already Exists"), 409
    else:
        return BaseUsers().insertUser(username, password, 0, 0, 0, False)

if __name__ == "__main__":
    app.run()