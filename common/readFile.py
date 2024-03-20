from tkinter import filedialog


def readFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    read = file.readlines()
    return read
