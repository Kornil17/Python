import logging

from confluent_kafka  import Consumer

# srv = 'gitlab-ci.ru:9092'
srv = '10.10.4.28:9092'
group = 'group-name'

c = Consumer({
    'bootstrap.servers': srv,
    'group.id': group,
    'enable.auto.commit': True,
    'auto.offset.reset': 'beginning'})

c.subscribe(['svs-inspector'])

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print("Received message: {}".format(msg.value().decode('utf-8')))

c.close()















# topics = ['svs-inspector']
# # srv = 'gitlab-ci.ru:9092'  # кафка песка доступна снаружи
# srv = '10.10.4.28:9092'  # kafka test
# group = 'group-name'
# # Sand
# # conf = {'bootstrap.servers': srv,
# #         'group.id': group,
# #         'enable.auto.commit': True,
# #         'auto.offset.reset': 'beginning'}  # 'earliest'}
#
# # Test
# conf = {'bootstrap.servers': srv,
#         'group.id': group,
#         'enable.auto.commit': True,
#         'auto.offset.reset': 'beginning'}
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
#                     encoding='utf-8', filemode='w')
# logging.debug("Debug log")
# logging.info("info log")
# logging.warning("warning log")
# logging.error("error log")
# logging.critical("critical log")

def kafkin_consume(conf, topics):
    # Подключение к кафке
    try:

        consumer = ck.Consumer(conf)
        consumer.subscribe(topics)
        logging.debug("kafka connect")
        while True:
            logging.info("start poll")
            msg = consumer.poll()
            logging.info("read message from kafka")
            if msg is None:
                logging.warning("not message")
                break
            else:
                val = msg.value().decode('utf8')
                print(msg.offset(), val)
                logging.info("find message in topic kafka and print their")

    except Exception as ex:
        logging.error(ex)
        print("Error connection")

if __name__ == "__main__":
    kafkin_consume(conf, topics)