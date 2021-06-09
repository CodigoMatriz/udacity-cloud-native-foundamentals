from flask import Flask
from flask import jsonify
from flask import request
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename='app.log',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info(f'{request.endpoint} endpoint was reached')
    response = {
        "result": "OK - Healthy"
    }
    return jsonify(response)

@app.route("/metrics")
def metrics():
    app.logger.info(f'{request.endpoint} endpoint was reached')
    response = {
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
