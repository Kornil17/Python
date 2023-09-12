import xml.etree.ElementTree as ET
tree = ET.parse('/mnt/Dmitriy_test/AWO&ACHR/AWO.xml')
root = tree.getroot()
print(root.tag.lstrip('{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}'))
print(root.find('.//{http://fsrar.ru/WEGAIS/ActWriteOff_v3}Identity').text)
namespaces = {
    'xsi': "{http://www.w3.org/2001/XMLSchema-instance}",
    'ns': "{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}",
    'pref': "{http://fsrar.ru/WEGAIS/ProductRef_v2}",
    'awr': "{http://fsrar.ru/WEGAIS/ActWriteOff_v3}",
    'ce': "{http://fsrar.ru/WEGAIS/CommonV3}"
}

print(root.find(f'.//{namespaces["awr"]}Identity').text)
print(root.find(f'.//{namespaces["awr"]}ActNumber').text)
print(root.find(f'.//{namespaces["awr"]}ActDate').text)
print(root.find(f'.//{namespaces["awr"]}TypeWriteOff').text)
root.find(f'.//{namespaces["awr"]}ActNumber') = 5


tree = ET.ElementTree(root)
tree.write('AWO.xml', encoding="UTF-8", xml_declaration=True)
