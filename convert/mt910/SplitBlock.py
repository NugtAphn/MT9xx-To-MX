import re
from tree.mt910.Header import *
from tree.mt910.Body import *


def splitBlock1(line):
    lstLine = re.findall(r'{([^{}]+)}', line[0])
    block1 = []
    for i in lstLine:
        if i[0:2] == '1:':
            block1.append(i[:])
    appID = block1[0][2:3]
    serviceID = block1[0][3:5]
    BIC12 = block1[0][5:17]
    sessionDigit = block1[0][17:21]
    sequenceDigit = block1[0][21:27]
    header_b2111.text = BIC12.strip()


def splitBlock2(line):
    lstLine = re.findall(r'{([^{}]+)}', line[0])
    block2 = []
    for i in lstLine:
        if i[0:2] == '2:':
            block2.append(i[:])
    for i in block2:
        if i[2:3] == 'I':
            appHeader = i[2:3]
            msgType = i[3:6]
            BIC12 = i[6:18]
            priority = i[18:19]
            deliver = i[19:20]
            period = i[20:22]
            header_b1111.text = BIC12.strip()
        elif i[2:3] == 'O':
            appHeader = i[2:3]
            msgType = i[3:6]
            inTime = i[6:10]
            inDate = i[10:16]
            BIC12 = i[16:28]
            sessionDigit = i[28:32]
            sequenceDigit = i[32:38]
            outDate = i[38:44]
            outTime = i[44:48]
            priority = i[-1:]
            header_b1111.text = BIC12.strip()


def splitBlock3(line):
    tags = ['103', '113', '108', '119', '423',
            '106', '424', '111', '121', '115',
            '165', '433', '434']
    lstLine = re.findall(r'{([^{}]+)}', line[0])
    block3 = []
    for i in lstLine:
        if i[0:3] in tags:
            block3.append(i[:])
    for i in block3:
        if i[0:3] == '103':
            serviceId = i[4:7]
        elif i[0:3] == '113':
            bankPrty = i[4:8]
        elif i[0:3] == '108':
            MUR = i[4:20]
        elif i[0:3] == '119':
            valFlag = i[4:12]
        elif i[0:3] == '423':
            balDttm = i[4:18]
        elif i[0:3] == '106':
            date = i[0:5]
            BIC12 = i[5:17]
            sessionDigit = i[17:21]
            sequenceDigit = i[21:27]
        elif i[0:3] == '424':
            relRef = i[4:20]
        elif i[0:3] == '111':
            serviceId = i[4:7]
        elif i[0:3] == '121':
            transRef = i[4:]
        elif i[0:3] == '115':
            addressInfo = i[4:36]
        elif i[0:3] == '165':
            paymentInfo = i[5:8]
            adtnInfo = i[9:]
        elif i[0:3] == '433':
            srceenInfo = i[5:8]
            adtnInfo = i[9:]
        elif i[0:3] == '434':
            paymentInfo = i[5:8]
            adtnInfo = i[9:]


