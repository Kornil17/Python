import os
from datetime import datetime, timezone
from time import sleep
import gen_bar
import gen_bar2
import random
import subprocess

class UTM:

    """class constructor"""

    def __init__(self, result=None):
        if result is None:
            self.result: list = list()
        else:
            self.result: list = result


    def gen_bar(self):
        self.bar = gen_bar.Bark()
        self.bars = str(self.bar.get_new(1))[2:]
        return self.bars[:-2]




    def randoms(self, x):
        if x == 1:
            return random.randint(1000, 9999)
        elif x == 2:
            return random.randint(1, 9999)
    def datas(self):
        return str(datetime.now())[:10]

    def sub_proc(self, bshCmd):
        self.process = subprocess.Popen(bshCmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        self.process.stdin.write("curl -F file=@- http://10.10.4.247:8002/wb < WBGZ.xml")
        self.process.stdin.close()





class WBGZ(UTM):
    """class send WBGZ"""

    def __init__(self, gz):
        super().__init__()
        self.gz = gz

    def construct_file(self):
        with open('/mnt/Dmitriy_test/Marks/Marks.xml', 'r') as f:
            self.n = f.readlines()
            for i in range(len(self.n)):
                if i == 0:
                    self.data = ["<?xml version='1.0' encoding='utf-8'?>",
                         '<ns:Documents xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"',
                         'xmlns:gz="http://fsrar.ru/WEGAIS/goznak">', "<ns:Header>",
                         "<gz:DocType>WayBillGoznak</gz:DocType>"]
                    for data in range(len(self.data)):
                        self.result.append(self.data[data])
                elif i == 5:
                    self.line6 = self.n[i].rstrip()
                    self.line6 = self.line6.replace("LOC-GZ-0000004111", f"LOC-GZ-000000{self.randoms(1)}")
                    self.result.append(self.line6)
                elif i == 6:
                    self.line7 = self.n[i].rstrip()
                    self.line7 = self.line7.replace("2023-05-25", f"{self.datas()}")
                    self.result.append(self.line7)
                elif i == 7:
                    self.line8 = self.n[i].rstrip()
                    self.line8 = self.line8.replace("1", f"{self.randoms(1)}")
                    self.result.append(self.line8)
                    self.data1 = [
                        '<gz:shipperID>030000253368</gz:shipperID>',
                        '<gz:ConsigneeID>030000353121</gz:ConsigneeID>',
                        '<gz:typeclaim>1</gz:typeclaim>',
                        '<gz:Content xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01" xmlns:gz="http://fsrar.ru/WEGAIS/goznak">',
                        '<gz:Pos>',
                        '<gz:DocPosId>1</gz:DocPosId>'
                    ]
                    for data1 in range(len(self.data1)):
                        self.result.append(self.data1[data1])
                elif i == 15:
                    self.line16 = self.n[i].rstrip()
                    self.line16 = self.line16.replace("TEST-FB-0000004555", f"TEST-FB-000000{self.randoms(1)}")
                    self.result.append(self.line16)
                    self.data2 = [
                        '<gz:bc xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"',
                        'xmlns:gz="http://fsrar.ru/WEGAIS/goznak">',
                    ]
                    for data2 in range(len(self.data2)):
                        self.result.append(self.data2[data2])
                elif i == 17:
                    for gz in range(self.gz):
                        gz = f"<gz:NCode>{self.gen_bar()}</gz:NCode>"
                        print(gz)
                        self.result.append(gz)
                    self.data3 = [
                        '</gz:bc>',
                        '</gz:Pos>',
                        '</gz:Content>',
                        '</ns:Header>',
                        '</ns:Documents>',
                    ]
                    for data3 in range(len(self.data3)):
                        self.result.append(self.data3[data3])
        os.system("touch WBGZ.xml")
        with open('WBGZ.xml', 'w') as op:
            for i in range(len(self.result)):
                op.write(str(self.result[i]) + '\n')
        os.system("scp /home/kornilov/PycharmProjects/pythonProject/UTM/WBGZ.xml d_kornilov@test-node03-nd:./")
        self.bshCmd = 'ssh -T Bark_test'
        self.send = self.sub_proc(self.bshCmd)



class RP(UTM):
    def __init__(self, results=None, gz=None):
        if gz is None and results is None:
            self.gz: list = list()
            self.results_rp: list = list()
        else:
            self.gz: list = gz
            self.results_rp: list = results
    def construct_file(self):
        print("Start function")
        with open('/home/kornilov/PycharmProjects/pythonProject/UTM/WBGZ.xml', 'r') as wb:
            self.wbgz = wb.readlines()
            for i in range(len(self.wbgz)):
                if i >= 17 and  "<gz:NCode>" in self.wbgz[i]:
                    self.wbgz[i] = self.wbgz[i].replace("<gz:NCode>", "<ce:amc>")
                    self.wbgz[i] = self.wbgz[i].replace("</gz:NCode>", "</ce:amc>")
                    self.gz.append(self.wbgz[i])

        with open('/mnt/Dmitriy_test/Produce_requests/RP.xml', 'r') as f:
            self.rp = f.readlines()
            for i in range(len(self.rp)):
                if i == 10:
                    self.line11 = self.rp[i].rstrip()
                    self.line11 = self.line11.replace("030000353121", f"030000353121")
                    self.results_rp.append(self.line11)
                elif i == 14:
                    self.line15 = self.rp[i].rstrip()
                    self.line15 = self.line15.replace("1", f"{self.randoms(2)}")
                    self.results_rp.append(self.line15)
                elif i == 17:
                    self.line18 = self.rp[i].rstrip()
                    self.line18  = self.line18 .replace("1", f"{self.randoms(2)}")
                    self.results_rp.append(self.line18)
                elif i == 18 or i == 19:
                    self.lines = self.rp[i].rstrip()
                    self.lines = self.lines.replace("2023-07-12", f"{self.datas()}")
                    self.results_rp.append(self.lines)
                elif i == 39:
                    self.line40 = self.rp[i].rstrip()
                    self.line40 = self.line40.replace("2", f"{str(len(self.wbgz))}")
                    self.results_rp.append(self.line40)
                elif i == 48:
                    for wbgz in range(len(self.wbgz)):
                        self.gz = f"{self.wbgz[wbgz]}"
                        self.results_rp.append(self.gz)
                    self.data = [
                        "</rpp:MarkInfo>",
                        "</rpp:Position>",
                        "</rpp:Content>",
                        "</ns:RepProducedProduct_v4>",
                         "</ns:Document>",
                        "</ns:Documents>"]
                    for data in range(len(self.data)):
                        self.results_rp.append(self.data[data])
                elif i < 47:
                    self.results_rp.append(self.rp[i].rstrip())

        os.system("touch RP.xml")
        with open('RP.xml', 'w') as rp:
            for data in range(len(self.results_rp)):
                rp.write(str(self.results_rp[data]) + '\n')
        # os.system(
        #     "curl -F'xml_file=@/home/kornilov/PycharmProjects/pythonProject/RP.xml' http://localhost:8080/opt/in/RepProducedProduct_v4")











def main():
    print("Welcome to send_files programm")
    command = input(f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'").upper()
    while command != "EXIT":
        if command == "WBGZ":
            gz_count = int(input("Введите количество марок ...:,'\n'"))
            send_files = WBGZ(gz_count)
            print(send_files.__dict__)
            send_files.construct_file()
            command = input(f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'").upper()
        elif command == "RP":
            send_files = RP()
            print(send_files.__dict__)
            send_files.construct_file()
            command = input(
                f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'").upper()
        # elif command  == "TTN":
        #     send_files = TTN(1, 2)
        else:
            print("Нет такого файла, попробуй еще раз или напиши 'Exit' для выхода. Спасибо! :)")
            command = input(f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'").upper()



if __name__ == "__main__":
    main()