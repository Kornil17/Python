import psycopg2
from .config import *
from loguru import logger

logger.add('db.log', format='{time} {level} {message}', level='DEBUG')
class Connect:
    """class for connect db"""
    @staticmethod
    def connect(host: str, port: int, user: str, password: str, db: str)->str:
        try:
            connection = psycopg2.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=db)
            return connection.cursor()
        except Exception as error:
            logger.error(error)

class Conductor:
    """class for get data from db conductor"""
    @staticmethod
    def get_info_by_conductor(service, doc_number) -> dict:
        connection = Connect.connect(ConductorProd.HOST.value,
                                     ConductorProd.PORT.value,
                                     ConductorProd.USER.value,
                                     ConductorProd.PASSWORD.value,
                                     ConductorProd.NAME.value
                                     )
        if service == 'corrector_epgu':
            service = 'correction_epgu'
        logger.info(f'got service_id name {service}')
        connection.execute(f"SELECT free_num  FROM {service}\n"
                           f"where doc_number = '{doc_number}'")
        result = connection.fetchone()
        logger.info(f"got result from select to {service} database")
        return result
class Leveler:
    """class for get data from db leveler"""

    @staticmethod
    def get_info_by_leveler(number) -> dict:
        connection = Connect.connect(LevelerProd.HOST.value,
                                     LevelerProd.PORT.value,
                                     LevelerProd.USER.value,
                                     LevelerProd.PASSWORD.value,
                                     LevelerProd.NAME.value
                                     )
        connection.execute(
            f"select service_id, request_id, request_type, update_timestamp, attachment_path from request r where r.request_content like '%{number}%'")
        result = connection.fetchone()
        return result
