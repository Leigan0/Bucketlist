# Bucket List

I have built this app following a [tutorial](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1). I am learning python so I have followed this tutorial to gain experience of python using a framework to create REST API Django app.

This tutorial also builds using a TDD approach.

App is CRUD style app for a Bucket List.

## Technologies Used
* Python3
* Django
* TestCase
* SQlite

## Getting started
* You will need to have python and virtual env installed globally
* git clone https://github.com/Leigan0/bucketlist.git
* cd bucketlist
* Create and fire up your virtual env
```
  $ virtualenv  venv -p python3
  $ source venv/bin/activate
```
* Install dependencies
```
$ pip install -r requirements.txt
```
* Run migrations
```
  $ python manage.py makemigrations
  $ python manage.py migrate
```
* Run app
```
  $ python manage.py runserver
```
* Navigate to  http://localhost:8000/

## To run tests
* cd djangorest
```
  $ python3 manage.py test
  ```

Django uses SQlite as default, so I have also used this.
