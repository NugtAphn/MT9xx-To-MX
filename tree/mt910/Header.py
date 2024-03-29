import xml.etree.ElementTree as ET

header = ET.Element('AppHdr')

header_b1 = ET.SubElement(header, 'Fr')
header_b11 = ET.SubElement(header_b1, 'FIId')
header_b111 = ET.SubElement(header_b11, 'FinInstnId')
header_b1111 = ET.SubElement(header_b111, 'BICFI')

header_b2 = ET.SubElement(header, 'Fr')
header_b21 = ET.SubElement(header_b2, 'FIId')
header_b211 = ET.SubElement(header_b21, 'FinInstnId')
header_b2111 = ET.SubElement(header_b211, 'BICFI')

header_b3 = ET.SubElement(header, 'BizMsgIdr')
header_b4 = ET.SubElement(header, 'MsgDefIdr')
header_b5 = ET.SubElement(header, 'BizSvc')
header_b6 = ET.SubElement(header, 'MktPrctc')
header_b61 = ET.SubElement(header_b6, 'Regy')
header_b62 = ET.SubElement(header_b6, 'Id')

header_b7 = ET.SubElement(header, 'CreDt')
header_b8 = ET.SubElement(header, 'PssblDplct')
header_b9 = ET.SubElement(header, 'Prty')