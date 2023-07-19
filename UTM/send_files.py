import os
from datetime import datetime, timezone
from time import sleep
from xml.etree import ElementTree as ET
import random
import string
import gen_bar


class Files:
    def WBGZ(bark1, bark2):
        os.system("scp d_kornilov@test-node03-nd:/home/ldapusers/d_kornilov/Marks.xml  /home/kornilov/Downloads")
        tree = ET.parse("/home/kornilov/Downloads/Marks.xml")
        root = tree.getroot()

        # print(root.tag)
        # print(root[0][1].text)
        n = random.randint(1000, 9999)
        # root[0][1].text = f"LOC-GZ-000000{n}"
        # print(root[0][1].text)
        # print(root[0][2].text)
        date = str(datetime.now())[:10]
        # root[0][2].text = date
        # print(root[0][2].text)
        # print(root[0][3].text)
        # root[0][3].text = random.randint(1, 9999)
        # print(root[0][3].text)
        for j in root.iter():
            if j.tag == "{http://fsrar.ru/WEGAIS/goznak}DocId":
                print(j.text)
                j.text = f"LOC-GZ-000000{n}"
                print(j.text)
            elif j.tag == "{http://fsrar.ru/WEGAIS/goznak}DocDate":
                print(j.text)
                j.text = date
                print(j.text)
            elif j.tag == "{http://fsrar.ru/WEGAIS/goznak}Form2":
                print(j.text)
                j.text = f"TEST-FB-000000{n}"
                print(j.text)
            elif j.tag == "{http://fsrar.ru/WEGAIS/goznak}bc":
                print(j[0].text)
                bar = gen_bar.Bark()
                j[0].text = str(*bar.get_new(1))
                bark1 = j[0].text
                print(j[0].text)
                print(j[1].text)
                j[1].text = str(*bar.get_new(1))
                bark2 = j[1].text
                print(j[1].text)
        os.system("rm /home/kornilov/Downloads/Marks.xml")
        tree.write(f"WBGZ.xml", encoding="UTF-8", xml_declaration=True)
        os.system("scp /home/kornilov/PycharmProjects/pythonProject/WBGZ.xml d_kornilov@test-node03-nd:./")
        os.system("ssh Bark_test")
        os.system("curl -F file=@- http://10.10.4.247:8002/wb < WBGZ.xml")



    def RP(bark1, bark2):
        tree = ET.parse("/mnt/Dmitriy_test/Produce_requests/RepProd_v4.xml")
        root = tree.getroot()
        print(root.tag)
        print([elem.tag for elem in root.iter()])
        for i in root.iter():
            if i.tag == "{http://fsrar.ru/WEGAIS/RepProducedProduct_v4}NUMBER":
                i.text = str(random.randint(0, 1000))
                print(i.text)
            elif i.tag == "{http://fsrar.ru/WEGAIS/RepProducedProduct_v4}Date" or i.tag == "{http://fsrar.ru/WEGAIS/RepProducedProduct_v4}ProducedDate":
                get_date = str(datetime.now())[:10]
                i.text = get_date
                print(i.text)
            elif i.tag == "{http://fsrar.ru/WEGAIS/RepProducedProduct_v4}MarkInfo":
                # bar = gen_bar.Bark()
                print(i[0].text)
                i[0].text = bark1
                print(i[0].text)
                print(i[1].text)
                i[1].text = bark2
                print(i[1].text)
        n = random.randint(1, 9)
        tree.write(f"RP.xml", encoding="UTF-8", xml_declaration=True)
        m = os.system(
            "curl -F'xml_file=@/home/kornilov/PycharmProjects/pythonProject/RP.xml' http://localhost:8080/opt/in/RepProducedProduct_v4")

bark1 = ""
bark2 = ""
# Files.WBGZ(bark1, bark2)
# Files.RP(bark1, bark2)
print(bark1, bark2)