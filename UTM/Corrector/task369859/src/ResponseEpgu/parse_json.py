import json
from datetime import datetime
import os
class Parser:
    """class for parse request json"""
    def __init__(self) -> None:
        self.js = self.open_file('request')
        self.response_json = self.open_file('response')
    def open_file(self, type: str)->dict:
        # with open(f'/home/kornilov/PycharmProjects/Python/UTM/Corrector/task369859/src/test_data/{type}.json', 'r', encoding='utf8') as file:
        print(os.getcwd())
        with open(f'./src/test_data/{type}.json', 'r', encoding='utf8') as file:
            js = json.load(file)
        return js

    def get_id(self)->str:
        return self.js['request'][0]['service_id']

    def get_requestId(self)->str:
        return self.js['request'][0]['request_id']

    def get_updateTimestamp(self)->str:
        return str(datetime.utcnow())

    def get_serviceStatus(self)->str:
        return str(input('Введите статус заявления "2002" или "2003"\n'))

    def get_caseNumber(self)->str:
        return str(input('Введите номер заявления\n'))

    def get_path(self)->str:
        return str(input('Введите путь до файла\n'))
    def get_response_json(self)->dict:
        self.response_json['serviceId'] = self.get_id()
        self.response_json['requestId'] = self.get_requestId()
        self.response_json['updateTimestamp'] = self.get_updateTimestamp()
        self.response_json['responseContent']['serviceStatus'] = self.get_serviceStatus()
        self.response_json['responseContent']['caseNumber'] = self.get_caseNumber()
        self.response_json['responseContent']['attachments'][0]['path'] = self.get_path()
        return self.response_json

# test = Parser()
# test.get_response_json()
# print(test.response_json)
