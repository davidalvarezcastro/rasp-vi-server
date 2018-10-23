# RASP-VI-SERVER
rasp-vi-server is a very simple and small project for playing with Flask and OpenCV technologies.

## List of project folders
```bash
.
├── LICENSE
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── run.py
├── src
│   ├── app.py
│   ├── config.py
│   ├── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── modules
│   │   ├── camera.py
│   │   └── __init__.py
│   ├── __pycache__
│   │   ├── app.cpython-36.pyc
│   │   └── __init__.cpython-36.pyc
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   └── index.html
│   ├── utils
│   │   ├── __init__.py
│   │   └── util.py
│   └── views
│       ├── camera.py
│       └── __init__.py
└── tests
```


## Steps to setup it [DEVELOPMENT]
1. `export FLASK_ENV=development`
2. Execute `python run.py` in a development environment.

## API List
If you access to the root of the project (web), you may watch a list with the services provided.
1. Shoot the camera [*POST*] `/api/v1/camera/shoot`. You have 2 options to run it: *single picture* or *multiple pictures (loop)*.
  
    Should you want to run under *multiple pictures* mode, you may need to specify the delay between the pictures and the total time execution (there are values by default).
    - Parameters example:
      ```python
        parameters = {
          'camera': 1,
          'loop': True,
          'delay': 5000,
          'time': 20000
        }
      ``` 
2. Get the latest photo [*GET*] `/api/v1/camera/getPhoto/<id>`. As you can see, this function just read the latest picture taken (the new picture overwrites the old one).

## **Notes**
Still developing the service.