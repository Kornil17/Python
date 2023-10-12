import logging
import kafka
from confluent_kafka  import Consumer
class Kafka:
    def __init__(self):
        self.connect = self.connection()
        self.contur = 'gitlab-ci.ru:9092'
        self.topic = ['svs-inspector']
        self.consumer = self.connect.subscribe(self.topic)

    def connection(self):
        result_connection = kafka.KafkaConsumer(bootstrap_servers=self.contur,
                            group_id='group_id',
                            consumer_timeout_ms=60000,
                            auto_offset_reset='earliest',
                            enable_auto_commit=False)
        return result_connection
