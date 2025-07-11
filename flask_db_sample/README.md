
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

> A simple musing on combining sqlLite DB with a FlaskApp, RESTful services.
Absolutely nothing fancy.  We use flask blueprints and db models.

###### 

# Running the application

From the command line:
```
make run
.. this will run local port 5000
http://127.0.0.1:5000/

http://127.0.0.1:5000/students/
* new
* edit
* delete
http://127.0.0.1:5000/comments/
* new
* edit
* delete
http://127.0.0.1:8201/projects/
* new
* edit
* delete

 your-flask-app/
├── newenv/               # Python virtual environment
├── Makefile              # Set of instructions for maketo build project
├── app/                  # Main application package
│   ├── __init__.py       # Initializes the Flask app and registers blueprints
│   ├── run.py            # Entry point to run the application; where blueprints are registered
│   ├── database/         # sqlLite DB folder
│   │   ├── __init__.py
│   │   ├── musings_db.db       # sqlLite db
│   │   ├── sqlAlchemy.py       # flask sqlAlchemy configurations
│   │   └── ...
│   ├── main/             # Main
│   │   ├── __init__.py         
│   │   ├── auth.py             # initial auth work
│   │   └── routes.py           # initial auth work
│   ├── models/           # flask DB models
│   │   ├── __init__.py    
│   │   ├── tables.py           # table schemas
│   │   └── ...
│   ├── projects/           # Project Class Misc
│   │   ├── __init__.py    
│   │   ├── routes.py
│   │   └── ...
│   ├── comments/           # Comments Class Misc
│   │   ├── __init__.py    
│   │   ├── routes.py
│   │   └── ...
│   ├── students/           # Students Class Misc
│   │   ├── __init__.py    
│   │   ├── routes.py
│   │   └── ...
│   └── templates/          # HTML templates for basic rendering
│       ├── base.html
│       ├── ...
├── config.py             # Application configuration settings
├── requirements.txt      # Project dependencies
└── .flaskenv             # Environment variables for Flask CLI (optional)