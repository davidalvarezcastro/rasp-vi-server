from flask import Flask, g #flask
from .config import app_config #app config
from .utils.util import render_template
from .views.CameraHandling import camera_api as camera_blueprint #view
from flask_bootstrap import Bootstrap #bootstrap

# Creating app
def create_app(env_name):
  """Create app

  Keyword arguments:
    env_name -- enviroment ('development or production')
  """

  # app init
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  app.register_blueprint(camera_blueprint, url_prefix='/api/v1/camera') #registering camera api

  # boostrap init
  Bootstrap(app)
  
  # / url [home page]
  @app.route('/index')
  @app.route('/', methods=['GET'])
  def index():
    """Home API page

    Keyword arguments:
    None
    """

    return render_template('index.html')

  return app