# Features (service)

* Features is a BDD collaboration tool bringing technical and non-technical people together to work on Scenarios.

## Features... so meta

* Auto import of feature files from Git (SSH or https)
* View feature files with auto Gherkin colour highlighting
* Multiple project support per user

## Technologies
* Python 3.x
* [Django](http://www.djangoproject.com)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [Celery](http://www.celeryproject.org/) & [Redis](https://redis.io/)
* [Postgresql](http://www.postgresql.com/)

### Client-side

See https://github.com/ademuk/features#technologies

## Installation

### Dependencies
```
$ pip install -r requirements.txt
```

### Install Postgresql
```
$ brew install postgresql
```

### Install Redis
```
$ brew install redis
```

### Create Feature DB
```
$ createdb features
$ python manage.py createsuperuser
$ python manage.py migrate
```

### Set environment vars
```
DATABASE_URL=postgres://<psql_host>:<psql_port>/features
REDIS_URL=redis://<redis_host:<redis_port>/0
SECRET_KEY=<django_secret_key> #See https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY

ALLOWED_HOSTS=<service_hostname> # i.e. features-service.appyharry.com
CORS_ORIGIN_WHITELIST=<client_hostname>:<client_port> # i.e. features.appyharry.com:80
```

### Starting service and worker
```
$ pip install honcho
$ honcho start
```
