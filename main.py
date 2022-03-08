from lib.Device import Device
from lib.Colour import Colour
import tkinter as tk
from tkinter import *

pipico = Device("COM4", 115200)
pipico.connect()
colour = Colour()

app = tk.Tk()


def windows():
    app.title("RGB LED")
    app.geometry("400x400")
    data = pipico.read()
    colour.initColour(data)
    app.configure(background=colour.getHEX())
    app.after(100, windows)


app.after(100, windows)
app.mainloop()
