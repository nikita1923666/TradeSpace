import pytest
from app import app

@pytest.fixture
def client():
  with app.test_client() as client:
    yield client

def test_empty_db(client):
  """Checking the hello world route."""
  rv = client.get('/')
  assert b'Hello world' in rv.data
