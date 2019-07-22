import os

from celery import Celery


def create_celery_app():
    BROKER_URL = os.environ.get('BROKER_URL')
    celery_app = Celery('api_celery', broker=BROKER_URL)
    return celery_app