def splitBlock4(line):
    tags = ['13', '20', '21', '25', '32',
            '50', '52', '56', '72']
    characters = ['{', ':', '-']
    block4 = []
    for i in line:
        if i[1:3] in tags:
            block4.append(i[:])
        elif i[0] not in characters:
            if len(block4) != 0:
                block4[-1] += i
    for i in block4:
        if i[1:3] == '20':
            msgId = i[4:]
            header_b3.text = msgId.strip()
            doc_b11.text = msgId.strip()
            doc_b21.text = msgId.strip()
            doc_b231.text = msgId.strip()
        elif i[1:3] == '21':
            receiverRef = i[4:]
            doc_b238111.text = receiverRef.strip()
        elif i[1:3] == '25':
            if i[3:4] == '':
                accCode = i[4:]
                doc_b22111.text = accCode.strip()
            elif i[3:4] == 'P':
                accCode = i[4:]
                doc_b22111.text = accCode.strip()
        elif i[1:3] == '13':
            datetime = ('20' + i[5:7]
                        + '-' + i[7:9]
                        + '-' + i[9:11]
                        + 'T' + i[11:13]
                        + ':' + i[13:15]
                        + ':00.000' + i[15:18]
                        + ':' + i[18:20])
            doc_b2351.text = datetime.strip()
        elif i[1:3] == '32':
            date = ('20' + i[5:7]
                    + '-' + i[7:9]
                    + '-' + i[9:11])
            currency = i[11:14]
            amount = i[14:-1]
            doc_b2361.text = date.strip()
            doc_b238161.text = date.strip()
            doc_b222.text = currency.strip()
            doc_b232.text = amount.strip()
            doc_b232.set('Ccy', currency)
            doc_b23812.text = amount.strip()
            doc_b23812.set('Ccy', currency)
        elif i[1:3] == '50':
            if i[3:4] == 'A':
                doc_b238141 = ET.SubElement(doc_b23814, 'Dbtr')
                doc_b2381411 = ET.SubElement(doc_b238141, 'Pty')
                doc_b23814111 = ET.SubElement(doc_b2381411, 'Id')
                doc_b238141111 = ET.SubElement(doc_b23814111, 'OrgId')
                doc_b2381411111 = ET.SubElement(doc_b238141111, 'AnyBIC')
                doc_b238142 = ET.SubElement(doc_b23814, 'DbtrAcct')
                doc_b2381421 = ET.SubElement(doc_b238142, 'Id')
                doc_b23814211 = ET.SubElement(doc_b2381421, 'Othr')
                doc_b238142111 = ET.SubElement(doc_b23814211, 'Id')
                splitPart = i.split("\n")
                accountId = splitPart[0].split(":")[2]
                idCode = splitPart[1]
                doc_b2381411111.text = idCode.strip()
                doc_b238142111.text = accountId.strip()
            elif i[3:4] == 'K':
                doc_b238141 = ET.SubElement(doc_b23814, 'Dbtr')
                doc_b2381411 = ET.SubElement(doc_b238141, 'Pty')
                doc_b23814111 = ET.SubElement(doc_b2381411, 'Nm')
                doc_b23814112 = ET.SubElement(doc_b2381411, 'PstlAdr')
                doc_b238141121 = ET.SubElement(doc_b23814112, 'AdrLine')
                doc_b238141122 = ET.SubElement(doc_b23814112, 'AdrLine')
                doc_b238141123 = ET.SubElement(doc_b23814112, 'AdrLine')
                doc_b238142 = ET.SubElement(doc_b23814, 'DbtrAcct')
                doc_b2381421 = ET.SubElement(doc_b238142, 'Id')
                doc_b23814211 = ET.SubElement(doc_b2381421, 'Othr')
                doc_b238141111 = ET.SubElement(doc_b23814211, 'Id')
                splitPart1 = i.split("\n")
                partyIdentifier = splitPart1[0].split(":")[2]
                splitPart2 = partyIdentifier.split('/')
                ID = splitPart2[1]
                doc_b238141111.text = ID.strip()
                for j, part in enumerate(splitPart1):
                    if j == 1:
                        name = part if part else None
                        doc_b23814111.text = name
                    elif j == 2:
                        address1 = part if part else None
                        doc_b238141121.text = address1
                    elif j == 3:
                        address2 = part if part else None
                        doc_b238141122.text = address2
                    elif j == 4:
                        address3 = part if part else None
                        doc_b238141123.text = address3
            elif i[3:4] == 'F':
                doc_b238141 = ET.SubElement(doc_b23814, 'Dbtr')
                doc_b2381411 = ET.SubElement(doc_b238141, 'Pty')
                doc_b23814111 = ET.SubElement(doc_b2381411, 'Nm')
                doc_b23814112 = ET.SubElement(doc_b2381411, 'PstlAdr')
                doc_b238141121 = ET.SubElement(doc_b23814112, 'TwnNm')
                doc_b238141122 = ET.SubElement(doc_b23814112, 'Ctry')
                doc_b238141123 = ET.SubElement(doc_b23814112, 'AdrLine')
                doc_b23814113 = ET.SubElement(doc_b2381411, 'Id')
                doc_b238141131 = ET.SubElement(doc_b23814113, 'PrvtId')
                doc_b2381411311 = ET.SubElement(doc_b238141131, 'DtAndPlcOfBirth')
                doc_b23814113111 = ET.SubElement(doc_b2381411311, 'BirthDt')
                doc_b23814113112 = ET.SubElement(doc_b2381411311, 'CityOfBirth')
                doc_b23814113113 = ET.SubElement(doc_b2381411311, 'CtryOfBirth')
                doc_b238141132 = ET.SubElement(doc_b23814113, 'Othr')
                doc_b2381411321 = ET.SubElement(doc_b238141132, 'Id')
                doc_b2381411322 = ET.SubElement(doc_b238141132, 'SchmeNm')
                doc_b23814113221 = ET.SubElement(doc_b2381411322, 'Cd')
                doc_b2381411323 = ET.SubElement(doc_b238141132, 'Issr')
                doc_b238141133 = ET.SubElement(doc_b23814113, 'Othr')
                doc_b2381411331 = ET.SubElement(doc_b238141133, 'Id')
                doc_b2381411332 = ET.SubElement(doc_b2381411331, 'SchmeNm')
                doc_b23814113321 = ET.SubElement(doc_b2381411332, 'Cd')
                doc_b238142 = ET.SubElement(doc_b23814, 'DbtrAcct')
                doc_b2381421 = ET.SubElement(doc_b238142, 'Id')
                doc_b23814211 = ET.SubElement(doc_b2381421, 'IBAN')
                doc_b238142111 = ET.SubElement(doc_b23814211, 'Id')
                doc_b23814212 = ET.SubElement(doc_b2381421, 'Othr')
                doc_b238142121 = ET.SubElement(doc_b23814212, 'Id')
                splitPart1 = i.split('\n')
                line1 = splitPart1[0].split(':')[2]
                line2 = splitPart1[1]
                line3 = splitPart1[2]
                line4 = splitPart1[3]
                line5 = splitPart1[4]
                splitPart2 = line1.split('/')
                print(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5)

        elif i[1:3] == '52':
            if i[3:4] == 'A':
                doc_b23815111 = ET.SubElement(doc_b2381511, 'BICFI')
                doc_b23815112 = ET.SubElement(doc_b2381511, 'Othr')
                doc_b238151121 = ET.SubElement(doc_b23815112, 'Id')
                splitPart1 = i.split("\n")
                partyIdentifier = splitPart1[0].split(":")[2]
                splitPart2 = partyIdentifier.split('/')
                idCode = splitPart1[1]
                for j, part in enumerate(splitPart2):
                    if j == 2:
                        partyID = part if part else None
                        doc_b23815111.text = partyID.strip()
                doc_b238151121.text = idCode.strip()
            elif i[3:4] == 'D':
                doc_b23815111 = ET.SubElement(doc_b2381511, 'Nm')
                doc_b23815112 = ET.SubElement(doc_b2381511, 'PstlAdr')
                doc_b238151121 = ET.SubElement(doc_b23815112, 'AdrLine')
                doc_b238151122 = ET.SubElement(doc_b23815112, 'AdrLine')
                doc_b238151123 = ET.SubElement(doc_b23815112, 'AdrLine')
                doc_b23815113 = ET.SubElement(doc_b2381511, 'Othr')
                doc_b238151131 = ET.SubElement(doc_b23815113, 'Id')
                splitPart1 = i.split("\n")
                partyIdentifier = splitPart1[0].split(":")[2]
                splitPart2 = partyIdentifier.split('/')
                for j, part in enumerate(splitPart1):
                    if j == 1:
                        name = part if part else None
                        doc_b23815111.text = name
                    elif j == 2:
                        address1 = part if part else None
                        doc_b238151121.text = address1
                    elif j == 3:
                        address2 = part if part else None
                        doc_b238151122.text = address2
                    elif j == 4:
                        address3 = part if part else None
                        doc_b238151123.text = address3
                partyID = splitPart2[2]
                doc_b238151131.text = partyID
        elif i[1:3] == '56':
            if i[3:4] == 'A':
                doc_b23815211 = ET.SubElement(doc_b2381521, 'BICFI')
                doc_b23815212 = ET.SubElement(doc_b2381521, 'Othr')
                doc_b238152121 = ET.SubElement(doc_b23815212, 'Id')
                splitPart1 = i.split("\n")
                partyIdentifier = splitPart1[0].split(":")[2]
                splitPart2 = partyIdentifier.split('/')
                idCode = splitPart1[1]
                for j, part in enumerate(splitPart2):
                    if j == 2:
                        partyID = part if part else None
                        doc_b23815211.text = partyID.strip()
                doc_b238152121.text = idCode.strip()
            elif i[3:4] == 'D':
                doc_b23815211 = ET.SubElement(doc_b2381521, 'Nm')
                doc_b23815212 = ET.SubElement(doc_b2381521, 'PstlAdr')
                doc_b238152121 = ET.SubElement(doc_b23815212, 'AdrLine')
                doc_b238152122 = ET.SubElement(doc_b23815212, 'AdrLine')
                doc_b238152123 = ET.SubElement(doc_b23815212, 'AdrLine')
                doc_b23815213 = ET.SubElement(doc_b2381521, 'Othr')
                doc_b23815231 = ET.SubElement(doc_b23815213, 'Id')
                splitPart1 = i.split("\n")
                partyIdentifier = splitPart1[0].split(":")[2]
                splitPart2 = partyIdentifier.split('/')
                name = splitPart1[1]
                address1 = splitPart1[2]
                address2 = splitPart1[3]
                address3 = splitPart1[4]
                partyID = splitPart2[2]
                doc_b23815231.text = partyID.strip()
                doc_b238152121.text = address1
                doc_b238152122.text = address2
                doc_b238152123.text = address3
                doc_b23815211.text = name
        elif i[1:3] == '72':
            additionalInfo = i[4:]
            doc_b24.text = additionalInfo.replace('\n', '')


def splitBlock5(line):
    block5 = re.findall(r'{([^{}]+)}', line[-1])
    for i in block5:
        if i[0:3] == 'CHK':
            checkSum = i[4:]
        elif i[0:2] == 'TNG':
            msg = i[3:]
        elif i[0:2] == 'PDE':
            time = i[3:7]
            date = i[7:13]
            BIC12 = i[13:25]
            sessionDigit = i[25:29]
            sequenceDigit = i[29:35]
        elif i[0:2] == 'DLM':
            msg = i[3:]
        elif i[0:2] == 'MRF':
            date1 = i[3:9]
            time = i[9:13]
            date2 = i[13:19]
            BIC12 = i[19:31]
            sessionDigit = i[31:35]
            sequenceDigit = i[35:41]
        elif i[0:2] == 'PDM':
            time = i[3:7]
            date = i[7:13]
            BIC12 = i[13:25]
            sessionDigit = i[25:29]
            sequenceDigit = i[29:35]
        elif i[0:2] == 'SYS':
            time = i[3:7]
            date = i[7:13]
            BIC12 = i[13:25]
            sessionDigit = i[25:29]
            sequenceDigit = i[29:35]
