import re
from tree.mt950.Root import *


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

            if priority == 'U':
                header_b7.text = 'HIGH'
            elif priority == 'N':
                header_b7.text = 'NORM'

    for i in block2:
        if i[3:6] == '950':
            print('')


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
    tags = ['20', '25', '28', '60', '61',
            '62', '64']
    characters = ['{', ':', '-']
    block4 = []

    for i in line:
        if i[1:3] in tags:
            block4.append(i[:])

        elif i[0] not in characters:
            if len(block4) != 0:
                block4[-1] += i

    count = 0
    for val in block4:
        if val[1:3] == '61':
            count += 1

    for i in block4:
        if i[1:3] == '20':
            msgId = i[4:]
            header_b3.text = msgId.strip()
            doc_b11.text = msgId.strip()
            doc_b21.text = msgId.strip()

        elif i[1:3] == '25':
            accID = i[4:]
            doc_b210121.text = accID.strip()

        elif i[1:4] == '28C':
            splitPart = i.split(':')[2]

            if '/' in splitPart:
                seqNb = splitPart.split('/')[0] if splitPart.split('/')[0] else None
                pgNb = splitPart.split('/')[1] if splitPart.split('/')[1] else None
                doc_b23.text = seqNb.strip()
                doc_b221.text = pgNb.strip()
            else:
                seqNb = i[5:]
                doc_b23.text = seqNb.strip()


        # elif i[1:3] == '60':
        #     if i[3:4] == 'F':
        #
        #
        #     elif i[3:4] == 'M':



def splitBlock5(line):
    block5 = re.findall(r'{([^{}]+)}', line[-1])

    for i in block5:
        if i[0:3] == 'CHK':
            checkSum = i[4:]

        elif i[0:3] == 'TNG':
            msg = i[4:]

        elif i[0:3] == 'PDE':
            time = i[4:8]
            date = i[8:14]
            BIC12 = i[14:26]
            sessionDigit = i[26:30]
            sequenceDigit = i[30:36]

        elif i[0:3] == 'DLM':
            msg = i[4:]

        elif i[0:3] == 'MRF':
            date1 = i[4:10]
            time = i[10:14]
            date2 = i[14:20]
            BIC12 = i[20:32]
            sessionDigit = i[32:36]
            sequenceDigit = i[36:42]

        elif i[0:3] == 'PDM':
            time = i[4:8]
            date = i[8:14]
            BIC12 = i[14:26]
            sessionDigit = i[26:30]
            sequenceDigit = i[30:36]

        elif i[0:3] == 'SYS':
            time = i[4:8]
            date = i[8:14]
            BIC12 = i[14:26]
            sessionDigit = i[26:30]
            sequenceDigit = i[30:36]
