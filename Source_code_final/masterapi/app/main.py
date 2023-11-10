# Code to demonstrate Synchronous REST Api - with the data stored in JSON file
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8000/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload

from flask import Flask, request, jsonify
from app.com import *

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def getAllUsers():
    user = get_data()
    return user

@app.route('/add', methods=['POST'])
def new_user():
    data = request.get_json()
    result = post_data(data)
    return result


