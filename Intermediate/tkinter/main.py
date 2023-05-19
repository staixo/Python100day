import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#install("tk")

import tkinter


my_label = tkinter.Label(text="Hello World")
my_label.pack()


window = tkinter.Tk()

window.mainloop()