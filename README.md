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
- Create a virtual environment <br />
    -- virtualenv -p python3 venv
- Activate venv <br />
    -- source venv/bin/activate
- Go to the project directory <br />
    -- cd Squad_Task
- Install all the requirements from requirements.txt <br />
    -- pip install -r requirements.txt
- Connect with your database (Postgres) <br />
    -- Open postgres in terminal(psql) <br />
    -- CREATE DATABASE squad; <br />
    -- Change database user and name in settings.py <br />
    -- GRANT ALL PRIVILEGES ON DATABASE squad TO user; <br />
- Make migrations <br />
    -- python manage.py makemigrations <br />
    -- python manage.py migrate
- Create Superuser <br />
    -- python manage.py createsuperuser
- Run the django project <br />
    -- python manage.py runserver
- Go to admin panel <br />
    -- url/admin
- Add primary and secondary images under images table
- Run the project(localhost) <br />
    -- url
- Signup
- Login
- Play Game
- Enjoy