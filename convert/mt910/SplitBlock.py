import re
from tree.mt910 import *


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
    print(len(block1))
    print('1. Application ID: ' + appID + '\n' +
          '2. Service ID: ' + serviceID + '\n' +
          '3. Business Identify Code: ' + BIC12 + '\n' +
          '4. Session Digit: ' + sessionDigit + '\n' +
          '5. Sequence Digit: ' + sequenceDigit)


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
            print('1. Application Header ID: ' + appHeader + '\n' +
                  '2. Message Type: ' + msgType + '\n' +
                  '3. Business Identify Code: ' + BIC12 + '\n' +
                  '4. Priority Code: ' + priority + '\n' +
                  '5. Delivery Monitoring: ' + deliver + '\n' +
                  '6. Obsolescence Period: ' + period)
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
            print('1. Application Header ID: ' + appHeader + '\n' +
                  '2. Message Type: ' + msgType + '\n' +
                  '3. Input Time: ' + inTime + '\n' +
                  '4. Input Date: ' + inDate + '\n' +
                  '5. Business Identify Code: ' + BIC12 + '\n' +
                  '6. Session Digit: ' + sessionDigit + '\n' +
                  '7. Sequence Digit: ' + sequenceDigit + '\n' +
                  '8. Output Date: ' + outDate + '\n' +
                  '9. Output Time: ' + outTime + '\n' +
                  '10. Priority Code: ' + priority)


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
            print('103 - Service Identifier: ' + serviceId)
        elif i[0:3] == '113':
            bankPrty = i[4:8]
            print('113 - Banking Priority: ' + bankPrty)
        elif i[0:3] == '108':
            MUR = i[4:20]
            print('108 - Message User Reference: ' + MUR)
        elif i[0:3] == '119':
            valFlag = i[4:12]
            print('119 - Validation Flag: ' + valFlag)
        elif i[0:3] == '423':
            balDttm = i[4:18]
            print('423 - Balance checkpoint date and time: ' + balDttm)
        elif i[0:3] == '106':
            date = i[0:5]
            BIC12 = i[5:17]
            sessionDigit = i[17:21]
            sequenceDigit = i[21:27]
            print('106 - 1. Date: ' + date + '\n' +
                  '2. Business Identify Code: ' + BIC12 + '\n' +
                  '3. Session Digit: ' + sessionDigit + '\n' +
                  '4. Sequence Digit' + sequenceDigit)
        elif i[0:3] == '424':
            relRef = i[4:20]
            print('424 - Related reference: ' + relRef)
        elif i[0:3] == '111':
            serviceId = i[4:7]
            print('111 - Service type identifier: ' + serviceId)
        elif i[0:3] == '121':
            transRef = i[4:]
            print('121 - Unique end-to-end transaction reference: ' + transRef)
        elif i[0:3] == '115':
            addressInfo = i[4:36]
            print('115 - Addressee Information: ' + addressInfo)
        elif i[0:3] == '165':
            paymentInfo = i[5:8]
            adtnInfo = i[9:]
            print('165 - 1. Payment release information receiver : ' + paymentInfo)
            print('2. Additional Information: ' + adtnInfo)
        elif i[0:3] == '433':
            srceenInfo = i[5:8]
            adtnInfo = i[9:]
            print('433 - 1. Payment release information receiver : ' + srceenInfo)
            print('2. Additional Information: ' + adtnInfo)
        elif i[0:3] == '434':
            paymentInfo = i[5:8]
            adtnInfo = i[9:]
            print('434 - 1. Payment release information receiver : ' + paymentInfo)
            print('2. Additional Information: ' + adtnInfo)


def splitBlock4(line):
    tags = ['13D', '20', '21', '25a', '32A',
            '50a', '52a', '56a', '72']
    characters = ['{', ':', '-']
    block4 = []

    for i in line:
        if i[1:4] in tags:
            block4.append(i[:])
        elif i[0] not in characters:
            if len(block4) != 0:
                block4[-1] += i


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
