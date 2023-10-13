import logging
# from kafka import KafkaConsumer
# /tmp/python_venv_dm
from confluent_kafka import Consumer
class Kafka:
    def __init__(self, topic):
        self.contur = 'gitlab-ci.ru:9092'
        # self.contur = '10.10.4.28:9092'
        self.topic = topic
        self.connect = self.connection()
        self.consumer = self.connect

    def connection(self):
        logging.debug('start connection function')
        result_connection = Consumer({'bootstrap.servers':self.contur, 'group.id':'group', 'auto.offset.reset':'earliest','enable.auto.commit':False})
        logging.debug('exit from connection function')
        return result_connection

    def write_message(self):
        pass

    def read_message(self):
        logging.debug('start kafka read function')
        try:
            logging.debug('Start read messages from kafka')
            while True:
                logging.info(f'subscribe topic {self.topic}')
                self.consumer.subscribe([self.topic])
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                logging.info('print all messages from topic')
                print(f"Received message: {msg.value().decode('utf-8')}")
                # break
        except KeyboardInterrupt:
            logging.warning("Aborted by user...")
        except Exception as error:
            logging.error(f'Service error: {error}')
        finally:
            self.consumer.close()
            logging.info('Close the kafka connection')
kafkin = Kafka(input('Write topic\n'))
logging.info(f'Get topic named as: {kafkin.topic}')
kafkin.read_message()
