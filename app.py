from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS  # Import the CORS module
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
print(app)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    print(app)
    app.run()
    #createHotelsTable()
