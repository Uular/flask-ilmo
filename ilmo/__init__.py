import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object('mysecret')
app.jinja_env.add_extension("jinja2.ext.do")
db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(os.path.join(basedir, '..', 'warning.log'))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

from ilmo import views, models
