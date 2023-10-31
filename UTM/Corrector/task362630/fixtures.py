import pytest
from create_json import Create
from kafkin import Kafka
@pytest.fixture
def test_json():
    return Create()

@pytest.fixture
def test_kafka():
    return Kafka()
