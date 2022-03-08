from module.Device import Device
from module.Colour import Colour
import tkinter as tk
from tkinter import *

pipico = Device("COM4", 115200)
pipico.connect()
colour = Colour()

app = tk.Tk()
app.geometry("400x400")


def windows():
    data = pipico.read()
    colour.initColour(data)
    app.configure(background=colour.getHEX())
    title = "RGB: {} - HEX: {}".format(colour.getRGB(), colour.getHEX())
    app.title(title)
    app.after(100, windows)


app.after(100, windows)
app.mainloop()
