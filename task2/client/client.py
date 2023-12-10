from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/client', methods=['GET'])
def echo():
    input_number = request.args.get('number')
    try:
        input_number = int(input_number)
    except:
        return 'Bad arg'
    
    try:
        response = requests.post(
            'http://127.0.0.1:3333/server',
            json={
                "number": input_number
            }
        )
    except requests.exceptions.RequestException as e:
        return 'Bad ping'
    
    
    return response



app.run(host='0.0.0.0', port=3000, debug=True)
