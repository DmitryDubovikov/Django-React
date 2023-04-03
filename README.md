# Django-React

## Project description:

This project is 1/2 test assignment and 1/2 pet project for skills development and demonstration.

Users can register, write posts, add likes and comments.

## Technologies used: 
* Django, 
* Django REST framework, 
* docker, docker-compose for containerization,
* drf-spectacular for swagger docs,
* pytest-django for testing,
* djangorestframework-simplejwt for JWT auth,
* django-cors-headers,
* React,
* react-bootstrap,
* axios, axios-auth-refresh package for HTTP requests.

## How to run:

Run containers:

    docker-compose build
    docker-compose up

Run in docker:    
    python manage.py migrate

Register:

    http://127.0.0.1:3000/register/

Write some posts, add comments and likes:

    http://127.0.0.1:3000/

Check swagger docs for more:

    http://127.0.0.1:8000/api/swagger/docs/


![image](https://github.com/DmitryDubovikov/Django-React-Blogs/blob/main/blogs.jpg)
