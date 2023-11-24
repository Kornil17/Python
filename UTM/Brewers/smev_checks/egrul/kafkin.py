from confluent_kafka import Producer
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',encoding='utf-8')
class Kafka:
    def __init__(self):
        self.contur = 'gitlab-ci.ru:9092'
        # self.contur = 'test-kafka1.fsrar.ru:9092'
        self.topic = 'test-smev-leveler-out-response-fromprod'
        self.producer = Producer({'bootstrap.servers':self.contur})
    def produce(self, messages):
        logging.debug("start produce function")
        self.producer.poll(0)
        self.producer.produce(self.topic, messages)
        logging.info(f"Message: {messages} was recieved to kafka topic: {self.topic}")
        print(f"Message: '{messages}' was recieved to kafka topic: '{self.topic}'")
        self.producer.flush()
        return True