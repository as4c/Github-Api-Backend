# Github-Api-Backend
Github Rest Api Backend
A Django based REST API for handling github rest api requests from reacjs frontend.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.6 or later
Django 2.2 or later
Django REST framework 3.11 or later
pip
Installing
Clone the repository

Copy code
git clone https://github.com/as4c/github-api-backend.git
Create a virtual environment and activate it

Copy code
python -m venv venv
source venv/bin/activate
Install the required packages

Copy code
pip install -r requirements.txt
Make migrations and migrate

Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser

Copy code
python manage.py createsuperuser
Run the server

Copy code
python manage.py runserver
API Endpoints
The API has the following endpoints:

/api/user/<str:username> - for sending requests from backend to github rest api server
Testing
Run the following command to run tests

Copy code
python manage.py test
Built With
Django - The web framework used
Django REST framework - Used for building RESTful API
Authors
sagar kumar- as4c
License
This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments
