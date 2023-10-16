import xml.etree.ElementTree as ET
from random import randint
from datetime import datetime
import UTM.gen_bar
import os
class RP:
    namespaces = {
    'oref': "{http://fsrar.ru/WEGAIS/ClientRef_v2}",
    'pref': "{http://fsrar.ru/WEGAIS/ProductRef_v2}",
    'rpp': "{http://fsrar.ru/WEGAIS/RepProducedProduct_v4}",
    'ns': "{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}",
    'xsi': "{http://www.w3.org/2001/XMLSchema-instance}",
    'ce': "{http://fsrar.ru/WEGAIS/CommonV3}"
    }
    def __init__(self, values):
        self.__dict__.update(values)
    def remove_tags(self, root):
        for parent in root.findall(f'.//{self.namespaces["rpp"]}MarkInfo'):
            for d in root.findall(f'.//{self.namespaces["rpp"]}MarkInfo/'):
                print(parent.tag)
                parent.remove(d)
    def add_tags(self, get_mark_tag):
        number = 0
        for parent in range(self.__dict__['Quantity']):
            amc = ET.SubElement(get_mark_tag, f'{self.namespaces["ce"]}amc')
            amc.text = self.__dict__['amc'][number]
            number += 1
    def constructor(self):
        tree = ET.parse('/mnt/Dmitriy_test/Produce_requests/RP.xml')
        root = tree.getroot()
        root.find(f'.//{self.namespaces["ns"]}FSRAR_ID').text = str(self.__dict__['FSRAR_ID'])
        root.find(f'.//{self.namespaces["rpp"]}Identity').text = str(self.__dict__['Identity'])
        root.find(f'.//{self.namespaces["rpp"]}NUMBER').text = str(self.__dict__['Number'])
        root.find(f'.//{self.namespaces["rpp"]}Date').text = str(self.__dict__['Date'])
        root.find(f'.//{self.namespaces["rpp"]}ProducedDate').text = str(self.__dict__['Date'])
        root.find(f'.//{self.namespaces["oref"]}ClientRegId').text = str(self.__dict__['FSRAR_ID'])
        root.find(f'.//{self.namespaces["oref"]}KPP').text = str(self.__dict__['KPP'])
        root.find(f'.//{self.namespaces["oref"]}Country').text = str(self.__dict__['Country'])
        root.find(f'.//{self.namespaces["oref"]}RegionCode').text = str(self.__dict__['RegionCode'])
        root.find(f'.//{self.namespaces["oref"]}description').text = str(self.__dict__['Adress'])
        root.find(f'.//{self.namespaces["rpp"]}ProductCode').text = str(self.__dict__['ProductCode'])
        root.find(f'.//{self.namespaces["rpp"]}Quantity').text = str(self.__dict__['Quantity'])
        root.find(f'.//{self.namespaces["rpp"]}alcPercent').text = str(self.__dict__['alcPercent'])
        self.remove_tags(root)
        get_mark_tag = root.find(f'.//{self.namespaces["rpp"]}MarkInfo')
        self.add_tags(get_mark_tag)
        tree = ET.ElementTree(root)
        tree.write('RP.xml', encoding="UTF-8", xml_declaration=True)
        # self.send()
    def send(self):
        os.system("curl -F'xml_file=@/home/kornilov/PycharmProjects/pythonProject/UTM/XML_Files/RP.xml' http://localhost:8080/opt/in/RepProducedProduct_v4")



def main():
    print('Добавление параметров для XML')
    if input('Если вы хотите изменить параметры организации, напишите - 1\n') == '1':
        parametrs['FSRAR_ID'] = input('Введите ФСРАР организации; Example: "030000434307"\n')
        parametrs['Identity'] = randint(1, 9999)
        parametrs['Number'] = randint(1, 9999)
        parametrs['Date'] = datetime.now().strftime('%Y-%m-%d')
        parametrs['KPP'] = input('Введите kpp организации; Example: "770101007"\n')
        parametrs['Country'] = input('Введите  код страны организации; Example: "643"\n')
        parametrs['RegionCode'] = input('Введите код региона организации; Example: "77"\n')
        parametrs['Adress'] = input('Введите адрес организации; Example: "Россия,117105,Москва Г, Варшавское ш, д. 37 А, стр. 8"\n')
        parametrs['ProductCode'] = input('Введите алкод продукта; Example: "0300004343070000124"\n')
        parametrs['Quantity'] = int(input('Введите количество марок; Example: "4"\n'))
        parametrs['alcPercent'] = input('Введите процент алкоголя в продукции; Example: "8"\n')
        marks = UTM.gen_bar.Bark().get_new(parametrs['Quantity'])
        parametrs['amc'] = marks
    else:
        parametrs['FSRAR_ID'] = "030000434307"
        parametrs['Identity'] = randint(1, 9999)
        parametrs['Number'] = randint(1, 9999)
        parametrs['Date'] = datetime.now().strftime('%Y-%m-%d')
        parametrs['KPP'] = "770101007"
        parametrs['Country'] = "643"
        parametrs['RegionCode'] = "77"
        parametrs['Adress'] = "Россия,117105,Москва Г, Варшавское ш, д. 37 А, стр. 8"
        parametrs['ProductCode'] = "0300004343070000124"
        parametrs['Quantity'] = int("4")
        parametrs['alcPercent'] = "8"
        marks = UTM.gen_bar.Bark().get_new(parametrs['Quantity'])
        parametrs['amc'] = marks
parametrs = dict()
main()
print(parametrs)
document = RP(parametrs)
document.constructor()




