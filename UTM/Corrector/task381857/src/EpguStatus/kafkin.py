from confluent_kafka import Producer
from .config import KafkaContur, KafkaTopic
from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')
class Kafka:
    def __init__(self):
        self.contur = KafkaContur.PROD.value
        self.topic = KafkaTopic.tests.value
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