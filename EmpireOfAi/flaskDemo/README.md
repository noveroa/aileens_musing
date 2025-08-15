
## Cambridge, MA

![N|Solid](https://ca.slack-edge.com/T0495HV8H-U01AM69UW3E-ae635702c574-72)

> A simple musing on combining some simply LLM models (ie chatGpt completion as a first iteratoin ) FlaskApp, 

Absolutely nothing fancy.  eventually i will restructure and i'll use blueprints and maybe keep building some stuff
 run make and then at local 8080 you cna hit /generateTest
###### 

# Running the application

From the command line:
```
make run
.. this will run local port 8080
http://127.0.0.1:8080/

http://127.0.0.1:8080/test
* its working
http://127.0.0.1:8080/testGenerate
* runs chatgpt with input text Once upon a time
http://127.0.0.1:88080...

flaskDemo/
├── genAiEnv/             # Python virtual environment
├── Makefile              # Set of instructions for maketo build project
├──                  # Main application package
│   ├── __init__.py       # Initializes the Flask app and registers blueprints
│   ├── run.py            # Entry point to run the application; where blueprints are registered
│   │   └── ...
│   ├── main/             # Main
│   │   ├── __init__.py         
│   │   ├── auth.py             # initial auth work
│   │   └── routes.py           # initial auth work
│   └── templates/          # HTML templates for basic rendering
│       ├── base.html
│       ├── ...
├── config.py             # Application configuration settings
├── requirements.txt      # Project dependencies
└── .flaskenv             # Environment variables for Flask CLI (optional)