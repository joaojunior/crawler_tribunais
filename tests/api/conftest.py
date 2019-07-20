import pytest

from api import app


@pytest.fixture
def client():
    app.app_flask.config['TESTING'] = True
    client = app.app_flask.test_client()

    yield client
