import xml.etree.ElementTree as ET

def make_lowercase(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for element in root.iter():
        if element.text is not None:
            element.text = element.text.lower()

    tree.write(xml_file, encoding="utf-8")

make_lowercase('example.xml')