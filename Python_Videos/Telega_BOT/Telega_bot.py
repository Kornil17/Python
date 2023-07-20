import requests
from datetime import datetime
import telebot
import logging

logging.basicConfig(level=logging.DEBUG,filename='my_logging_telegabot.log',format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8', filemode='w')
# logging.debug("Debug log")
# logging.info("Info log")
# logging.warning("Warning log")
# logging.error("Error log")
# logging.critical("Critical log")

token = "6378917995:AAF3Ur9M4KsgwUX5Wg3HH4YOyqvhbZQPbuw"
bot = telebot.TeleBot(token)


responses = ["AUD","AZN","GBP","AMD","BYN","BGN","BRL","HUF","HKD","DKK","USD","EUR","INR","KZT","CAD","KGS","CNY","MDL","NOK","PLN","RON","XDR","SGD","TJS","TRY","UZS","UAH","CZK","SEK","CHF","ZAR","KRW","JPY"]

def get_data(message):
    # req = requests.get("https://www.cbr-xml-daily.ru/latest.js")
    try:
        req = requests.get("https://www.cbr-xml-daily.ru/archive/2020/06/02/daily_json.js")
        response = req.json()
        print(response)
        result = message.text.upper()
        val = response["Valute"][result]["Value"]
    # print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nUSD price by RUB now: {message}")
        logging.debug("All tasks success")
        return val, result
    except Exception as ex:
        logging.error(ex)



@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}!")
    logging.debug("Sand message Hello in chat")
    bot.send_message(message.chat.id, "I hope you provide the best time in your life)")
    logging.info("Sand good message in chat")
    bot.send_message(message.chat.id, "You should write name of value from the list:")
    logging.debug("Sand message list in chat")
    req = requests.get("https://www.cbr-xml-daily.ru/archive/2020/06/02/daily_json.js")
    response = req.json()
    logging.info("Api reques is correct")
    for i in responses:
        bot.send_message(message.chat.id,f"{i} - {str(response['Valute'][i]['Name'])}")
        logging.debug(f"Sand message {i} list in chat")
    bot.send_message(message.chat.id, "Write the name of value you want to see (just three letters) Example: 'USD'")
    logging.debug(f"Good work for func start")

# @bot.message_handler(content_types=['text'])
# def send_message(message):
#     if message.text.lower() == "1":
#         bot.send_message(message.chat.id, f"Hello")
#     else:
#         bot.send_message(message.chat.id, "Something wrong...")

@bot.message_handler(content_types=['text'])
def send_message(message):
    try:
        if message.text.upper() in ["AUD","AZN","GBP","AMD","BYN","BGN","BRL","HUF","HKD","DKK","USD","EUR","INR","KZT","CAD","KGS","CNY","MDL","NOK","PLN","RON","XDR","SGD","TJS","TRY","UZS","UAH","CZK","SEK","CHF","ZAR","KRW","JPY"]:
            n, m = get_data(message)
            bot.send_message(
            message.chat.id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n{m} price by RUB now: {n}")
            logging.debug(f"Work messsage is correct ")
        else:
            bot.send_message(message.chat.id, "Hmm.. Something wrong, try again please\nMay be you write incorrect value")
            logging.warning(f"Incorrect message {message.text}")

    except Exception as ex:
        bot.send_message(message.chat.id, "Hmm.. Something wrong..")
        logging.error("Programm can't handle with task")


logging.info("All tasks success")
logging.debug("End processing")
bot.polling()

if __name__ == "__main__":
    start_message()
