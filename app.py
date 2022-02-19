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

    cursor.execute('''CREATE TABLE IF NOT EXISTS VehicleType	(
         VehicleTypeID	INTEGER NOT NULL AUTO_INCREMENT,
         NAME VARCHAR(30) NOT NULL,
         CAPACITY INTEGER,
          PRIMARY KEY (VehicleTypeID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS VEHICLE	(
         VEHICLE_ID	INTEGER NOT NULL AUTO_INCREMENT,
         NAME VARCHAR(30) NOT NULL,
         TypeID INTEGER,
         PRICE decimal(6,2) NOT NULL,
          PRIMARY KEY (VEHICLE_ID),
          FOREIGN KEY (TypeID) REFERENCES VehicleType(VehicleTypeID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS BOOKING	(
             BOOKING_ID	INTEGER NOT NULL AUTO_INCREMENT,
             Customer_ID INTEGER,
             Vehicle_ID INTEGER,
             TOTAL_PRICE decimal(6,2) NOT NULL,
             Booking_Date datetime DEFAULT current_timestamp,
             Hiring_Date datetime DEFAULT current_timestamp,
             Return_Date datetime Not NULL,
              PRIMARY KEY (BOOKING_ID),
              FOREIGN KEY (Customer_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
              FOREIGN KEY (Vehicle_ID) REFERENCES VEHICLE(VEHICLE_ID),
              constraint check_dates check (Hiring_Date < Return_Date and DATEDIFF(Hiring_Date, Return_Date) <= 7 and DATEDIFF(Booking_Date, Hiring_Date) <= 7 ))''')

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
