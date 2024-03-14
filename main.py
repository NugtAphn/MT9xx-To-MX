import xml.dom.minidom
from tkinter import *
from tkinter import filedialog
from convert.mt910.SplitBlock import *


def readFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    read = file.readlines()
    return read


if __name__ == '__main__':
    line = readFile()
    splitBlock1(line)
    splitBlock2(line)
    splitBlock3(line)
    splitBlock4(line)
    splitBlock5(line)
    xml_header = ET.tostring(header, encoding="utf-8")
    xml_doc = ET.tostring(doc, encoding="utf-8")
    dom1 = xml.dom.minidom.parseString(xml_header)
    dom2 = xml.dom.minidom.parseString(xml_doc)
    header_xml = dom1.toprettyxml(indent="  ")
    doc_xml = dom2.toprettyxml(indent="  ")
    # with open("new_file.xml", "w") as file:
    #     file.write(header_xml + '\n' + doc_xml)
    print(header_xml + '\n' + doc_xml)
    window = Tk()
    button = Button(text="open", command=readFile)
    button.pack()
    window.mainloop()
