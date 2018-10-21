
#/src/views/CameraHandling

from flask import g, request, Blueprint
from ..utils.util import custom_response, render_template

camera_api = Blueprint('camera', __name__) #Camera Blueprint

@camera_api.route('/shoot', methods=['GET'])
def shootCamera():
  """Shoot camera.

  Keyword arguments:
  None
  """
  return custom_response({'description': 'send signal to camera to take a photo'}, 201)

@camera_api.route('/get', methods=['GET'])
def getPhoto():
  """Get latest picture shooted

  Keyword arguments:
  None
  """
  return custom_response({'description': 'get the latest stored picture'}, 201)