import pytest
from kafkin import Kafka
from get_response_json import JSON
from parse_json import Parse


name = str(input('get file_name: rf, fias, op:\n'))
@pytest.fixture
def test_kafka():
    return Kafka()

@pytest.fixture(params=[name])
def test_json(request):
    print('it is fixture')
    print(request.param)
    return JSON(request.param)

@pytest.fixture
def parse_json():
    return Parse()


