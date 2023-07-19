import os
from datetime import datetime, timezone
from time import sleep
from xml.etree import ElementTree as ET
import random
import string
from xml.etree.ElementTree import fromstring

import gen_bar
import gen_bar2
import subprocess
import SQL_Connect


marks = list()
def RP():
    # 11 15 18 19 20
    result = list()
    r = random.randint(1000, 9999)
    r1 = random.randint(1, 9999)
    date1 = str(datetime.now())[:10]
    print(date1)
    bar = gen_bar.Bark()
    with open('/home/kornilov/PycharmProjects/pythonProject/WBGZ.xml', 'r') as op:
        m = op.readlines()
        print(m[17])
        for i in range(len(m)):
            if i >= 17 and  "<gz:NCode>" in m[i]:
                m[i] = m[i].replace("<gz:NCode>", "<ce:amc>")
                m[i] = m[i].replace("</gz:NCode>", "</ce:amc>")
                marks.append(m[i])
                print(m[i])
                print(i)


    with open('/mnt/Dmitriy_test/Produce_requests/RP.xml', 'r') as f:
        n = f.readlines()
        for i in range(len(n)):
            if i == 10:
                line11 = n[i].rstrip()
                print(line11[line11.find(">") + 1:line11.find("</")])
                line11 = line11.replace("030000434307", f"030000434307")
                print(line11)
                result.append(line11)
            elif i == 14:
                line15 = n[i].rstrip()
                print(line15[line15.find(">") + 1:line15.find("</")])
                line15 = line15.replace("1", f"{r1}")
                print(line15)
                result.append(line15)
            elif i == 17:
                line18 = n[i].rstrip()
                print(line18[line18.find(">") + 1:line18.find("</")])
                line18 = line18.replace("1", f"{r1}")
                print(line18)
                result.append(line18)
            elif i == 18 or i == 19:
                lines = n[i].rstrip()
                print(lines[lines.find(">") + 1:lines.find("</")])
                lines = lines.replace("2023-07-12", f"{date1}")
                print(lines)
                result.append(lines)
            elif i == 39:
                line40 = n[i].rstrip()
                print(line40[line40.find(">") + 1:line40.find("</")])
                line40 = line40.replace("2", f"{str(len(marks))}")
                print(line40)
                result.append(line40)
            elif i == 48:
                for i in range(len(marks)):
                    # x = "<ce:amc>705564591946380535179MKOONVOPJLOETZ0PNE5LBJU9F2IQ2RFHS5V1ZB2E7KFOWPQL3G8U52Y4RLEJYB5S8OMJ7OZRXAYK4P7MNDTM9FK1MSD7RONKBNY771P3MK46NZAXWRCA3N0B6HK7K9OJE</ce:amc>"
                    # x = x.replace("705564591946380535179MKOONVOPJLOETZ0PNE5LBJU9F2IQ2RFHS5V1ZB2E7KFOWPQL3G8U52Y4RLEJYB5S8OMJ7OZRXAYK4P7MNDTM9FK1MSD7RONKBNY771P3MK46NZAXWRCA3N0B6HK7K9OJE",f"{marks[i]}")
                    x =f"{marks[i]}"

                    print(x)
                    result.append(x)
                b = ["</rpp:MarkInfo>", "</rpp:Position>", "</rpp:Content>", "</ns:RepProducedProduct_v4>", "</ns:Document>","</ns:Documents>"]
                for i in range(len(b)):
                    result.append(b[i])
            elif i < 47:
                result.append(n[i].rstrip())


    os.system("touch RP.xml")
    with open('RP.xml', 'w') as op:
        for i in range(len(result)):
            op.write(str(result[i]) + '\n')
    os.system("curl -F'xml_file=@/home/kornilov/PycharmProjects/pythonProject/RP.xml' http://localhost:8080/opt/in/RepProducedProduct_v4")


def TTN():
# 3, 7, 9, 10, 11,
    tree = ET.parse("TTN.xml")
    root = tree.getroot()
    print(root)
    r = random.randint(1000, 9999)
    date1 = str(datetime.now())[:10]
    # print(date1)
    bar = gen_bar.Bark()
    for elm in root.findall(".//"):
        print(elm.tag)
        if elm.tag == "{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}FSRAR_ID":
            elm.text = "030000434307"
            print(elm.tag)
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/TTNSingle_v4}Identity":
            elm.text = r
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/TTNSingle_v4}NUMBER":
            elm.text = r
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/TTNSingle_v4}Date" or "{http://fsrar.ru/WEGAIS/TTNSingle_v4}ShippingDate":
            elm.text = date1
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/TTNSingle_v4}Quantity":
            elm.text = len(marks)
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/TTNSingle_v4}FARegId":
            c = SQL_Connect.SQL()
            c.SQL_Postgres("docs")
            # TEST - FA - 0000000
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/CommonV3}F2RegId":
            print(elm.text)
        elif elm.tag == "{http://fsrar.ru/WEGAIS/CommonV3}amclist":
            print(elm.text)
        elif elm.tag == elm.tag:
            elm.text = elm.text
            print(elm.text, elm.tag)
    tree.write('TTN.xml')








