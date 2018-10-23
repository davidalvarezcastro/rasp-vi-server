
from flask import json, Response, render_template as render_template_flask
import threading
import time as t

# Utilities / Helpers
def setInterval(func, args, delay, time):
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