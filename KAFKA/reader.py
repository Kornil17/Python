import os
import uuid

from confluent_kafka import Consumer, KafkaException

from sys import path as local_lib

local_lib.append('../')
local_lib.append('../../')

# from Logger.baseLogger import BaseLogger


class KafkaConsumerWrapper:
    def __init__(self, topic,
                 bootstrap_servers,
                 group_id=None,
                 auto_offset_reset='earliest',
                 pool_timeout=1,
                 enable_auto_commit=True):
        """

        :param topic: Имя топика, на который подписываемся
        :type topic: str
        :param bootstrap_servers: Адрес кафки
        :type bootstrap_servers: str
        :param group_id: группа под которой считываем топик ( default='test-{uuid.uuid4()}' )
        :type group_id: str
        :param auto_offset_reset: откуда считываем топик [default('earliest'), 'latest']
        :type auto_offset_reset: str
        :param pool_timeout: периодичность обращения к кафке ( default = 1 sec )
        :type pool_timeout: int
        :param enable_auto_commit: коммитим ли сообщения при вычитывании? ( default = True )
        :type enable_auto_commit: bool
        """

        # базовые проверки при создании класса
        assert auto_offset_reset in ('earliest', 'latest')
        assert isinstance(group_id, str | None)
        assert isinstance(topic, str)
        assert isinstance(bootstrap_servers, str)
        assert isinstance(enable_auto_commit, bool)

        # self.log = BaseLogger(f'{topic}Consumer')
        self.consumer = self.__create_consumer__(bootstrap_servers, group_id, auto_offset_reset, enable_auto_commit)
        self.topic = topic
        self.pool_timeout = pool_timeout

    def __create_consumer__(self, bootstrap_servers, group_id, auto_offset_reset, enable_auto_commit):

        client_id = os.getlogin()
        if group_id is None:
            group_id = f'test-{uuid.uuid4()}'

        # self.log.info
        print(f'Creating consumer: \n'
                      f' - bootstrap.servers: {bootstrap_servers}\n'
                      f' - group.id: {group_id} \n'
                      f' - client.id: {client_id} \n'
                      f' - auto.offset.reset: {auto_offset_reset}\n'
                      f' - enable.auto.commit: {enable_auto_commit}')

        return Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'client.id': client_id,
            'auto.offset.reset': auto_offset_reset,
            'enable.auto.commit': enable_auto_commit
        })

    def consume(self):
        # self.log.info
        print(f'Subscribing to topic...')
        self.consumer.subscribe([self.topic])

        try:
            while True:
                msg = self.consumer.poll(self.pool_timeout / 1)
                if msg is None:  # если ничего не получаем
                    # self.log.info
                    print('No message received')
                    yield None
                    continue
                if msg.error():  # вывести и вернуть ошибку, если что-то пошло не так
                    # self.log.error
                    print(msg.error())
                    raise KafkaException(msg.error())

                # self.log.info
                print(f'Получено сообщение из: \n'
                              f' - {msg.topic() = }\n'
                              f' - {msg.partition() = }')
                # self.log.info
                print(f"Cообщение: {msg.value().decode('utf-8')}")
                yield msg.value().decode('utf-8')
        except KeyboardInterrupt:
            pass  # если закрыть руками
        finally:
            self.close()  # при любой не понятной ситуации - закрыть

    def close(self):
        """ Закрытие консумера """
        # self.log.info
        print('Closing consumer...')
        self.consumer.close()
        # self.log.info
        print('Success!')


def get_sum():
    """  Просто тестовая функция """
    return 1 + 1


def test_consumer():
    consumer = KafkaConsumerWrapper('inbox', 'gitlab-ci.ru:9092', group_id='test-50f74e50-52f9-4476-8c88-35b31eaaa245')

    try:
        for message in consumer.consume():
            if message is not None:
                print(get_sum())
            continue
    except KafkaException as e:
        print(f'KafkaException: {e}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == '__main__':
    test_consumer()
