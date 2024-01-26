import pytest
import requests
import allure
from json import load, dumps
from loguru import logger
from typing import Dict, Any

logger.add('debug.log', format='{time} {level} {message}', level='INFO')


# Создание сессии
session = requests.Session()

# Отключение верификации сертификата
session.verify = False

url = 'lk-conductor.api.monitor-utm.ru'
# url = 'lk-test.egais.ru'
def get_token() -> Dict[str, str]:
    token = session.get('http://lk-test.egais.ru/lk-conductor/tools/token?role=developer')
    headers = {
        'accept': '*/*',
        'Authorization': token
    }
    return headers

@pytest.mark.get_methods
@pytest.mark.corr_methods
@pytest.fixture(autouse=True)
def token():
    return get_token()
@pytest.mark.parametrize('endpoint',
    [
        f'http://{url}/lk-conductor/dashboard/conductor/corr/1',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/1/diagram',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/1594/downLoad?checkId=3',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/1/downLoadAttFilesInZip',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/attachmentFile/1',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/correctionsWithPagination?page=0&size=10',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/monitoring/aggregateIndicators?dateFrom=2023-01-01&dateTo=2024-01-26',
        f'http://{url}/lk-conductor/dashboard/conductor/corr/monitoring/statsByTypeOfDelivery?dateFrom=2023-01-01&dateTo=2024-01-26'


    ]
)
def test_gets_corr(endpoint: str) -> None:
    logger.debug(f'Start gets method with endpoint - {endpoint}')
    try:
        headers = token
        result = session.get(endpoint, verify=False)
        logger.info(f"Got result - {result} from endpoint - {endpoint}")
    except Exception as error:
        logger.error(f'Got ERROR - {error}')


@pytest.mark.post_methods
@pytest.mark.corr_methods
@pytest.fixture(autouse=True)
def token():
    return get_token()
@pytest.mark.parametrize('endpoint, json_data',
    [
        (f'http://{url}/lk-conductor/dashboard/conductor/corr/1593', {"branch":"МРУ Росалкогольрегулирования по ЦФО","checkId":5,"docDate":"2023-10-26","docNumber":"92100882","email":"test@mail.ru","inn":"7714698320","kpp":"271744622","orgName":"ООО СИМЭНЕРГО","sadDate":"2024-01-24","sadNum":"56284802","status":2002}),
        (f'http://{url}/lk-conductor/dashboard/conductor/corr/1594/letter', {"branch":"МРУ Росалкогольрегулирования по ЦФО","docDate":"2024-01-24","docNumber":"92100882","email":"test@mail.ru","inn":"7714698320","orgName":"ООО СИМЭНЕРГО","sadDate":"2024-01-24","sadNum":"56284802"}),
    ]
)
def test_posts_corr(endpoint: str, json_data: Dict[str, Any]) -> None:
    logger.debug(f'Start posts method with endpoint - {endpoint}')
    try:
        headers = token
        result = session.post(endpoint, json=json_data, verify=False)
        logger.info(f"Got result - {result} from endpoint - {endpoint}")
    except Exception as error:
        logger.error(f'Got ERROR - {error}')


@pytest.mark.put_methods
@pytest.mark.corr_methods
@pytest.fixture(autouse=True)
def token():
    return get_token()
@pytest.mark.parametrize('endpoint',
    [f'http://{url}/lk-conductor/dashboard/conductor/corr/changeValueIsVerified/1']
)
def test_puts_corr(endpoint: str) -> None:
    logger.debug(f'Start puts method with endpoint - {endpoint}')
    try:
        headers = token
        result = session.post(endpoint, verify=False)
        logger.info(f"Got result - {result} from endpoint - {endpoint}")
    except Exception as error:
        logger.error(f'Got ERROR - {error}')



@pytest.mark.get_methods
@pytest.mark.info_methods
@pytest.fixture(autouse=True)
def token():
    return get_token()
@pytest.mark.parametrize('endpoint',
    [
        f'http://{url}/lk-conductor/dashboard/conductor/info/253',
        f'http://{url}/lk-conductor/dashboard/conductor/info/253/diagram',
        f'http://{url}/lk-conductor/dashboard/conductor/info/infoWithPagination?page=0&size=20',
        f'http://{url}/lk-conductor/dashboard/conductor/info/monitoring/aggregateIndicators?dateFrom=2023-01-01&dateTo=2024-01-26',
        f'http://{url}/lk-conductor/dashboard/conductor/info/monitoring/statsByTypeOfDelivery?dateFrom=2023-01-01&dateTo=2024-01-26',
    ]
)
def test_gets_info(endpoint: str) -> None:
    logger.debug(f'Start gets method with endpoint - {endpoint}')
    try:
        headers = token
        result = session.get(endpoint, verify=False)
        logger.info(f"Got result - {result} from endpoint - {endpoint}")
    except Exception as error:
        logger.error(f'Got ERROR - {error}')


@pytest.mark.post_methods
@pytest.mark.info_methods
@pytest.fixture(autouse=True)
def token():
    return get_token()
@pytest.mark.parametrize('endpoint, json_data',
    [
        (f'http://{url}/lk-conductor/dashboard/conductor/info/253', {"docDate":"2023-12-29","docNumber":"1323","email":"test@mail.ru","inn":"1234567891","orgName":"test","sadDate":"2024-01-26","sadNum":"123321","status":2002}),
        (f'http://{url}/lk-conductor/dashboard/conductor/info/253/uploadZip', {"email":"test@mail.ru","inn":"1233214567"}),
    ]
)
def test_posts_info(endpoint: str, json_data: Dict[str, Any]) -> None:
    logger.debug(f'Start posts method with endpoint - {endpoint}')
    try:
        headers = token
        if 'uploadZip' in endpoint:
            files = {
                'zip': ('EGAIS.zip', open('EGAIS.zip', 'rb'), 'application/zip'),
            }
            result = session.post(endpoint, params=json_data, files=files, verify=False)
        else:
            result = session.post(endpoint, json=json_data, verify=False)
        logger.info(f"Got result - {result} from endpoint - {endpoint}")
    except Exception as error:
        logger.error(f'Got ERROR - {error}')



