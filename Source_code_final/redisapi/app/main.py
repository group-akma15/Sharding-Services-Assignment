# Code to demonstrate Synchronous REST Api - with the data stored in JSON file
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8000/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload

from flask import Flask, request, jsonify
import redis

'''
r.set('India', 'Delhi') 
r.set('Bangladesh', 'Dhaka')
r.set('France', 'Paris')
'''



app = Flask(__name__)
r = redis.Redis(host='test-redis',port='6379',decode_responses=True)

@app.route('/add', methods=['POST'])
def add_to_redis():
    data = request.get_json()
    key = data['key']
    value = data['value']
    r.set(key, value)
    return jsonify({'message': 'Data added to Redis'})

@app.route('/delete', methods=['DELETE'])
def delete_from_redis():
    data = request.get_json()
    key = data['key']
    if r.delete(key):
        return json.dump({'message': 'Data deleted from Redis'})
    else:
        return jsonify({'message': 'Key not found in Redis'})

@app.route('/view', methods=['GET'])
@app.route('/view/<string:key>', methods=['GET'])
def view_from_redis(key=None):
    if key is not None:
        value = r.get(key)
        if value is not None:
            return jsonify({'key': key, 'value': value.decode('utf-8')})
        else:
            return jsonify({'message': 'Key not found in Redis'})
    else:
        keys = r.keys('*')
        data = {}
        for k in keys:
            #data[k.decode('utf-8')] = r.get(k).decode('utf-8')
            data[k] = r.get(k)
        return jsonify(data)
