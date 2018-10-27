
from flask import json, Response, send_file, render_template as render_template_flask
import threading
import time as t
import os
from base64 import b64encode
from json import dumps

# Utilities / Helpers
def get_folder(path, filename):
  """Get project folder

  Param arguments:
    path -- path
    filename -- filename
  Return: string
  """
  return os.path.join(path, filename)

def set_interval(func, args, delay, time):
  """Set interval with cancel process based on time

  Param arguments:
    func -- function to execute
    args -- extra arguments for func [i.e camera id]
    delay -- time between executions (ms)
    time -- total time execution (ms)
  Return: 
  """
  start = t.time()
  while True:
    e = threading.Event()
    while not e.wait(delay/1000):
      func(*args)
      if t.time() > start + (time/1000) : break
    break
  
def image_data_to_json(picture_path):
  """Get the image date into a json object

  Param arguments:
    picture_path -- path
  Return: JSON
  """
  with open(picture_path, "rb") as image_file:
    byte_content = image_file.read()

  base64_bytes = b64encode(byte_content)
  base64_string = base64_bytes.decode('utf-8')
  raw_data = base64_string
  return dumps(raw_data)

# View stuff: templates, responses
def render_template(url):
  """Render a template

  Param arguments:
    url -- url to render
  Return: Template rendered
  """
  return render_template_flask(url)

def custom_response(res, status_code):
  """Custom Response Function

  Param arguments:
    res -- json response
    status_code -- code
  Return: Response
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

def custom_response_file(path, filename, mimetype):
  """Custom Response Function (send file)

  Param arguments:
    path -- url
    filename -- name
    mimetype -- type
  Return: send_file
  """
  return send_file(path, attachment_filename=filename, mimetype=mimetype)
