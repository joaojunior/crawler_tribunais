from flask import Flask
from flask_restful import Api

from resources import ProcessResource


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    from models import db
    from schemas import ma
    ma.init_app(app)
    db.init_app(app)
    api = Api(app)
    api.add_resource(ProcessResource, '/<string:process_number>')

    return app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run()
