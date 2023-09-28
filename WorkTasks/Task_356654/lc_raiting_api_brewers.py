# Task: Task_356654 - Протестировать Endpoint: Оценка качества(изменение оценки)
import os

import requests
import logging
from openpyxl import load_workbook

# test: http://lk-egais.monitor-utm.ru/api-lc-rating/dashboard/rating/updateRating
# sand:
# params = {'advice': '1','chartId': '1','comment': '1','newRate': '1'}
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
class Request:
    headers = {
        'accept': '*/*',
        'Authorization': None,
    }
    def __init__(self, params):

        self.params = params

    def send_requests(self):
        logging.debug('start send function')
        response = requests.patch(
            'http://lk-egais.monitor-utm.ru/api-lc-rating/dashboard/rating/updateRating',
            params=self.params,
            headers=Request.headers,
        )
        logging.debug(response.text)
        logging.debug(response.status_code)


def main():
    logging.debug('start main func')
    for values in params:
        logging.debug('create obj')
        request = Request(values)
        request.send_requests()
def exel(file):
    book = load_workbook(filename=file)
    sheet = book.active
    d = {}
    for st in range(1, 5):
        for row in range(1, 18):
            if row == 1:
                d[sheet[1][st].value] = [sheet[row + 1][st].value]
            else:
                d[sheet[1][st].value].append(sheet[row][st].value)
            # print(sheet[1][st].value)
            # print(sheet[row][st].value)
    print(d)
    return d
def form():
    array = []
    result = {}
    for i in range(len(d['advice'])):
        for key, value in d.items():
            try:
                result[key] = value[i]
                i += 1
            except:
                continue
        array.append(result)
        result = {}
    print(array)
    return array


file = '/home/kornilov/Downloads/Pairwise.xlsx'
d = exel(file)
params = form()
# token = requests.get('http://lk-test.test-kuber-nd.fsrar.ru/api-lc-license/tools/token?role=developer',headers={'accept': '*/*'})
# logging.debug(token.text)
main()
# params = [{'advice': '1', 'chartId': '1', 'comment': '1', 'newRate': '1'},
#           {'chartId': '1', 'newRate': '1'}]

if __name__ == "__main__":
    main()
