import requests
from create_json import Create
from GetToken import Token


class Request:
    """class for request to endpoint /dashboard/conductor/consideration/with-pagination"""

    def __init__(self):
        """for test"""
        self.path = 'http://lk-test.egais.ru/lk-conductor/dashboard/conductor/corr/correctionsWithPagination'
        # self.token = Token.get_token()
        self.token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsYXN0TmFtZSI6IkF1dG8iLCJmaXJzdE5hbWUiOiJBdXRvIiwicmVnaW9uQ29kZSI6Ijc3Iiwicm9sZSI6ImRldmVsb3BlciIsInBlcm1pc3Npb25zIjoiUmV0YWlsIiwicm9sZWlkIjoiMCIsImxvY2FsaXR5IjoiQXV0byIsInJlZ2lvbiI6IkF1dG8iLCJ1c2VyaWQiOiIxMjMifQ.lD9tvdwoWBYWedm4hBWdWCf73Ea-TMMpCCSaifZ6qdk-S9_TrEKbzD6F4dVPXKigTc28jPeDTRhZQ1Lpu2t9fg'
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