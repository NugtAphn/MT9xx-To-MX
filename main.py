import xml.dom.minidom
import datetime
import sys
from tkinter import *
from tkinter import filedialog
from convert.mt910.SplitBlock import *


def readFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    read = file.readlines()
    return read


def remove_empty_elements(element):
    for child in list(element):
        remove_empty_elements(child)
        if child.text is None and len(child) == 0:
            element.remove(child)
    if element.text is None and len(element) == 0:
        parent = element.find("..")
        if parent is not None:
            parent.remove(element)


def mapping():
    line = readFile()

    splitBlock1(line)
    splitBlock2(line)
    splitBlock3(line)
    splitBlock4(line)
    splitBlock5(line)

    currentTime = datetime.datetime.now()
    formattedTime = currentTime.strftime("%Y-%m-%dT%H:%M:%S.%f")

    header.set('xmlns', "urn:iso:std:iso:20022:tech:xsd:head.001.001.02")
    doc.set('xmlns', "urn:iso:std:iso:20022:tech:xsd:camt.054.001.08")

    header_b4.text = 'camt.054.001.08'
    header_b5.text = 'swift.cbprplus.02'
    header_b6.text = formattedTime.strip()
    doc_b12.text = formattedTime.strip()

    xml_header = ET.tostring(header, encoding="unicode", )
    xml_doc = ET.tostring(doc, encoding="unicode")

    sys.setrecursionlimit(10000)

    xmlHeader = ET.fromstring(xml_header)
    xmlDoc = ET.fromstring(xml_doc)

    remove_empty_elements(xmlHeader)
    remove_empty_elements(xmlDoc)

    headerXML = ET.tostring(xmlHeader)
    docXML = ET.tostring(xmlDoc)

    dom1 = xml.dom.minidom.parseString(headerXML)
    dom2 = xml.dom.minidom.parseString(docXML)

    header_xml = dom1.toprettyxml(indent="  ")
    doc_xml = dom2.toprettyxml(indent="  ")

    with open("acmt.054.001.08.xml", "w") as file:
        file.write(header_xml + '\n' + doc_xml)


if __name__ == '__main__':
    mapping()
    window = Tk()
    button = Button(text="open", command=readFile)
    button.pack()
    window.mainloop()
