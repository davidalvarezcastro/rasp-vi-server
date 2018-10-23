import cv2

from ..utils.util import setInterval

# Globals
PATH_PHOTOS = '/home/david/Desktop/test.jpg'

def shoot_camera_by_id(id):
  """Take a photo for a specific camera

  Param arguments:
    id -- camera id
  Return: None
  """
  camera = cv2.VideoCapture(id)
  return_value,image = camera.read()
  cv2.imwrite(PATH_PHOTOS,image)

def handle_shoot_camera(num_cam, loop = False, delay = None, time = None):
  """Handle camera shooting (multiples photos or just one)

  Param arguments:
    num_cam -- camera id
    loop -- allow the camera to take continually photos (loop)
    delay -- delay between shootings
    time -- duration of the loop
  Return: None
  """
  if(not loop):
    shoot_camera_by_id(num_cam)
    return True
  else:
    # Do something
    setInterval(shoot_camera_by_id, [num_cam], delay, time)
    return True
  return False