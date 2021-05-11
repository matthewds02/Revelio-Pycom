from machine import UART

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=190)

def Sensor():
    while True:
        header_bytes = uart.read(1)
        HEADER = int(uart.read(1)[0])
        DATA_H = int(uart.read(2)[0])
        DATA_L = int(uart.read(3)[0])
        SUM = DATA_H*256 + DATA_L
        if int(SUM/10) < 1000 and int(SUM/10) > 10:
            print("LENGTE",int(SUM/10), "cm")
        if int(SUM/10) <= 10:
            print("Je komt wel heel dichtbij..., namelijk ",int(SUM/10), "cm")
