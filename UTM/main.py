import xml.etree.ElementTree as ET
import requests as rq
# <?xml version="1.0" encoding="UTF-8"?>
# <ns:Documents Version="1.0"
#    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
#    xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"
#    xmlns:ck="http://fsrar.ru/WEGAIS/ChequeV3"
# 	xmlns:oref="http://fsrar.ru/WEGAIS/ClientRef_v2"
# 	xmlns:pref="http://fsrar.ru/WEGAIS/ProductRef_v2">
# <ns:Owner>
#   <ns:FSRAR_ID>030000428196</ns:FSRAR_ID>
# </ns:Owner>
# <ns:Document>
#   <ns:ChequeV3>
#     <ck:Identity>1</ck:Identity>
#     <ck:Header>
#       <ck:Date>2023-05-19T14:35:00</ck:Date>
#       <ck:Kassa>1</ck:Kassa>
#       <ck:Shift>2</ck:Shift>
#       <ck:Number>2</ck:Number>
#       <ck:Type>Продажа</ck:Type>
#     </ck:Header>
#     <ck:Content>
# <ck:Bottle>
# <ck:Barcode>197400052808600121236SESHLHTLUAFHYP3BW5JSADDSCQRNDVJKWY2YI3QLB5YR4D4QOP2ZZ3T67KHFKIE2R5TYAHX43QSFKHWSA7I7XUY5V35N3AGDK7DTDQHYZ7GUGHMXEFDCN22VIWVSNORVI</ck:Barcode>
# <ck:EAN>5010196091008</ck:EAN>
# <ck:Price>1.00</ck:Price>
# </ck:Bottle>
#     </ck:Content>
#   </ns:ChequeV3>
# </ns:Document>
# </ns:Documents>

# с немспейсами
# ns = '{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}'
# cq = '{http://fsrar.ru/WEGAIS/Cheque}'
# root = et.Element(ns + 'Document')
# et.SubElement(root, cq + 'Bottle').text = 'some 1'
# et.dump(root)
# bo = root.find(cq + 'Bottle').text
# print(bo)
# exit()
# tree = ET.ElementTree(root)
# tree.write("sales_receipt.xml", encoding="UTF-8", xml_declaration=True)
n = ["Version=1.0","{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}","{http://fsrar.ru/WEGAIS/Cheque}","{http://fsrar.ru/WEGAIS/Cheque}"]
root = ET.Element('Documents')
for i in n:
    root.set(i, "")
for i in root.find("Documents"):
    print(i.tag,i.attrib)
