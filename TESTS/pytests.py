import requests
import pytest

URL = "http://api-lc-gateway.monitor-utm.ru/organizations?search=1&size=10"


class Test_api():
    def test_api1(self, r):
        request = requests.get(URL)
        print("\n", request.text)
        assert request.status_code == 200, "Expected result"
        print(r)


