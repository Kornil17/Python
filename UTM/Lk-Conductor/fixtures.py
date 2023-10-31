import pytest
from create_json import Create
from get_consideration import Request
@pytest.fixture
def test_json():
    return Create()

@pytest.fixture
def test_request():
    return Request()