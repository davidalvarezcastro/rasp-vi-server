
from flask import json, Response, render_template as render_template_flask

# Rendering template
def render_template(url):
    return render_template_flask(url)

# Customizing api responses
def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )