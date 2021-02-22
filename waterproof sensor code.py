from machine import UART, Pin
from micropyGPS import MicropyGPS
import time

uart = UART(1,9600, pins = ('P21','P22'))
uart.init(9600,bits = 8, parity = None, stop = 1)

while(True):
    if(uart.any()):
        a = uart.read(100)
        print(a)
    else:
        print("No data")