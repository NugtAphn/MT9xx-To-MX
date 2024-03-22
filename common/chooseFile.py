import re
from common.readFile import *
from convert.mt910.Mapping import mapping910
from convert.mt950.Mapping import mapping950


def chooseFile():
    line = readFile()
    lstLine = re.findall(r'{([^{}]+)}', line[0])
    block = []

    for i in lstLine:
        if i[0:2] == '2:':
            block.append(i[:])

    for i in block:
        if i[3:6] == '900':
            print('Not Done Yet')
        elif i[3:6] == '910':
            mapping910(line)
        elif i[3:6] == '940':
            print('Not Done Yet')
        elif i[3:6] == '942':
            print('Not Done Yet')
        elif i[3:6] == '950':
            mapping950(line)