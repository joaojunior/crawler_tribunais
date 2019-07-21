import pytest

from api import app


@pytest.fixture
def client():
    app.app_flask.config['TESTING'] = True
    client = app.app_flask.test_client()

    with app.app_flask.app_context():
        app.db.create_all()
        client.db = app.db
        yield client
        # app.db.drop_all()
        meta = app.db.metadata
        for table in reversed(meta.sorted_tables):
            app.db.session.execute(table.delete())
            app.db.session.commit()
