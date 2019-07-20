from flask_marshmallow import Marshmallow

from models import Process

ma = Marshmallow()


class ProcessSchema(ma.ModelSchema):
    class Meta:
        model = Process
