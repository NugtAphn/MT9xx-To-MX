from convert.mt910.Mapping import mapping
from common.readFile import *
from tkinter import *


if __name__ == '__main__':
    line = readFile()
    mapping(line)
    window = Tk()
    button = Button(text="open", command=readFile)
    button.pack()
    window.mainloop()
