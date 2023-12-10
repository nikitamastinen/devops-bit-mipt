from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/server', methods = ['GET', 'POST'])
def echo():
    try:
        return request.json["number"]
    except requests.exceptions.RequestException as e:
        return 'Sever error'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 3333, debug = True)