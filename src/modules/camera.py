import cv2

from ..utils.util import set_interval, get_folder, image_data_to_json
from ..settings import APP_PHOTOS

# Globals
CAMERA = None
CAMERA_STOPPED = None #Variable to stop video capturing method
CAMERA_TO_STOP = None

def shoot_camera_by_id(id):
  """Take a photo for a specific camera and write it to {APP_PHOTOS}

  Param arguments:
    id -- camera id
  Return: None
  """
  global CAMERA, CAMERA_STOPPED, CAMERA_TO_STOP
  try:
    if(CAMERA_STOPPED and (id == CAMERA_TO_STOP)):
      CAMERA_TO_STOP = None
      CAMERA.release()
      raise Exception #Stop process
    CAMERA = None
    CAMERA = cv2.VideoCapture(id) #VideoCapture Management
    # Get image and write it
    return_value,image = CAMERA.read()
    cv2.imwrite(get_folder(APP_PHOTOS, 'test_{}.jpg'.format(id)),image)
  except Exception as e:
    # Controlled exception
    raise Exception('OK', 'Process stopped!') if CAMERA_STOPPED else Exception(e)


def handle_shoot_camera(num_cam, loop = False, delay = None, time = None):
  """Handle camera shooting (multiples photos or just one)

  Param arguments:
    num_cam -- camera id
    loop -- allow the camera to take continually photos (loop)
    delay -- delay between shootings
    time -- duration of the loop
  Return: None
  """
  global CAMERA, CAMERA_STOPPED
  CAMERA_STOPPED = None
  CAMERA_TO_STOP = None

  # Simple shoot / multiple shoots
  if(not loop):
    shoot_camera_by_id(num_cam)
  else:
    set_interval(shoot_camera_by_id, [num_cam], delay, time)

  CAMERA.release()
  CAMERA = None
  return True

def handle_stop_camera(num_cam):
  """Handle camera shooting (multiples photos or just one)

  Param arguments:
    num_cam -- camera id
  Return: None [this event will generate an exception inside handle_shoot_camera]
  """
  global CAMERA_STOPPED, CAMERA_TO_STOP

  CAMERA_TO_STOP = int(num_cam)
  CAMERA_STOPPED = True

def handle_get_photo_as_image(num_cam):
  """Handle get latest photo

  Param arguments:
    num_cam -- camera id
  Return: None
  """
  filename = 'test_{}.jpg'.format(num_cam)
  return (get_folder(APP_PHOTOS, filename), filename, 'image/jpg')

def handle_get_photo(num_cam):
  """Handle get latest photo

  Param arguments:
    num_cam -- camera id
  Return: None
  """
  return image_data_to_json(get_folder(APP_PHOTOS, 'test_{}.jpg'.format(num_cam)))