from confluent_kafka import Producer
from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')
class Kafka:
    def __init__(self):
        self.contur = 'gitlab-ci.ru:9092'
        # self.contur = 'test-kafka1.fsrar.ru:9092'
        self.topic = 'test-smev-leveler-in-response'
        self.producer = Producer({'bootstrap.servers':self.contur})
    def produce(self, messages)->None:
        try:
            logger.debug("start produce function")
            self.producer.poll(0)
            self.producer.produce(self.topic, messages)
            logger.info(f"Message: {messages} was recieved to kafka topic: {self.topic}")
            logger.debug('Flushing...')
            self.producer.flush()
        except Exception as ex:
            logger.error(ex)