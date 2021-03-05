from machine import UART

uart = None

def uart():
    global uart
    uart = UART(1)
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3','P4'))