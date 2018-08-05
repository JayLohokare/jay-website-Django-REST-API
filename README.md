# jay-website-Django-REST-API
Django-MongoDB API for jaylohokare.com

This project is the REST API used in jaylohokre.com
The website (ReactJS) uses this API to load projects, education details, etc.

The API uses Django REST Framework along with DJONGO for enabling MongoDB as backend.

Requirements:
Python3,
pip3,
MongoDB (Tested with V4.0.0)

```
pip3 install django
pip3 install djangorestframework
pip3 install markdown       
pip3 install django-filter  
pip3 install djongo
```

To replicate the project structure:

```
django-admin startproject jayWebsite
python3 manage.py startapp projects
python3 manage.py runserver
#Create Mongo database 'jayWebsite'
```

Steps to follow for creating MongoDB schemas, users and to enable the REST APIs:

```
python3 manage.py createsuperuser #Follow the instructions seen on command line
python3 manage.py makemigrations projects
python3 manage.py migrate
```


