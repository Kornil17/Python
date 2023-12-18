from loguru import logger
# /tmp/python_venv_dm
from confluent_kafka import Consumer, Producer
import os
from json import load, dumps
from zipfile import ZipFile

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')
class Kafka:
    def __init__(self, contur, topic):
        self.choose_contur = {'sand':'gitlab-ci.ru:9092', 'test':'test-kafka1.fsrar.ru:9092', 'prod':'prod-kafka01-nd.fsrar.ru'}
        self.contur = self.choose_contur[contur]
        self.topic = topic
        self.connect = self.connection()
        self.consumer = self.connect
        self.producer = Producer({'bootstrap.servers':self.contur})

    def connection(self):
        logger.debug('start connection function')
        result_connection = Consumer({'bootstrap.servers':self.contur, 'group.id':'group', 'auto.offset.reset':'earliest','enable.auto.commit':False})
        logger.debug('exit from connection function')
        return result_connection
    def produce(self, topic, file_path):
        logger.debug("start produce function")
        self.producer.poll(0)
        with open(f'{file_path}', 'r') as f:
            js = load(f)
        self.producer.produce(topic, dumps(js, ensure_ascii=False).encode("utf8"))
        logger.info(f"Message: {dumps(js, ensure_ascii=False)} was recieved to kafka topic: {topic}")
        self.producer.flush()
    def read_message(self):
        logger.debug('start kafka read function')
        try:
            logger.debug('Start read messages from kafka')
            while True:
                logger.info(f'subscribe topic {self.topic}')
                self.consumer.subscribe([self.topic])
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                logger.info('print all messages from topic')
                print(f"Received message: {msg.value().decode('utf-8')}")
                # break
        except KeyboardInterrupt:
            logger.warning("Aborted by user...")
        except Exception as error:
            logger.error(f'Service error: {error}')
        finally:
            self.consumer.close()
            logger.info('Close the kafka connection')

def main():
    try:
        logger.debug('start main func')
        action = int(input('choose action: 1-write, 2-read, 3-exit. Just numbers!!\n'))
        if action != 3 and action < 3:
            if action == 1:
                count = int(input('Введите количество сообщений для отправки\n'))
                logger.info(f'Get count msg: {count}')
                kafkin = Kafka(input('Write contur (sand or test or prod)\n'), input('Write topic\n'))
                logger.info(f'Get contur named as: {kafkin.contur}')
                logger.info(f'Get topic named as: {kafkin.topic}')
                if count > 1:
                    archive_name = input('Write zip path\n')
                    with ZipFile(archive_name, mode='r') as zf:
                        data = zf.infolist()
                        try:
                            for d in data:
                                print(d.filename.split('/')[-1])
                                if not d.is_dir() and d.filename.split('.')[-1] == 'json':
                                    zf.extract(d.filename)
                                    kafkin.produce(kafkin.topic, d.filename)
                                    logger.info(f'send file - {d.filename}')
                        except Exception as error:
                            logger.error(f"Got error message - {error}")
                else:
                    logger.debug('start produce msg circle')
                    kafkin.produce(kafkin.topic, input('Write file path\n'))
                    logger.info(f'send msg')
            elif action == 2:
                kafkin = Kafka(input('Write topic\n'))
                logger.info(f'Get topic named as: {kafkin.topic}')
                kafkin.read_message()
        else:
            logger.debug('Goodbay! Have a nice day!)')

    except Exception as ex:
        logger.error(f'Exception: {ex}')
    finally:
        logger.debug('Goodbay! Have a nice day!)')

if __name__ == '__main__':
    main()