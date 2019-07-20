import os

from celery import Celery


def create_celery_app():
    BROKER_URL = os.environ.get('BROKER_URL')
    celery_app = Celery(__name__, broker=BROKER_URL)
    return celery_app


celery_app = create_celery_app()
