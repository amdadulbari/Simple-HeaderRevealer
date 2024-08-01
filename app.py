from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    # Collect headers
    headers = {key: value for key, value in request.headers.items()}
    
    # Get the raw body for non-form data
    if request.data:
        body = request.data.decode('utf-8')
    else:
        body = request.form if request.form else {}
    
    # Collect query parameters
    params = {key: value for key, value in request.args.items()}

    # Construct the response
    response = {
        'path': path,
        'method': request.method,
        'headers': headers,
        'params': params,
        'body': body
    }

    # Return the response as JSON
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
