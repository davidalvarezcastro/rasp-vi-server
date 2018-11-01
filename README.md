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
│   ├── photos
│   ├── __pycache__
│   │   ├── app.cpython-36.pyc
│   │   └── __init__.cpython-36.pyc
│   ├── settings.py
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
  
    Should you want to run under *multiple pictures* mode, you may need to specify the delay between the pictures and the total time execution. There are values by default where the user specifies `loop = True`:
    - Default values for looping:
      ```python
        parameters = {
          'delay': 1000,
          'time': -1
        }
      ```
      If `time = -1`, the process runs infinitely.
    - Parameters example:
      ```python
        parameters = {
          'camera': 1,
          'loop': True,
          'delay': 5000,
          'time': 20000
        }
      ``` 
2. Stop the video capturing process [*POST*] `/api/v1/camera/stop/<num_camera>` for a specific camera id.
3. Get the latest photo [*GET*] `/api/v1/camera/get_photo_as_image/<num_camera>`. As you can see, this function just read the latest picture taken (the new picture overwrites the old one) returnign the photo itself.
4. Get the latest photo [*GET*] `/api/v1/camera/get_photo/<num_camera>` -like the previous api- but returning the image as a based64 string.

## **Notes**
Still developing features.