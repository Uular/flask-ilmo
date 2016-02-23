from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('warning.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

from ilmo import views, models
