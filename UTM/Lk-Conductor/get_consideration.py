import requests
from create_json import Create
from GetToken import Token


class Request:
    """class for request to endpoint /dashboard/conductor/consideration/with-pagination"""

    def __init__(self):
        """for test"""
        self.path = 'https://lk-test.egais.ru/lk-conductor/dashboard/conductor/consideration/with-pagination'
        self.token = Token.get_token()
        self.headers = {
            'accept': '*/*',
            'Authorization': self.token
        }
    # def __init__(self):
    #     """for sand"""
    #     self.path = "https://lk-conductor.api.monitor-utm.ru/dashboard/conductor/consideration/with-pagination"
    #     self.token = Token.get_token()
    #     self.headers = {
    #         'accept': '*/*',
    #         'Authorization': self.token
    #     }
    #     self.parametrs = {'filter': '1','page': '1','size': '1','sort': '1'}
    # def get_result(self):
    #     response = requests.get(
    #         self.path,
    #         params=self.parametrs,
    #         headers=self.headers,
    #     )
    #     print(response.text, response.status_code)

# test = Request()
# # test.get_result()
# print(test.token)