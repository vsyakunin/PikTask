import pytest
from webapp import create_app

@pytest.fixture(scope = 'module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    yield testing_client
 