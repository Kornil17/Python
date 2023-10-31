import pytest
from json import load, dumps
from fixtures import test_json, test_kafka
# command for runnig test in remote server "python -m pytest"
# 99999999, corrector-epgu, Сведения о поставке, 010000000047, 7714698320, 271744622

@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    ('77777777', 'domain-info', 'Сведения о поставке', '010000000047', '7714698320', '271744622'),
    ('12312311', 'corrector-epgu', 'test', '010000000047', '7714698320', '271744622'),
    ('77777777', 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622'),
    ('32132122', 'corrector-epgu', 'Сведения о поставке', '010000000000', '1111111111', '333333333'),
    ('54334566', 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_values(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(result_json.result)
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result)) == True




