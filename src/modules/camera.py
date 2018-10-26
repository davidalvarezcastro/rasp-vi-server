import cv2

from ..utils.util import set_interval

# Globals
PATH_PHOTOS = '/home/david/Desktop/test.jpg'
CAMERA = None
CAMERA_STOPPED = None

def shoot_camera_by_id(id):
  """Take a photo for a specific camera and write it to {PATH_PHOTOS}

  Param arguments:
    id -- camera id
  Return: None
  """
  global CAMERA, CAMERA_STOPPED
  try:
    # Get image and write it
    return_value,image = CAMERA.read()
    cv2.imwrite(PATH_PHOTOS,image)
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
  global CAMERA
  CAMERA = None
  CAMERA = cv2.VideoCapture(num_cam) #VideoCapture Management

  # Simple shoot / multiple shoots
  if(not loop):
    shoot_camera_by_id(num_cam)
    return True
  else:
    set_interval(shoot_camera_by_id, [num_cam], delay, time)
    return True
  return False

def handle_stop_camera():
  """Handle camera shooting (multiples photos or just one)

  Param arguments:
    None
  Return: None [this event will generate an exception inside handle_shoot_camera]
  """
  global CAMERA, CAMERA_STOPPED
  CAMERA.release()
  CAMERA = None #Value changed to generate the exception
  CAMERA_STOPPED = True