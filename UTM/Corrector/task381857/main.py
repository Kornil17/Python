import json
from src.EpguStatus.database import Connect
from src.EpguStatus.config import *
from src.EpguStatus.kafkin import Kafka
from src.EpguStatus.database import Conductor, Leveler
import json
from loguru import logger

logger.add('main.log', format='{time} {level} {message}', level='DEBUG')


def main():
    logger.debug('start function main')
    doc_number = int(input('Введите номер документа\n'))
    status = input('Введите статус заявления\n')
    logger.info(f"get doc_number {doc_number}")
    logger.info('call leveler function')
    leveler_data = Leveler.get_info_by_leveler(doc_number)
    logger.info(f'got value = {leveler_data} from func leveler')
    result_leveler_data = {'serviceId':leveler_data[0], 'requestId':leveler_data[1], 'requestType':leveler_data[2], 'updateTimestamp':leveler_data[3].isoformat()+'+0300', "responseContent":{"serviceStatus":"2001","caseNumber":"Е-173","attachments":[]}}
    logger.info('check status equal (2002, 2003)')
    if status in ["2002", "2003"]:
        result_leveler_data["responseContent"]["serviceStatus"] = status
        result_leveler_data["responseContent"]["attachments"] = [{"path": leveler_data[4].replace('Application.zip', f'response/{doc_number}.zip')}]
        # result_leveler_data["responseContent"]["attachments"] = [{"path": leveler_data[4].replace('Application.zip', f'response/Визуализация_ИСХ_ЦА.pdf')}]
        # result_leveler_data["responseContent"]["attachments"].append({"path": leveler_data[4].replace('Application.zip', f'response/Pril.zip')})
    logger.info(f"formed result json {result_leveler_data}")
    logger.info('call conductor function')
    conductor_data = Conductor.get_info_by_conductor(result_leveler_data['serviceId'].replace('-', '_'), doc_number)
    logger.info(f'got value = {conductor_data} from func leveler')
    result_leveler_data["responseContent"]['caseNumber'] = str(*conductor_data)
    logger.info(f'added value = {conductor_data} to result json')
    logger.info('call kafka function')
    kafka = Kafka()
    kafka.produce(json.dumps(result_leveler_data, ensure_ascii=False))
    logger.debug('End main function')



if __name__ == '__main__':
    main()
