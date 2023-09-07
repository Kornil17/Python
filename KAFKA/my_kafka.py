import logging
import kafka
from confluent_kafka  import Consumer
import json.decoder


logging.basicConfig(level=logging.INFO, filename='kafka_log.logs', format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
logging.debug("Debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.critical("critical log")

class MainKafka:
    """Главный класс-конструктор Кафки"""
    logging.debug('Start class MainKafka')
    def __init__(self, parametrs):
        logging.debug('initializate parametrs')
        self.__dict__.update(parametrs)
        self.consumer = None
        logging.info(f"got parametrs: {self.__dict__}")
    def kafka_connect(self):
        logging.debug('start initializate consumer')
        self.consumer = kafka.KafkaConsumer(bootstrap_servers=self.__dict__['bootstrap_servers'],
                                       group_id=self.__dict__['group_id'],
                                       consumer_timeout_ms=int(self.__dict__['consumer_timeout_ms']),
                                       auto_offset_reset=self.__dict__['auto_offset_reset'],
                                       enable_auto_commit=self.__dict__['enable_auto_commit'])
        logging.info(f"got consumer paramets: {self.__dict__['bootstrap_servers'], }")
        logging.debug(f"start subscribe topic: {self.__dict__['topic'], self.__dict__['group_id'],self.__dict__['consumer_timeout_ms'],self.__dict__['auto_offset_reset'],self.__dict__['enable_auto_commit']}")
        self.consumer.subscribe([self.__dict__['topic']])
        logging.debug('select action')
        if self.__dict__['action'] == 'read':
            logging.info("got read action")
            self.kafka_read()
        else:
            logging.info("got write action")
            self.kafka_write()


    def kafka_read(self) -> None:
        logging.debug('start read function')
        try:
            logging.debug(f"try read topic")
            for message in self.consumer:
                logging.info('print message from topic')
                print(message.value.decode('utf-8'))
                logging.info('next message')

        except KeyboardInterrupt:
            logging.warning("Aborted by user...")
        except Exception as ex:
            logging.error(ex)

        finally:
            logging.info("close kafka connection")
            self.consumer.close()
    def kafka_write(self):
        pass

def main():
    logging.debug('Start main function')
    print('Приветствую вас в программе по работе с кафкой')
    logging.debug('get contur')
    get_contur = input('Выберите контур для работы с кафкой: sand, test или же exit\n').lower()
    logging.info(f'got contur: {get_contur}')
    logging.debug('get topic')
    get_topic = input('Выберите топик для работы с кафкой или же exit\n').lower()
    logging.info(f'got topic: {get_topic}')
    logging.debug('get action')
    get_action = input('Выберите действие с кафкой: read-чтение, write-запись\n').lower()
    logging.info(f'got action: {get_action}')
    if get_contur != 'exit' and get_topic != 'exit':
        logging.debug('start while circle')
        while get_contur != 'exit' or get_topic != 'exit':
            try:
                logging.debug('activate parametrs')
                parametrs_active = int(input("Вы хотите изменить параметры настроек кафки?: 1-да или 0-нет\n"))
                if parametrs_active == 1:
                    logging.debug('change parametrs')
                    parametrs = {
                        'bootstrap_servers': input('Выберите контур для работы с кафкой: sand, test\n').lower(),
                        'group_id': input('Напишите пользователя\n').lower(),
                        'consumer_timeout_ms': int(input('Установите время ожидания\n')),
                        'auto_offset_reset': input('Напишите уровень считывания сообщений\n').lower(),
                        'enable_auto_commit': input('Активируйте запоминание смещения пользователем: True-включено или False-выключено\n').title(),
                        'topic': input('Выберите топик для работы с кафкой\n').lower(),
                        'action': input('Выберите действие с кафкой: read-чтение, write-запись\n').lower()
                    }

                    logging.info(f"got parametrs: {parametrs}")
                    logging.debug('connect to class MainKafka')
                    kaf = MainKafka(parametrs)
                    kaf.kafka_connect()
                    logging.debug('get contur')
                    get_contur = input('Выберите контур для работы с кафкой: sand, test или же exit\n').lower()
                    logging.info(f'got contur: {get_contur}')
                    logging.debug('get topic')
                    get_topic = input('Выберите топик для работы с кафкой или же exit\n').lower()
                    logging.info(f'got topic: {get_topic}')
                    logging.debug('get action')
                    get_action = input('Выберите действие с кафкой: read-чтение, write-запись\n').lower()
                    logging.info(f'got action: {get_action}')
                elif parametrs_active == 0:
                    if get_contur == 'sand':
                        contur = 'gitlab-ci.ru:9092'
                    else:
                        contur = '10.10.4.28:9092'
                    parametrs = {
                        'bootstrap_servers': contur,
                        'group_id': 'group_id',
                        'consumer_timeout_ms': 60000,
                        'auto_offset_reset': 'earliest',
                        'enable_auto_commit': False,
                        'topic': get_topic,
                        'action': 'read'
                    }
                    logging.info(f"got parametrs: {parametrs}")
                    logging.debug('connect to class MainKafka')
                    kaf = MainKafka(parametrs)
                    kaf.kafka_connect()
                    logging.debug('get contur')
                    get_contur = input('Выберите контур для работы с кафкой: sand, test или же exit\n').lower()
                    logging.info(f'got contur: {get_contur}')
                    logging.debug('get topic')
                    get_topic = input('Выберите топик для работы с кафкой или же exit\n').lower()
                    logging.info(f'got topic: {get_topic}')
                    logging.debug('get action')
                    get_action = input('Выберите действие с кафкой: read-чтение, write-запись\n').lower()
                    logging.info(f'got action: {get_action}')

            except Exception as ex:
                logging.error(ex)
            finally:
                logging.debug('Всего хорошегоооо!!))')
    else:
        logging.debug('Всего хорошегоооо!!))')


if __name__ =='__main__':
    main()

































# class Kafkin:
#     """Работа с  кафкой"""
#     group = 'group'
#     # def __init__(self, srv):
#     #     self.srv = srv
#     logging.debug("Start kafka class")
#     @classmethod
#     def connect(cls, srv, topic, consumer=None):
#             logging.debug("connect function")
#             cls.srv = srv
#             cls.topic = topic
#             cls.consumer = kafka.KafkaConsumer(bootstrap_servers=cls.srv,
#                                                group_id=cls.group,
#                                                consumer_timeout_ms=60000,
#                                                auto_offset_reset='earliest',
#                                                enable_auto_commit=False)
#             # cls.c = kafka.KafkaConsumer({
#             #     'bootstrap.servers': cls.srv,
#             #     'group.id': cls.group,
#             #     'enable.auto.commit': False,
#             #     'auto.offset.reset': 'earliest'})
#             cls.consumer.subscribe([cls.topic])
#             logging.debug("start circle")
#             try:
#                 for i in cls.consumer:
#                     print(i.value.decode('utf-8'))
#             except Exception as ex:
#                 logging.debug(ex)
#             finally:
#                 cls.consumer.close()
#
#
#
# class main:
#     """Подключение к кафке"""
#     print("Приветствую вас в программе для работы с кафкой\n")
#     srv = input("Выберите контур для подключения 1(test), 2(sand) или 3(exit)\n")
#     topic = input("Выберите топик ('svs-inspector', 'confirmed', 'crater') для подключения или 3(exit)\n")
#     # if keyboard.press('ctrl + c'):
#     #     keyboard.send('exit')
#     @classmethod
#     def get_data(cls):
#         try:
#             while cls.srv != "3" or cls.topic != "3":
#                 if cls.srv == "1":
#                     logging.debug("connect test_kafka")
#                     Kafkin.connect('10.10.4.28:9092', cls.topic)
#                     cls.srv = input("Выберите контур для подключения 1(test), 2(sand) или 3(exit)\n")
#                     topic = input("Выберите топик ('svs-inspector', 'confirmed', 'crater') для подключения или 3(exit)\n")
#
#                 elif cls.srv == "2":
#                     logging.debug("connect sand_kafka")
#                     Kafkin.connect('gitlab-ci.ru:9092', cls.topic)
#                     cls.srv = input("Выберите контур для подключения 1(test), 2(sand) или 3(exit)\n")
#                     topic = input("Выберите топик ('svs-inspector', 'confirmed', 'crater') для подключения или 3(exit)\n")
#
#                 elif cls.srv == "3":
#                     break
#                 # elif keyboard.press('ctrl + c'):
#                 #     break
#         except Exception as ex:
#             logging.debug(ex)

# if __name__ == "__main__":
#     main.get_data()






# srv = 'gitlab-ci.ru:9092'
# # srv = '10.10.4.28:9092'
# group = 'group-name'
#
# c = Consumer({
#     'bootstrap.servers': srv,
#     'group.id': group,
#     'enable.auto.commit': True,
#     'auto.offset.reset': 'beginning'})
#
# c.subscribe(['svs-inspector'])
# c.subscribe(['confirmed'])
# c.subscribe(['crater'])
# while True:
#     msg = c.poll(1.0)
#     if msg is None:
#         continue
#     if msg.error():
#         print("Consumer error: {}".format(msg.error()))
#         continue
#     print("Received message: {}".format(msg.value().decode('utf-8')))
#
# c.close()
#
#

#
# from confluent_kafka import Producer
#
# p = Producer({'bootstrap.servers': 'mybroker1,mybroker2'})
#
# def delivery_report(err, msg):
#     """ Called once for each message produced to indicate delivery result.
#         Triggered by poll() or flush(). """
#     if err is not None:
#         print('Message delivery failed: {}'.format(err))
#     else:
#         print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
#
# for data in some_data_source:
#     # Trigger any available delivery report callbacks from previous produce() calls
#     p.poll(0)
#
#     # Asynchronously produce a message. The delivery report callback will
#     # be triggered from the call to poll() above, or flush() below, when the
#     # message has been successfully delivered or failed permanently.
#     p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)
#
# # Wait for any outstanding messages to be delivered and delivery report
# # callbacks to be triggered.
# p.flush()








