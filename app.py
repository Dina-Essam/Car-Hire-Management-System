from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
with app.app_context():
    app.config.from_object('config.DevConfig')
    mysql = MySQL(app)

    # Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Executing SQL Statements
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER	(
         CUSTOMER_ID	INTEGER NOT NULL AUTO_INCREMENT,
         FIRST_NAME	VARCHAR(30) NOT NULL,
         LAST_NAME	VARCHAR(30) NOT NULL,
         EMAIL_ADDRESS	VARCHAR(64) NOT NULL,
         TELEPHONE_NUMBER	CHAR(12) NOT NULL,
          PRIMARY KEY	(CUSTOMER_ID))''')


    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()



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
