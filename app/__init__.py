from flask import Flask, render_template, request
from celery import Celery

import os

app = Flask(__name__)

if os.environ.get('REDIS_HOST'):
    redis = 'redis://{}:6379/0'.format(os.environ.get('REDIS_HOST'))
else:
    redis = 'redis://{}:6379/0'.format('localhost')

print(redis)

app.config['CELERY_BROKER_URL'] = redis
app.config['CELERY_RESULT_BACKEND'] = redis

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app.controllers.pages import mod_pages as pages_module
from app.controllers.api import mod_api as api_module

app.register_blueprint(pages_module)
app.register_blueprint(api_module)