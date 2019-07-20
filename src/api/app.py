from flask import Flask
from flask_restful import Api

from celery_app import celery_app
from models import db
from resources import ProcessResource
from schemas import ma


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    ma.init_app(app)
    db.init_app(app)
    api = Api(app)
    api.add_resource(ProcessResource, '/<string:process_number>')
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask

    return app


app_flask = create_app()


if __name__ == '__main__':
    app_flask = create_app()
    app_flask.run()
