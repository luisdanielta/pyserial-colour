from module.Device import Device
from module.Colour import Colour
import time

pipico = Device("COM4", 115200)
pipico.connect()
colour = Colour()

while True:
    data = pipico.read()
    colour.initColour(data)
    print('|- - - - - - - - -|')
    print(colour.getHEX())
    print(colour.getRGB())
    time.sleep(0.1)
