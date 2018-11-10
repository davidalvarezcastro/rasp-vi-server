# RASP-VI-SERVER
rasp-vi-server is a very simple and small project for playing with Flask and OpenCV technologies.

## List of project folders
```bash
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── manage.py
├── run.py
└── src
    ├── __init__.py
    ├── app.py
    ├── config.py
    ├── documentation
    │   └── camera
    │       ├── get_photo.yml
    │       ├── get_photo_as_image.yml
    │       ├── shoot_camera.yml
    │       └── stop_shoot_camera.yml
    ├── models
    │   └── __init__.py
    ├── modules
    │   ├── __init__.py
    │   └── camera.py
    ├── photos
    ├── settings.py
    ├── static
    │   └── style.css
    ├── templates
    │   └── index.html
    ├── utils
    │   ├── __init__.py
    │   └── util.py
    └── views
        ├── __init__.py
        └── camera.py
```


## Steps to setup it [DEVELOPMENT]
1. `export FLASK_ENV=development`
2. Execute `python run.py` in a development environment.
3. To see the API documentation enter the next url: `http://localhost:5000/apidocs/`

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
          'num_cam': 1,
          'loop': True,
          'delay': 5000,
          'time': 20000
        }
      ``` 
2. Stop the video capturing process [*POST*] `/api/v1/camera/stop/<num_cam>` for a specific camera id.
3. Get the latest photo [*GET*] `/api/v1/camera/get_photo_as_image/<num_cam>`. As you can see, this function just read the latest picture taken (the new picture overwrites the old one) returnign the photo itself.
4. Get the latest photo [*GET*] `/api/v1/camera/get_photo/<num_cam>` -like the previous api- but returning the image as a based64 string.

## **Notes**
Still developing features.