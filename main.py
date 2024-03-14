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
    # splitBlock1(line)
    # splitBlock2(line)
    # splitBlock3(line)
    splitBlock5(line)
    window = Tk()
    button = Button(text="open", command=readFile)
    button.pack()
    window.mainloop()
