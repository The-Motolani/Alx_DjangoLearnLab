# LibraryProject

## Objective

Gain familiarity with Django by setting up a Django development environment and creating a basic Django project.  
This project introduces the workflow of Django projects, including project creation and running the development server.

## Steps Completed

1. Installed Django using `pip install django`.
2. Created new Django project using `django-admin startproject LibraryProject`.
3. Started the development server using `python manage.py runserver`.
4. Opened the browser at `http://127.0.0.1:8000/` to view the default Django welcome page.

## Project Structure

LibraryProject/
│
├── LibraryProject/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
└── manage.py

## Description of Key Files

- **manage.py** – Command-line tool for Django management tasks.
- **settings.py** – Contains project configuration (database, installed apps, etc.)  
- **urls.py** – Maps URLs to views.
- **asgi.py / wsgi.py** – Entry points for ASGI/WSGI web servers.
