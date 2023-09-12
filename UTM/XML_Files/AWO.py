import xml.etree.ElementTree as ET
tree = ET.parse('/mnt/Dmitriy_test/AWO&ACHR/AWO.xml')
root = tree.getroot()
print(root.tag.lstrip('{http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01}'))
for child in root:
    print(child.tag, child.attrib)
print(root.findtext("//Document/Identity/text()"))
