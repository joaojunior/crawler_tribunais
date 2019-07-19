from uuid import uuid4
import zlib

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property


db = SQLAlchemy()


class RawHTML(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4)
    number = db.Column(db.String(25))
    grade = db.Column(db.Integer)
    _html = db.Column(db.LargeBinary)

    @hybrid_property
    def html(self) -> str:
        return zlib.decompress(self._html).decode('utf-8')

    @html.setter
    def html(self, html: str):
        self._html = zlib.compress(html.encode('utf-8'))


class Process(db.Model):
    number = db.Column(db.String(25), primary_key=True)
    grade1 = db.Column(JSONB)
    grade2 = db.Column(JSONB)
