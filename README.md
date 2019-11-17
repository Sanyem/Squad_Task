# Squad Coding Task



## Problem Statement: 
As part of this activity, you have to create an ESP Game e.g. Artigo is an esp game that is used for tagging.

## Tech Stack

- WebFramework: Django
- Language: python

## Design Document (Schema)
- Design Document is made using the django-extensions. This is an image file named 'schema.png' in the Github Repo


## To run in your own system
- Clone the github repo
- Create a virtual environment
    -- virtualenv -p python3 venv
- Activate venv
    -- source venv/bin/activate
- Go to the project directory
    -- cd Squad_Task
- Install all the requirements from requirements.txt
    -- pip install -r requirements.txt
- Connect with your database (Postgres)
    -- Open postgres in terminal(psql)
    -- CREATE DATABASE squad;
    -- Change database user and name in settings.py
    -- GRANT ALL PRIVILEGES ON DATABASE squad TO user;
- Make migrations
    -- python manage.py makemigrations
    -- python manage.py migrate
- Create Superuser
    -- python manage.py createsuperuser
- Run the django project
    -- python manage.py runserver
- Go to admin panel
    -- url/admin
- Add primary and secondary images under images table
- Run the project(localhost)
    -- url
- Signup
- Login
- Play Game
- Enjoy