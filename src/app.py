from flask import Flask, g #flask
from .config import app_config #app config
from .utils.util import render_template
from .views.camera import camera_api as camera_blueprint #view
from flasgger import Swagger
from flasgger.utils import swag_from

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

  app.config['SWAGGER'] = {
    'title': 'Raspi VI API'
  }
  # Swagger init
  Swagger(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  return app