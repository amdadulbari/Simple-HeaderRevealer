from flask import Flask, request, jsonify
import json
import sys

app = Flask(__name__)

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
