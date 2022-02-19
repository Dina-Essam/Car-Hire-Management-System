from flask import Flask

app = Flask(__name__)
with app.app_context():
    app.config.from_object('config.DevConfig')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
