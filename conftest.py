import pytest

from common.client import APIclient


@pytest.fixture
def api_client():
    client = APIclient()
    yield client
    client.close()
