from enum import Enum


class ConductorProd(Enum):
    HOST = 'prod-patroni.fsrar.ru'
    PORT = 5000
    USER = 'corrector-epgu-rw'
    PASSWORD = 'y2tM$u9p&T'
    NAME = 'conductor'

class LevelerProd(Enum):
    HOST = 'postgres-r1.fsrar.ru'
    PORT = 5432
    USER = 'leveler'
    PASSWORD = 'QAZwsx123'
    NAME = 'leveler'


class ConductorTest(Enum):
    HOST = 'test-pstgr.nd.fsrar.ru'
    PORT = 5432
    USER = 'ci'
    PASSWORD = 'ci'
    NAME = 'conductor'

class LevelerTest(Enum):
    HOST = 'test-pstgr.nd.fsrar.ru'
    PORT = 5432
    USER = 'leveler'
    PASSWORD = 'QAZwsx123'
    NAME = 'leveler'

class ConductorSand(Enum):
    HOST = '89.108.103.170'
    PORT = 5432
    USER = 'fsrar_user'
    PASSWORD = 'Qwerty1234'
    NAME = 'conductor'

class LevelerSand(Enum):
    HOST = 'gitlab-ci.ru'
    PORT = 5432
    USER = 'leveler'
    PASSWORD = 'QAZwsx123'
    NAME = 'leveler'

class KafkaContur(Enum):
    TEST = 'test-kafka1.fsrar.ru:9092'
    SAND = 'gitlab-ci.ru:9092'
    PROD = 'prod-kafka01-nd.fsrar.ru:9092'

class KafkaTopic(Enum):
    TEST = 'test-smev-leveler-in-response'
    SAND = 'test-smev-leveler-in-response'
    PROD = 'smev-leveler-in-response'
    tests = 'test'