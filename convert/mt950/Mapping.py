from convert.mt950.SplitBlock import *
import datetime
import sys
from common.reformatXML import *
import xml.dom.minidom


def mapping950(line):
    splitBlock1(line)
    splitBlock2(line)
    splitBlock3(line)
    splitBlock4(line)
    splitBlock5(line)

    currentTime = datetime.datetime.now()
    formattedTime = currentTime.strftime("%Y-%m-%dT%H:%M:%S.%f")

    header_b4.text = 'camt.053.001.12'
    header_b5.text = 'swift.cbprplus.02'
    header_b6.text = formattedTime.strip()
    doc_b12.text = formattedTime.strip()

    xml_root = ET.tostring(root, encoding="unicode", )

    sys.setrecursionlimit(10000)

    xmlRoot = ET.fromstring(xml_root)

    remove_empty_elements(xmlRoot)

    rootXML = ET.tostring(xmlRoot)

    rootET = ET.fromstring(rootXML)

    for elem in rootET.iter():
        if not hasattr(elem.tag, 'find'):
            continue
        i = elem.tag.find('}')
        if i >= 0:
            elem.tag = elem.tag[i + 1:]

    rootXML = ET.tostring(rootET, encoding='unicode', method='xml')

    dom = xml.dom.minidom.parseString(rootXML)

    root_xml = dom.toprettyxml(indent="  ")

    with open("example/mx/acmt.053.001.xx.xml", "w") as file:
        file.write(root_xml)
