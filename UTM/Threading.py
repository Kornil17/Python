import os
from datetime import datetime
from time import time, sleep
from threading import *
import functools
'Отправка документов по потокам в Барк по SOAP'

def count_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time() - start
        current_datetime = datetime.now()
        print(f"Время выполнения потока {func.__name__}: {end}, Дата  и время завершения выполнения потока {func.__name__}: {current_datetime}")
    return wrapper
@count_time
def first(path):
    for count in range(len(rp)):
        os.system(f"curl -F'xml_file=@{path+rp[count]}' http://localhost:8080/opt/in/RepProducedProduct_v4")
        # print(path+rp[count])
    print('\nexit')

@count_time
def second(path):
    for count in range(len(ttn)):
        os.system(f"curl -F'xml_file=@{path+ttn[count]}' http://localhost:8080/opt/in/WayBill_v4")
        # print(path + ttn[count])
    print('\nexit')
# 1 тип документа
rp_doc = '/mnt/Dmitriy_test/TASKS/TASK26Potoks_UTM/'
ttn_doc = '/mnt/Dmitriy_test/TASKS/TASK26Potoks_UTM/'
rp = ['RP.xml', 'RP1.xml', 'RP2.xml']
ttn = ['TTN.xml', 'TTN1.xml', 'TTN2.xml']
p1 = Thread(target=first, args=(rp_doc,))
p2 = Thread(target=second, args=(ttn_doc,))
p1.start()
p2.start()
p1.join()
p2.join()



