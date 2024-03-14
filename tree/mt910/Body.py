import xml.etree.ElementTree as ET

doc = ET.Element('Document')
doc_b = ET.SubElement(doc, 'BkToCstmrDbtCdtNtfctn')

doc_b1 = ET.SubElement(doc_b, 'GrpHdr')
doc_b11 = ET.SubElement(doc_b1, 'MsgId')
doc_b12 = ET.SubElement(doc_b1, 'CreDtTm')
doc_b2 = ET.SubElement(doc_b, 'Ntfctn')
doc_b21 = ET.SubElement(doc_b2, 'Id')
doc_b22 = ET.SubElement(doc_b2, 'Acct')
doc_b221 = ET.SubElement(doc_b22, 'Id')
doc_b2211 = ET.SubElement(doc_b221, 'Othr')
doc_b22111 = ET.SubElement(doc_b2211, 'Id')
doc_b222 = ET.SubElement(doc_b22, 'Ccy')
doc_b23 = ET.SubElement(doc_b2, 'Ntry')
doc_b231 = ET.SubElement(doc_b23, 'NtryRef')
doc_b232 = ET.SubElement(doc_b23, 'Amt')
doc_b233 = ET.SubElement(doc_b23, 'CdtDbtInd')
doc_b234 = ET.SubElement(doc_b23, 'Sts')
doc_b2341 = ET.SubElement(doc_b234, 'Cd')
doc_b235 = ET.SubElement(doc_b23, 'BookgDt')
doc_b2351 = ET.SubElement(doc_b235, 'DtTm')
doc_b236 = ET.SubElement(doc_b23, 'ValDt')
doc_b2361 = ET.SubElement(doc_b236, 'Dt')
doc_b237 = ET.SubElement(doc_b23, 'BkTxCd')
doc_b2371 = ET.SubElement(doc_b237, 'Domn')
doc_b23711 = ET.SubElement(doc_b2371, 'Cd')
doc_b23712 = ET.SubElement(doc_b2371, 'Fmly')
doc_b237121 = ET.SubElement(doc_b23712, 'Cd')
doc_b237122 = ET.SubElement(doc_b23712, 'SubFmlyCd')
doc_b238 = ET.SubElement(doc_b23, 'NtryDtls')
doc_b2381 = ET.SubElement(doc_b238, 'TxDtls')
doc_b23811 = ET.SubElement(doc_b2381, 'Refs')
doc_b238111 = ET.SubElement(doc_b23811, 'InstrId')
doc_b23812 = ET.SubElement(doc_b2381, 'Amt')
doc_b23813 = ET.SubElement(doc_b2381, 'CdtDbtInd')
doc_b23814 = ET.SubElement(doc_b2381, 'RltdPties')
doc_b238141 = ET.SubElement(doc_b23814, 'Dbtr')
doc_b2381411 = ET.SubElement(doc_b238141, 'Pty')
doc_b23814111 = ET.SubElement(doc_b2381411, 'Id')
doc_b238141111 = ET.SubElement(doc_b23814111, 'OrgId')
doc_b2381411111 = ET.SubElement(doc_b238141111, 'AnyBIC')
doc_b238142 = ET.SubElement(doc_b23814, 'Dbtr')
doc_b2381421 = ET.SubElement(doc_b238142, 'Id')
doc_b23814211 = ET.SubElement(doc_b2381421, 'Othr')
doc_b238142111 = ET.SubElement(doc_b23814211, 'Id')
doc_b23815 = ET.SubElement(doc_b2381, 'RltdAgts')
doc_b238151 = ET.SubElement(doc_b23815, 'DbtrAgt')
doc_b2381511 = ET.SubElement(doc_b238151, 'FinInstnId')
doc_b23815111 = ET.SubElement(doc_b2381511, 'BICFI')
doc_b23815112 = ET.SubElement(doc_b2381511, 'Othr')
doc_b238151121 = ET.SubElement(doc_b23815112, 'Id')
doc_b238152 = ET.SubElement(doc_b23815, 'IntrmyAgt1')
doc_b2381521 = ET.SubElement(doc_b238152, 'FinInstnId')
doc_b23815211 = ET.SubElement(doc_b2381521, 'BICFI')
doc_b23815212 = ET.SubElement(doc_b2381521, 'Othr')
doc_b238152121 = ET.SubElement(doc_b23815212, 'Id')
doc_b23816 = ET.SubElement(doc_b2381, 'RltdDts')
doc_b238161 = ET.SubElement(doc_b23816, 'IntrBkSttlmDt')
doc_b24 = ET.SubElement(doc_b2, 'AddtlNtfctnInf')













