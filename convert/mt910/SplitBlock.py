import re
from tree.mt910 import *


def splitBlock1(line):
    listLine1 = re.findall(r'{([^{}]+)}', line[0])
    block1 = []
    for i in listLine1:
        if i[0:2] == '1:':
            block1.append(i[:])
    appID = block1[0][2:3]
    serviceID = block1[0][3:5]
    BIC11 = block1[0][5:17]
    sessionDigit = block1[0][17:21]
    sequenceDigit = block1[0][21:27]
    print(len(block1))
    print('1. Application ID: ' + appID + '\n' +
          '2. Service ID: ' + serviceID + '\n' +
          '3. Business Identify Code: ' + BIC11 + '\n' +
          '4. Session Digit: ' + sessionDigit + '\n' +
          '5. Sequence Digit: ' + sequenceDigit)


def splitBlock2(line):
    listLine1 = re.findall(r'{([^{}]+)}', line[0])
    block2 = []

    for i in listLine1:
        if i[0:2] == '2:':
            block2.append(i[:])

    appHeader = block2[0][2:3]
    msgType = block2[0][3:6]
    inTime = block2[0][3:6]
    inDate = block2[0][3:6]
    BIC11 = block2[0][3:6]
    sessionDigit = block2[0][17:21]
    sequenceDigit = block2[0][21:27]
    outTime = block2[0][3:6]
    outDate = block2[0][3:6]
    priority = block2[0][-1:]
    print('1. Application Header ID: ' + appHeader + '\n' +
          '2. Message Type: ' + msgType + '\n' +
          '3. Input Time: ' + inTime + '\n' +
          '4. Input Date: ' + inDate + '\n' +
          '5. Business Identify Code: ' + BIC11 + '\n' +
          '6. Session Digit: ' + sessionDigit + '\n' +
          '7. Sequence Digit: ' + sequenceDigit + '\n' +
          '8. Output Time: ' + outTime + '\n' +
          '9. Output Date: ' + outDate + '\n' +
          '10. Priority Code: ' + priority)


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
