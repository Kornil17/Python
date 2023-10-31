import requests

class Token:
    @staticmethod
    def get_token():
        return requests.get('http://lk-test.test-kuber-nd.fsrar.ru/api-lc-license/tools/token?role=developer', headers={'accept': '*/*'}).text