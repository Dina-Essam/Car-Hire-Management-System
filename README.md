
<h1>Car Hire Management System</h1>


<h2>Reqirements</h2>
Details: The main focus of the business is renting cars and vans, and the database is to manage the
booking system.
1. Vehicles are categorized into small cars (suitable for carrying up to 4 people), family cars
(suitable for carrying up to 7 adults), and vans.<br>
2. Information stored for each booking includes customer, car, date of hire and date on which the
vehicle is to be returned.<br>
3. A customer cannot hire a car for longer than a week.<br>
4. If a vehicle is available, the customer&#39;s details are recorded (if not stored already) and a new
booking is made.<br>
5. Potential or existing customers can book a vehicle up to 7 days in advance depending on
availability.<br>
6. Customers must pay for the vehicle at the time of hire.<br>
7. On receiving an enquiry, employees are required to check availability of cars and vans.<br>
8. An invoice is written at the time of booking for the customer.<br>
9. If the booking has been made in advance, a confirmation letter will be sent to the customer.<br>
10. A report is printed at the start of each day showing the bookings for that particular day.<br>


<h2>ERD</h2>
<img src="https://github.com/Dina-Essam/Car-Hire-Management-System/blob/main/erdCarRent.PNG?raw=true"/>

<h2>To run locally, do the usual:</h2>

1- Install pipenv<br>
    pip install pipenv
    
2- Activate the venv<br>
    pipenv shell
    
3- Install the dependencies<br>
    pipenv install

4- Create databse in mysql<br>
	mysql -u root -p<br>
	mysql>CREATE DATABASE exchange_rate;
    
5- Update MySql configuration<br>
    update in file .env
    
6- Start the flask server<br>
    flask run
    

