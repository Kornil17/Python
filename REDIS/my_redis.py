import logging
import redis
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
# redis_host = '10.10.5.103'
# redis_port = 6379
# redis_db = 0
# redis_pass = 'YV82Szr4GBI7bdrnytLpXJN2'

# redis_host = '194.67.93.217'
# redis_port = 6379
# redis_db = 0
# redis_pass = 'YV82Szr4GBI7bdrnytLpXJN2'

class Rediss:

    # Класс для подключения к базам редиса на разных контурах
    def __init__(self, redis_host, redis_port, redis_db, redis_pass):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_pass = redis_pass



    def redis_connect(self):
        # connect to Sand Redis
        try:
            logging.info("Connection to Redis")
            redis_client = redis.Redis(host=self.redis_host, port= self.redis_port, db=self.redis_db, password=self.redis_pass, decode_responses=True)
            sand_commands = str(input("Введите команду (get, set, delete) для работы с базой или exit для выхода\n")).lower()
            logging.debug("Get command")
            while sand_commands != 'exit':
                logging.debug("Start the circle")
                if sand_commands == 'get':
                    logging.debug("Send the get request")
                    print(redis_client.get(str(input("Введите ключ для запроса в БД\n").lower())))
                    logging.debug("Request success")
                    sand_commands = str(input("Введите команду (get, set, delete) для работы с базой или exit для выхода\n")).lower()
                    logging.debug("Repeat sand the command")

                elif sand_commands == 'set':
                    logging.debug("Send the set request")
                    name = str(input("Введите ключ для запроса в БД\n"))
                    value = int(input("Введите значение для ключа\n"))
                    print(redis_client.set(name=name, value=value))
                    logging.debug("Request success")
                    sand_commands = str(input("Введите команду (get, set, delete) для работы с базой или exit для выхода\n")).lower()
                    logging.debug("Repeat sand the command")

                elif sand_commands == 'delete':
                    logging.debug("Send the delete request")
                    print(redis_client.delete(str(input("Введите ключ для удаление из БД\n"))))
                    logging.debug("Request success")
                    sand_commands = str(input("Введите команду (get, set, delete) для работы с базой или exit для выхода\n")).lower()
                    logging.debug("Repeat sand the command")

                elif sand_commands == 'exit':
                    redis_client.close()
                    logging.info("Connection close")
                    logging.debug("All tasks success")
                    break

                else:
                    logging.error("Bad request")
                    print("Введены некорректные данные\nПопробуйте еще раз!")
                    sand_commands = str(input("Введите команду (get, set, delete) для работы с базой или exit для выхода\n")).lower
                    logging.debug("Repeat sand the command")

        except Exception as ex:
            logging.error("Error")
            print('#' * 20)



def main():
    logging.debug('Start processing')
    command = str(input("Выберите контур для подключения к базе Redis:\nSand ('194.67.93.217')\nTest ('10.10.5.103')\nExit\n")).lower()
    logging.debug('Get commnad')
    while command != 'exit':
        logging.debug("Start circle")
        # if isinstance(command, str):
        #     logging.error("Incorrect command")
        #     raise TypeError("Неккоректное значение, попробуйте еще раз!")
        if command == 'sand':
            logging.debug("Connect to Redis Sand")
            request = Rediss('194.67.93.217', 6379, 0, 'YV82Szr4GBI7bdrnytLpXJN2')
            request.redis_connect()
            command = str(input("Выберите контур для подключения к базе Redis:\nSand ('194.67.93.217')\nTest ('10.10.5.103')\nExit\n")).lower()
        elif command == 'test':
            logging.debug("Connect to Redis Test")
            request = Rediss('10.10.5.103', 6379, 0, 'YV82Szr4GBI7bdrnytLpXJN2')
            request.redis_connect()
            command = str(input("Выберите контур для подключения к базе Redis:\nSand ('194.67.93.217')\nTest ('10.10.5.103')\nExit\n")).lower()
        elif command == 'exit':
            logging.debug('Close connection and exit from Redis')
            print("Спасибо за работу, хорошего дня!)")
            break

        else:
            logging.error("Bad request")
            print("Введены некорректные данные\nПопробуйте еще раз!")
            command = str(input("Выберите контур для подключения к базе Redis:\nSand ('194.67.93.217')\nTest ('10.10.5.103')\nExit\n")).lower()




if __name__ == "__main__":
    main()
