from flask import Flask, request, jsonify
import os

app = Flask(__name__)

auth_token = os.getenv('AUTH_TOKEN')

# Auth handler
def auth_handler(request):
    if 'Authorization' in request.headers:
        auth_header = request.headers.get('Authorization')
        token = auth_header.replace('Bearer ', '')
        if token == auth_token:
            return True
        else:
            return False
    else:
        return False


@app.route('/', methods=['GET'])
def index():
    if not auth_handler(request):
        return ('This is not for you!', 403)

    return ('Successfully Authenticated', 200)

if __name__ == '__main__':
    PORT = 8080
    # To run locally
    app.run(host='127.0.0.1', port=PORT, debug=True)