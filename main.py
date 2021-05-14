from ultrasonic import *
import loraWAN
import wifi
import pycom

wifi.wifi_connect()
if loraWAN.connect():
    while True:
        Sensor()
        distance = Sensor()
        loraWAN.send(distance)