def WBGZ():
    # 6, 7, 8, 16, after 18
    result = list()
    marks = list()
    r = random.randint(1000, 9999)
    date = str(datetime.now())[:10]
    print(date)
    bar = gen_bar.Bark()
    gz = int(input("Введите количество марок ...:,'\n'"))
    with open('/mnt/Dmitriy_test/Marks/Marks.xml', 'r') as f:
        n = f.readlines()
        for i in range(len(n)):
            if i == 0:
                b = ["<?xml version='1.0' encoding='utf-8'?>",
                     '<ns:Documents xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"',
                     'xmlns:gz="http://fsrar.ru/WEGAIS/goznak">', "<ns:Header>",
                     "<gz:DocType>WayBillGoznak</gz:DocType>"]
                for i in range(len(b)):
                    result.append(b[i])
            elif i == 5:
                line6 = n[i].rstrip()
                print(line6[line6.find(">") + 1:line6.find("</")])
                line6 = line6.replace("LOC-GZ-0000004111", f"LOC-GZ-000000{r}")
                print(line6)
                result.append(line6)
            elif i == 6:
                line7 = n[i].rstrip()
                print(line7[line7.find(">") + 1:line7.find("</")])
                line7 = line7.replace("2023-05-25", f"{date}")
                print(line7)
                result.append(line7)
            elif i == 7:
                line8 = n[i].rstrip()
                print(line8[line8.find(">") + 1:line8.find("</")])
                line8 = line8.replace("1", f"{r}")
                print(line8)
                result.append(line8)
                result.append('<gz:shipperID>030000253368</gz:shipperID>')
                result.append('<gz:ConsigneeID>030000434307</gz:ConsigneeID>')
                result.append('<gz:typeclaim>1</gz:typeclaim>')
                result.append(
                    '<gz:Content xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01" xmlns:gz="http://fsrar.ru/WEGAIS/goznak">')
                result.append('<gz:Pos>')
                result.append('<gz:DocPosId>1</gz:DocPosId>')
            elif i == 15:
                line16 = n[i].rstrip()
                print(line16[line16.find(">") + 1:line16.find("</")])
                line16 = line16.replace("TEST-FB-0000004555", f"TEST-FB-000000{r}")
                print(line16)
                result.append(line16)
                result.append('<gz:bc xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"')
                result.append('xmlns:gz="http://fsrar.ru/WEGAIS/goznak">')
            elif i == 17:
                # gz = int(input("Введите количество марок ...:,'\n'"))
                for i in range(gz):
                    x = str(*bar.get_new(1))
                    x1 = f"<gz:NCode>{x}</gz:NCode>"
                    print(x1)
                    result.append(x1)
                    # marks.append(x1)
                b = ["</gz:bc>", "</gz:Pos>", "</gz:Content>", "</ns:Header>", "</ns:Documents>"]
                for i in range(len(b)):
                    result.append(b[i])
    os.system("touch WBGZ.xml")
    with open('WBGZ.xml', 'w') as op:
        for i in range(len(result)):
            op.write(str(result[i]) + '\n')
    os.system("scp /home/kornilov/PycharmProjects/pythonProject/WBGZ.xml d_kornilov@test-node03-nd:./")
    # os.system("ssh Bark_test")
    # os.system("curl -F file=@- http://10.10.4.247:8002/wb < WBGZ.xml")
    bshCmd = 'ssh -T Bark_test'
    process = subprocess.Popen(bshCmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)
    n = process.stdin.write("curl -F file=@- http://10.10.4.247:8002/wb < WBGZ.xml")
    print(n)
    process.stdin.close()



def AA():
    a = 1


def AR():
    a = 1


def AD():
    a = 1


commands = {'RP': RP, 'WBGZ': WBGZ, 'TTN': TTN, 'AA': AA, 'AR': AR, 'AD': AD}
request = input(f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'")
command = request.upper()
print(command)
while command != "EXIT":
    if command in ['WBGZ', 'RP', 'TTN', 'AA', 'AR', 'AD']:
        commands[command]()
        request = input(
            f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'")
        command = request.upper()
    else:
        print("Нет такого файла, попробуй еще раз или напиши 'Exit' для выхода. Спасибо! :)")
        request = input(
            f"Напишите название файла для отправки в УТМ: WBGZ,RP,TTN,AA,AR,AD или Exit для отключения,'\n'")
        command = request.upper()
