from flask import Flask, jsonify, request

app = Flask(__name__)
with app.app_context():
    app.config.from_object('config.DevConfig')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.errorhandler(500)
def internal_error(error):
    message = {
        'status': 500,
        'message': 'Server error',
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@app.errorhandler(Exception)
def handle_exception(e):
    res = {'status': e.code,
           'message': e.message if hasattr(e, 'message') else f'{e}'}
    resp = jsonify(res)
    resp.status_code = e.code
    return resp




if __name__ == '__main__':
    app.run()
