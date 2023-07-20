import logging
import smtplib
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8')

logging.debug("test Debug")
logging.info("test info")
logging.warning("test warning")
logging.error("test error")
logging.critical("test critical")






class Send:
    def send_mail(self, message):

        self.message = message
        self.sender = "kornil172191@gmail.com"
        self.password = "KorniLoV200117DM!!_"
        logging.debug("Connect to SMTP")

        # server = smtplib.SMTP("smtp.mail.ru", 25)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        logging.debug("Server start")
        try :
            logging.debug("Server login")
            server.login(self.sender,self.password)
            logging.debug("Server sand message")
            server.sendmail(self.sender, self.sender, self.message)
            logging.info("The message was sent successfully")

        except Exception as ex:
            logging.error(ex)





def main():

    obj = Send()
    obj.send_mail(str(input("Введите сообщение для отправки\n")))




if __name__ == "__main__":
    main()