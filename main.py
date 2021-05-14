from ultrasonic import *
import LORAWAN

if LORAWAN.connect():
    while True:
        Sensor()
        LORAWAN.send(SUM)
