from src.ResponseEpgu.kafkin import Kafka
from src.ResponseEpgu.parse_json import Parser
from src.ResponseEpgu import json
from src.ResponseEpgu import logger
import src.ResponseEpgu as ResponseEpgu

def main()->None:
    """main function"""
    parser = Parser()
    response_json = json.dumps(parser.get_response_json(), ensure_ascii=False).encode("utf8")
    logger.info(f'Get response json {response_json}')
    logger.debug('Start send message to Kafka')
    kafka = Kafka()
    kafka.produce(response_json)
    logger.debug('Message send to kafka')
    logger.debug('Goodbye! Have a nice day)')






if __name__ == "__main__":
    main()