import pytest
from json import load, dumps
from fixtures import test_json, test_kafka
from random import randint
# command for runnig test in remote server "python -m pytest"
# 99999999, corrector-epgu, Сведения о поставке, 010000000047, 7714698320, 271744622

result = randint(11111111, 99999999)

@pytest.mark.all_cases
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp, branch', [
    (result, 'domain-info', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО'),
    (result, 'corrector-epgu', 'test', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО'),
    ('44444444', 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000000', '1111111111', '333333333', 'МРУ Росалкогольрегулирования по ЦФО'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'test'),
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО')
])
def test_all_cases(orderID, serviceId, typeDoc, fsrar, inn, kpp, branch, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp).set_branch(branch)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.first_case  # Отправка некорретного serviceId.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'domain-info', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
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
    (result, 'corrector-epgu', 'test', '010000000047', '7714698320', '271744622')
])
def test_second_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.third_case  # Отправка  повторного docNum.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    ('44444444', 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_third_case(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.forth_case  #  Организации нет в таблице org_history.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000000', '1111111111', '333333333')
])
def test_forth_case1(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.positive
@pytest.mark.forth_case  #  Организация есть в таблице org_history.
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp', [
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622')
])
def test_forth_case2(orderID, serviceId, typeDoc, fsrar, inn, kpp, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True
@pytest.mark.negative
@pytest.mark.fifth_case  #  Если данные из branch (поле в documentsCorrection) не найдены в справочнике .
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp, branch', [
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'test')
])
def test_fifth_case1(orderID, serviceId, typeDoc, fsrar, inn, kpp, branch, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp).set_branch(branch)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True

@pytest.mark.positive
@pytest.mark.fifth_case  #  Если данные из branch (поле в documentsCorrection) не найдены в справочнике .
@pytest.mark.parametrize('orderID, serviceId, typeDoc, fsrar, inn, kpp, branch', [
    (result, 'corrector-epgu', 'Сведения о поставке', '010000000047', '7714698320', '271744622', 'МРУ Росалкогольрегулирования по ЦФО')
])
def test_fifth_case2(orderID, serviceId, typeDoc, fsrar, inn, kpp, branch, test_json, test_kafka):
    result_json = test_json
    result_json.set_uuid().set_date().set_docid(orderID).set_serviceId(serviceId).set_typeDoc(typeDoc).set_fsrar(fsrar).set_inn(inn).set_kpp(kpp).set_branch(branch)
    print(dumps(result_json.result, ensure_ascii=False))
    kafka = test_kafka
    assert kafka.produce(dumps(result_json.result, ensure_ascii=False)) == True




