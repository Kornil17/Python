import pytest
from json import load, dumps
from fixtures import test_json, test_kafka, parse_json


# {"serviceId":"brewers-service","requestId":"dd45cc73-ccce-4cb5-8d19-a9aa04b55cb1","clientInternalNumber":"3565361655","requestType":"EGRUL","requestContent":{"requestId":"dd45cc73-ccce-4cb5-8d19-a9aa04b55cb1","innUl":"6321357476"}}
jsons = str(input('GET json\n'))
def test_send_egrul(test_kafka, parse_json, test_json):
    parse = parse_json
    print(parse.parse_json(jsons))
    parse_result = parse.parse_json(jsons)
    js = test_json
    js.set_uuid(parse_result).set_client_number(parse_result)
    print(dumps(js.result, ensure_ascii=False))
    # kafka = test_kafka
    # assert kafka.produce(dumps(js.result, ensure_ascii=False)) == True



