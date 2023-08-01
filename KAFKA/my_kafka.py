import logging

from confluent_kafka  import Consumer

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
#                     encoding='utf-8', filemode='w')
# logging.debug("Debug log")
# logging.info("info log")
# logging.warning("warning log")
# logging.error("error log")
# logging.critical("critical log")
#
# class Kafkin:
#     """Работа с  кафкой"""
#     group = 'group-name'
#     # def __init__(self, srv):
#     #     self.srv = srv
#     logging.debug("Start kafka class")
#     @classmethod
#     def connect(cls, srv, topic):
#         try:
#             logging.debug("connect function")
#             cls.srv = srv
#             cls.topic = topic
#             cls.c = Consumer({
#                 'bootstrap.servers': cls.srv,
#                 'group.id': cls.group,
#                 'enable.auto.commit': True,
#                 'auto.offset.reset': 'beginning'})
#             cls.c.subscribe([cls.topic])
#             while True:
#                 logging.debug("start circle")
#                 cls.msg = cls.c.poll(1.0)
#                 if cls.msg is None:
#                     logging.info("end circle")
#                     continue
#                 elif cls.msg.error():
#                     print(f"Consumer error: {cls.msg}")
#                     logging.info("read message")
#                     continue
#                 else:
#                     print(f"Received message: {cls.msg}")
#         except Exception as ex:
#             logging.debug(ex)
#         finally:
#             cls.c.close()
#
#
#
# class main:
#     """Подключение к кафке"""
#     print("Приветствую вас в программе для работы с кафкой\n")
#     srv = input("Выберите контур для подключения 1(test), 2(sand) или 3(exit)\n")
#     topic = input("Выберите топик ('svs-inspector', 'confirmed', 'crater') для подключения или 3(exit)\n")
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
#         except Exception as ex:
#             logging.debug(ex)
#
#
#
#
# if __name__ == "__main__":
#     main.get_data()






srv = 'gitlab-ci.ru:9092'
# srv = '10.10.4.28:9092'
group = 'group-name'

c = Consumer({
    'bootstrap.servers': srv,
    'group.id': group,
    'enable.auto.commit': True,
    'auto.offset.reset': 'beginning'})

c.subscribe(['svs-inspector'])
c.subscribe(['confirmed'])
c.subscribe(['crater'])
while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print("Received message: {}".format(msg.value().decode('utf-8')))

c.close()
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








