import pytest
from json import load, dumps
from fixtures import test_json, test_kafka
from random import randint
# command for runnig test in remote server "python -m pytest"
# 99999999, corrector-epgu, Сведения о поставке, 010000000047, 7714698320, 271744622

result = [randint(11111111, 99999999) for _ in range(4)]
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'domain-info', 'Сведения о поставке', '010000000047', '7714698320', '271744622'),
    (result, 'corrector-epgu', 'test', '010000000047', '7714698320', '271744622'),
    (result[0], 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000000', '1111111111', '333333333'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_values(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(result_json.result)
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result)) == True






