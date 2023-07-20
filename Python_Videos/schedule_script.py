import schedule, requests
from datetime import datetime
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')


# logging.debug("Debug log")
# logging.info("Info log")
# logging.warning("Warning log")
# logging.error("Error log")
# logging.critical("Critical log")

def greeting():
    try:
        sched = {
            '08:00': 'run Telegram Bot',
            '10:00': 'parse weather'
        }
        print("Daily tasks")
        logging.info("Create schedule")
        for i, j in sched.items():
            print(f"{i}-{j}")
            logging.debug(f"get key - {i} and value - {j} from  schedule")
        # response = requests.get(url=f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=11.07.2023')"
        print(requests.get("https://www.cbr.ru/scripts/XML_daily.asp").text)
        logging.debug("Get all valutes from Center Bank Russian Federation bank")
        response = float(ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text).find(
            './Valute[CharCode="USD"]/Value').text.replace(',', '.'))
        logging.debug("We get 'USD' value")
        print(datetime.now())
        logging.info(f"Time now is {datetime.now()}")

    except Exception as ex:
        logging.error(ex)


def main():
    greeting()
    schedule.every(1).minutes.do(greeting)
    logging.debug("Start schedule 1 minute")
    schedule.every().day.at('08:07').do(greeting)
    logging.debug("Start schedule every day at 08:07 ")

    while True:
        schedule.run_pending()


logging.info("All tasks success :)")

if __name__ == "__main__":
    main()
