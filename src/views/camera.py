
#/src/views/camera

from flask import g, request, Blueprint
from flask_restplus import inputs
from ..utils.util import custom_response, render_template, custom_response_file
from ..modules.camera import handle_shoot_camera, handle_stop_camera, handle_get_photo_as_image, handle_get_photo
from flasgger import swag_from

import io

camera_api = Blueprint('camera', __name__) #Camera Blueprint

@camera_api.route('/shoot', methods=['POST'])
@swag_from('../documentation/camera/shoot_camera.yml')
def shoot_camera():
  """Shoot camera.

  Param arguments (Request API):
    num_cam -- camera id
    loop -- allow the camera to take continually photos (loop)
    delay -- delay between shootings
    time -- duration of the loop
  Return: Response
  """
  msg = ''
  code = 200
  delay = None
  time = None
  num_cam = request.args.get('num_cam', default = 0, type = int)
  loop = request.args.get('loop', default = False, type = inputs.boolean)

  if (loop):
    delay = request.args.get('delay', default = 3000, type = int)
    time = request.args.get('time', default = -1, type = int)

  try:
    msg = 'Photo(s) stored!' if handle_shoot_camera(num_cam, loop, delay, time) else 'Something wrong has happened!'
  except Exception as inst:
    obj = inst.args
    """When we stop the process a Exception will be thrown. We need to
    handle it properly
    """
    if(obj[0] == 'OK'):
      msg = 'Photo(s) stored!' + ' ' + str(obj[1])
    else:
      msg = 'Something wrong has happened!' + str(inst)
      code = 500
  
  return custom_response({'message': msg}, code)

@camera_api.route('/stop/<num_cam>', methods=['POST'])
@swag_from('../documentation/camera/stop_shoot_camera.yml')
def stop_shoot_camera(num_cam):
  """Close video file or capturing device

  Keyword arguments:
    num_cam -- camera id
  Return: Response
  """
  msg = ''
  code = 200

  try:
    handle_stop_camera(num_cam)
    msg = 'Signal send to the process. Capturing process is being stopped!'
  except Exception as inst:
    msg = 'Something wrong has happened!' + str(inst)
    code = 500

  return custom_response({'message': msg}, code)

@camera_api.route('/get_photo_as_image/<num_cam>', methods=['GET'])
@swag_from('../documentation/camera/get_photo_as_image.yml')
def get_photo_as_image(num_cam):
  """Get latest picture shooted

  Keyword arguments:
    num_cam -- camera id
  Return: Response
  """
  path, filename, mimetype = handle_get_photo_as_image(num_cam)
  try:
    return custom_response_file(path, filename, mimetype)
  except Exception as inst:
    msg = 'Something wrong has happened!' + str(inst)
    code = 500
    return custom_response({'message': msg}, code)

@camera_api.route('/get_photo/<num_cam>', methods=['GET'])
@swag_from('../documentation/camera/get_photo.yml')
def get_photo(num_cam):
  """Get latest picture shooted (as json object)

  Keyword arguments:
    num_cam -- camera id
  Return: Response
  """
  msg = ''
  code = 200

  try:
    msg = handle_get_photo(num_cam)
  except Exception as inst:
    msg = 'Something wrong has happened!' + str(inst)
    code = 500

  return custom_response({'message': msg}, code)