import pytest
from json import load, dumps
from fixtures import test_json, test_kafka
from random import randint
# command for runnig test in remote server "python -m pytest"
# 99999999, corrector-epgu, Сведения о поставке, 010000000047, 7714698320, 271744622

result = randint(11111111, 99999999)

@pytest.mark.all_cases
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'brewers-service', 'Сведения о поставке', '010000000047', '7714698320', '271744622'),
    (result, 'info-epgu', 'TEST', '010000000047', '7714698320', '271744622'),
    (result, 'info-epgu', 'Сведения о поставке', '010000000047', '1112223334', '444555666'),
    (result, 'info-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_all_cases(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.first_case  # Отправка некорретного serviceId.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'brewers-service', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_first_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.second_case  # Отправка некорретного typeDoc.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'info-epgu', 'TEST', '010000000047', '7714698320', '271744622')
])
def test_second_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.third_case  # Отправка "inn" и "kpp", которых нет в таблице org_history.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'info-epgu', 'Сведения о поставке', '010000000047', '1112223334', '444555666')
])
def test_third_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.positive
@pytest.mark.forth_case  #  Получение ошибки при регистрации в СЭД.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'info-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_forth_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True





