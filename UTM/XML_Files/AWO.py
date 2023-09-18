import xml.etree.ElementTree as ET
from random import randint
from datetime import datetime
import UTM.gen_bar
class AWO:
    namespaces = {
    'xsi': "{http://www.w3.org/2001/XMLSchema-instance}",
    'ns': "{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}",
    'pref': "{http://fsrar.ru/WEGAIS/ProductRef_v2}",
    'awr': "{http://fsrar.ru/WEGAIS/ActWriteOff_v3}",
    'ce': "{http://fsrar.ru/WEGAIS/CommonV3}"
    }
    def __init__(self, values):
        self.__dict__.update(values)
    def constructor(self):
        tree = ET.parse('/mnt/Dmitriy_test/AWO&ACHR/AWO.xml')
        root = tree.getroot()
        root.find(f'.//{self.namespaces["ns"]}FSRAR_ID').text = str(self.__dict__['FSRAR_ID'])
        root.find(f'.//{self.namespaces["awr"]}Identity').text = str(self.__dict__['Identity'])
        root.find(f'.//{self.namespaces["awr"]}ActNumber').text = str(self.__dict__['ActNumber'])
        root.find(f'.//{self.namespaces["awr"]}ActDate').text = str(self.__dict__['ActDate'])
        root.find(f'.//{self.namespaces["awr"]}TypeWriteOff').text = str(self.__dict__['TypeWriteOff'])
        mark = 0
        for amc in root.findall(f'.//{self.namespaces["ce"]}amc'):
            amc.text = str(self.__dict__['amc'][mark])
            mark += 1
        tree = ET.ElementTree(root)
        print(type(tree))
        tree.write('AWO.xml', encoding="UTF-8", xml_declaration=True)



def main():
    print('Добавление параметров для XML')
    parametrs['document_path'] = '/mnt/Dmitriy_test/AWO&ACHR/AWO.xml'
    parametrs['FSRAR_ID'] = input('Введите ФСРАР организации\n')
    parametrs['Identity'] = randint(1, 9999)
    parametrs['ActNumber'] = randint(1, 9999)
    parametrs['ActDate'] = datetime.now().strftime('%Y-%m-%d')
    parametrs['TypeWriteOff'] = input('Введите тип Акта списания (Пересортица, Излишки)\n')
    # parametrs['Quantity'] = int(input('Введите количество марок для XML\n'))
    parametrs['Quantity'] = 2
    marks = UTM.gen_bar.Bark().get_new(parametrs['Quantity'])
    parametrs['amc'] = marks

parametrs = dict()
main()
print(parametrs)
document = AWO(parametrs)
document.constructor()




#
# tree = ET.parse('/mnt/Dmitriy_test/AWO&ACHR/AWO.xml')
# root = tree.getroot()
# # print(root.tag.lstrip('{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}'))
# # print(root.find('.//{http://fsrar.ru/WEGAIS/ActWriteOff_v3}Identity').text)
# namespaces = {
#     'xsi': "{http://www.w3.org/2001/XMLSchema-instance}",
#     'ns': "{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}",
#     'pref': "{http://fsrar.ru/WEGAIS/ProductRef_v2}",
#     'awr': "{http://fsrar.ru/WEGAIS/ActWriteOff_v3}",
#     'ce': "{http://fsrar.ru/WEGAIS/CommonV3}"
# }
# print(root.find(f'.//{namespaces["ns"]}FSRAR_ID').text)
# print(root.find(f'.//{namespaces["awr"]}Identity').text)
# print(root.find(f'.//{namespaces["awr"]}ActNumber').text)
# print(root.find(f'.//{namespaces["awr"]}ActDate').text)
# print(root.find(f'.//{namespaces["awr"]}TypeWriteOff').text)
# # print(root.find(f'.//{namespaces["ce"]}amc').text)
# for i in root.findall(f'.//{namespaces["ce"]}amc'):
#     print(i.text)
#     i.text = '000564591946380535177MKOONVOPJLOETZ0PNE5LBJU9F2IQ2RFHS5V1ZB2E7KFOWPQL3G8U52Y4RLEJYB5S8OMJ7OZRXAYK4P7MNDTM9FK1MSD7RONKBNY771P3MK46NZAXWRCA3N0B6HK7K9OJE'
# root.find(f'.//{namespaces["awr"]}TypeWriteOff').text = '1005'
# tree = ET.ElementTree(root)
# print(tree)
# tree.write('AWO.xml', encoding="UTF-8", xml_declaration=True)
