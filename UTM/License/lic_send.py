import requests
from datetime import datetime
import logging
import certifi
import ssl
import json
context=ssl.create_default_context(cafile=certifi.where())

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
# /mnt/Dmitriy_test/Documents/reject.pdf
# /home/ldapusers/d_kornilov/scripts/reject.pdf
# curl - curl -X POST "http://10.10.5.202:5005/api/AddRCWithFileAndSig" -H  "accept: text/plain" -H  "Content-Type: multipart/form-data" -F "dueCard=0.LQAL.2P3KT." -F "dueDocgroup=0.LLHZ.LLMU.LYY4.2RUOK.2RUOT." -F "aIsnDelivery=1033658" -F "duePersonExe=0.LVIP.M3PQ.2T78C." -F "aAnnotat=" -F "aNote="
class License:

    """class construction"""
    def __init__(self, address, token, licenseTypeCode, requestTypeCode, inn='7841051711', file=open('/mnt/Dmitriy_test/Documents/reject.pdf', 'rb'), time=datetime.now().strftime("%Y-%m-%d"), orgBriefName="ООО Тестировщик", orgFullName="ООО Тестим", response=""):
        logging.debug("start __init__ function")
        self.address = address
        self.token = token
        self.inn = inn
        self.file = file
        self.time = time
        self.orgBriefName = orgBriefName
        self.orgFullName = orgFullName
        self.resp = response
        self.licenseTypeCode = licenseTypeCode
        self.requestTypeCode = requestTypeCode
        self.due = self.get_due(requestTypeCode)
        self.card = None
        self.headers = {
            'accept': '*/*',
            'Authorization': self.token.text
        }
        self.files = {
                'deloDate': self.time,
                'file': self.file,
                'inn': self.inn,
                'licenseTypeCode': self.licenseTypeCode,
                'orgBriefName': self.orgBriefName,
                'orgFullName': self.orgFullName,
                'requestTypeCode': self.requestTypeCode
            }
        logging.info(f"got parametrs: {self.files, self.headers}")

    def get_due(self, requestTypeCode):
        logging.debug('start get_due func')
        if requestTypeCode == 7:
            logging.debug('got due requestTypeCode == 7')
            return '0.LLHZ.LLMU.LYY4.2RUOK.2RUOT.'
        elif requestTypeCode == 3:
            logging.debug('got due requestTypeCode == 3')
            return '0.LLHZ.LLMU.LYY4.2RUOK.2RUOX.'
        elif requestTypeCode == 2:
            logging.debug('got due requestTypeCode == 2')
            return '0.LLHZ.LLMU.LYY4.2RUOK.2RUP1.'
        else:
            logging.error('invalid requestTypeCode')
            raise ValueError('invalid requestTypeCode')

    def send_card(self):
        self.headers_card = {
            'accept': 'text/plain'
        }

        self.files_card = {
            'dueCard': (None, '0.2R58A.'),
        'dueDocgroup': (None, self.due),
        'aIsnDelivery': (None, '1033658'),
        'duePersonExe': (None, '0.LVIP.M3PQ.2T78C.'),
        'aAnnotat': (None, 'test'),
        'aNote': (None, 'test'),
        }
        logging.info(f'got parametrs send_card function - {self.files_card}')
        try:
            logging.debug('send post request')
            self.card = requests.post('http://10.10.5.202:5005/api/AddRCWithFileAndSig', headers=self.headers_card, files=self.files_card)
            logging.debug(f'get status code - {self.card.text}')
            self.result = self.card.json()
            logging.info(f'get aIsn: {self.result["aIsn"]}')
        except Exception as ex:
            logging.error(ex)
    def send(self):
        try:
            logging.debug('update parametrs')
            self.files.update({'isnDoc':  self.result["aIsn"]})
            logging.debug(f"got self.files: {self.files}")
            logging.debug('start send function')
            self.resp = requests.post(f'http://{self.address}/api-lc-license/dashboard/license/request/', headers=self.headers, files=self.files)
            logging.debug('send post request')
            logging.debug(f'get status code - {self.resp.text}')
        except Exception as ex:
            logging.error('Error!')
            logging.error(ex)
            raise ex


