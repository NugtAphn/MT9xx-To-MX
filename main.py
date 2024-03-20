from common.chooseFile import *
from tkinter import *


if __name__ == '__main__':
    chooseFile()
    window = Tk()
    button = Button(text="open", command=readFile)
    button.pack()
    window.mainloop()
