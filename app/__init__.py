import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
import os

def create_app():
  app = Flask(__name__)
  CORS(app, resources={r"/*": {"origins": "*"}})

  if not os.path.exists('logs'):
    os.mkdir('logs')
  file_handler = RotatingFileHandler(os.path.join('logs', 'app.log'), maxBytes=10240, backupCount=10)
  file_handler.setFormatter(logging.Formatter(
      '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
  ))
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)

  if not app.debug and not app.testing:
    app.logger.setLevel(logging.INFO)
    app.logger.info('Application startup')
  

  from .routes import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app