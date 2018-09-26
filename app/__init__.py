from flask import Flask, render_template, request
from celery import Celery

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app.controllers.pages import mod_pages as pages_module
from app.controllers.api import mod_api as api_module

app.register_blueprint(pages_module)
app.register_blueprint(api_module)