def main():

    """start function"""
    logging.debug("start main function")
    contur = input("Выберите контур для создания документа: test, pred-prod или exit\n").lower()
    logging.info(f"got contur - {contur}")
    if contur not in ['test', 'pred', 'pred-prod', 'exit']:
        raise logging.error('Bad request')
    elif contur == 'exit':
        logging.debug("exit main function")
        logging.info("Всего хорошего!")
    else:
        licenseTypeCode = int(input("Введите номер licenseTypeCode для отправки\n"))
        logging.info(f"got licenseTypeCode - {licenseTypeCode}")
        requestTypeCode = int(input("Введите номер requestTypeCode для отправки\n"))
        logging.info(f"got requestTypeCode - {requestTypeCode}")
        get_inn = int(input("Введите 1-для создания ЮЛ и 2-для создания ИП для отправки\n"))
        logging.info(f"got get_inn - {get_inn}")
        if get_inn == 1:
            inn = '7841051711'
            logging.info(f"got inn - {inn}")
        elif get_inn == 2:
            inn = '771510315518'
            logging.info(f"got inn - {inn}")
    try:
        while contur != 'exit':
            logging.debug("start circle")
            if contur == 'test':
                try:
                    logging.debug("start test contur")
                    token = requests.get('http://lk-test.test-kuber-nd.fsrar.ru/api-lc-license/tools/token?role=developer', headers={'accept': '*/*'})
                    print(token.text)
                    address = 'lk-test.test-kuber-nd.fsrar.ru'
                    send_files = License(address, token, licenseTypeCode, requestTypeCode, inn)
                    print(send_files.send_card())
                    print(send_files.send())
                    contur = input("Выберите контур для создания документа: test, pred-prod или exit\n").lower()
                    if contur == 'exit':
                        logging.debug("exit main function")
                        logging.info("Всего хорошего!")
                        break
                    licenseTypeCode = int(input("Введите номер licenseTypeCode для отправки\n"))
                    logging.info(f"got licenseTypeCode - {licenseTypeCode}")
                    requestTypeCode = int(input("Введите номер requestTypeCode для отправки\n"))
                    logging.info(f"got requestTypeCode - {requestTypeCode}")
                except Exception as ex:
                    logging.error(ex)
            elif contur == 'pred' or contur == 'pred-prod':
                try:
                    logging.debug("start test contur")
                    token = requests.get(
                        'http://lk-egais.pred-kuber-nd.fsrar.ru/api-lc-license/tools/token?role=developer',
                        headers={'accept': '*/*'})
                    print(token.text)
                    address = 'lk-egais.pred-kuber-nd.fsrar.ru'
                    send_files = License(address, token, licenseTypeCode, requestTypeCode, inn)
                    print(send_files.send_card())
                    print(send_files.send())
                    contur = input("Выберите контур для создания документа: test, pred-prod или exit\n").lower()
                    if contur == 'exit':
                        logging.debug("exit main function")
                        logging.info("Всего хорошего!")
                        break
                    licenseTypeCode = int(input("Введите номер licenseTypeCode для отправки\n"))
                    logging.info(f"got licenseTypeCode - {licenseTypeCode}")
                    requestTypeCode = int(input("Введите номер requestTypeCode для отправки\n"))
                    logging.info(f"got requestTypeCode - {requestTypeCode}")
                except Exception as ex:
                    logging.error(ex)
            elif contur == 'exit':
                logging.debug("exit main function")
                logging.info("Всего хорошего!")
                break
            else:
                logging.debug("Error requests! Please try again!")
                contur = input("Выберите контур для создания документа: test, pred-prod или exit\n").lower()
                licenseTypeCode = int(input("Введите номер licenseTypeCode для отправки\n"))
                logging.info(f"got licenseTypeCode - {licenseTypeCode}")
                requestTypeCode = int(input("Введите номер requestTypeCode для отправки\n"))
                logging.info(f"got requestTypeCode - {requestTypeCode}")
    except Exception as ex:
        logging.error(ex)
    finally:
        logging.info("try again!")




if __name__ == "__main__":
    main()
