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
pip install django-cors-headers
pip3 install whitenoise
```
Create MongoDB database 'jayWebsite'.

To replicate the project structure:

```
django-admin startproject PROJECTNAME
#django-admin startproject jayWebsite

python3 manage.py startapp api
```

Steps to follow for creating MongoDB schemas, users and to enable the REST APIs:

```
python3 manage.py createsuperuser #Follow the instructions seen on command line
python3 manage.py makemigrations api
python3 manage.py migrate
```

To start the server

```
python3 manage.py runserver IP:PORT
```

If deploying the project on AWS (Or equivalent hosting), use the Private IP (Get it using ifconfig) in the runserver command (The API will be accessible on the Public IP). 

To ensure security, configure network settings:
1. Inbound and Outbound MongoDB accessible only locally at the default port
2. Inbound and outbound SSH accessible for all IPs at port 22
3. Inbound and outbound Django accessible for all IPs at port 8000


Use Environment variables for Debug and Security key. Change settings.py
```
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True))
```

Deploy:
```
python3 manage.py check --deploy
```

Migrate static files:
```
python3 manage.py collectstatic
```

Run production server
```
gunicorn --bind IP:PORT PROJECTNAME.wsgi --daemon
#gunicorn --bind 172.31.19.120:8000 jayWebsite.wsgi --daemon
```

Stopping Gunicorn server
```
ps ax|grep gunicorn
kill -9 PID
```

To enable HTTPS on Gunicorn:
1. Generate SSL keys/certificate
```
openssl genrsa 1024 > host.key
chmod 400 host.key
openssl req -new -x509 -nodes -sha1 -days 365 -key host.key -out host.cert
```
2. Provide the cert to Gunicorn while starting
```
gunicorn --certfile=server.crt --keyfile=server.key --bind IP:PORT PROJECTNAME.wsgi --daemon
#gunicorn -certfile=server.crt --keyfile=server.key --bind 172.31.19.120:8000 jayWebsite.wsgi --daemon
```
