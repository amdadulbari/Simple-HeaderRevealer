from flask import Flask, request, jsonify
import json
import sys


from flask_sock import Sock
import time
import datetime

app = Flask(__name__)
sock = Sock(app)

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            yield f"data: {datetime.datetime.now().isoformat()}\n\n"
            time.sleep(1)
    return app.response_class(event_stream(), mimetype='text/event-stream')

@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        ws.send(data)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    # Collect headers
    headers = {key: value for key, value in request.headers.items()}
    
    # Get the raw body for non-form data
    body = request.data.decode('utf-8') if request.data else request.form.to_dict()
    
    # Collect query parameters
    params = request.args.to_dict()

    # Construct the response
    response = {
        'path': path,
        'method': request.method,
        'headers': headers,
        'params': params,
        'body': body
    }

    # Log response to stdout
    print(json.dumps(response, indent=2), file=sys.stdout)

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
