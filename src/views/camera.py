
#/src/views/camera

from flask import g, request, Blueprint
from ..utils.util import custom_response, render_template
from ..modules.camera import handle_shoot_camera

camera_api = Blueprint('camera', __name__) #Camera Blueprint

@camera_api.route('/shoot', methods=['POST'])
def shootCamera():
  """Shoot camera.

  Param arguments (Request API):
    num_cam -- camera id
    loop -- allow the camera to take continually photos (loop)
    delay -- delay between shootings
    time -- duration of the loop
  Return: Response
  """
  msg = ''
  code = 201
  delay = None
  time = None
  num_cam = request.args.get('num_cam', default = 0, type = int)
  loop = request.args.get('loop', default = False, type = bool)

  if (loop):
    delay = request.args.get('delay', default = 3000, type = int)
    time = request.args.get('time', default = 10000, type = int)

  # data to return
  parameters = {
    'camera': num_cam,
    'loop': loop and {
      'delay': delay,
      'time': time
    },
  }

  try:
    msg = 'Photo(s) stored!' if handle_shoot_camera(num_cam, loop, delay, time) else 'Something wrong has happened!'
  except Exception as inst:
    msg = 'Something wrong has happened!' + str(inst)
    code = 500
  
  return custom_response({'result': msg, 'parameters': parameters}, code)

@camera_api.route('/getPhoto/<num_camera>', methods=['GET'])
def getPhoto(num_camera):
  """Get latest picture shooted

  Keyword arguments:
  None
  """
  return custom_response({'description': 'get the latest stored picture'}, 201)