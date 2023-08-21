import requests
from datetime import datetime
import logging
import certifi
import ssl
context=ssl.create_default_context(cafile=certifi.where())

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
# /mnt/Dmitriy_test/Documents/reject.pdf
# /home/ldapusers/d_kornilov/scripts/reject.pdf
class License:

    """class construction"""
    def __init__(self, address, token, licenseTypeCode, requestTypeCode, inn='7841051711', file=open('/home/ldapusers/d_kornilov/scripts/reject.pdf', 'rb'), time=datetime.now().strftime("%Y-%m-%d"), orgBriefName="ООО Тестировщик", orgFullName="ООО Тестим", response=""):
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
                'requestTypeCode': self.requestTypeCode,
            }
        logging.info(f"got parametrs")
    def send(self):
        try:
            logging.debug('start send function')
            self.resp = requests.post(f'http://{self.address}/api-lc-license/dashboard/license/request/', headers=self.headers, files=self.files)
            logging.debug('send post request')
            logging.debug(f'get status code - {self.resp.text}')
        except Exception as ex:
            logging.error('Error!')
            raise logging.error(ex)



# class Test(License):
#
#     """class send to Test contur"""
#
#     def __init__(self, licenseTypeCode, requestTypeCode):
#         super().__init__(token, licenseTypeCode, requestTypeCode)
#     def send(self):
#         self.response = requests.post('http://lk-test.test-kuber-nd.fsrar.ru/api-lc-license/dashboard/license/request/', headers=self.headers, files=self.files)
#
#
#
#
# class Pred(License):
#
#     """class send to Pred-Prod contur"""
#
#     def __init__(self, licenseTypeCode, requestTypeCode):
#         super().__init__(token, licenseTypeCode, requestTypeCode)
#
#     def send(self):
#         self.response = requests.post('http://lk-egais.pred-kuber-nd.fsrar.ru/api-lc-license/dashboard/license/request/',
#                                       headers=self.headers, files=self.files)




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
                    # print(send_files.__dict__)
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
                    # print(send_files.__dict__)
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
