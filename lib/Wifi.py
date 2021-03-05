#https://docs.pycom.io/tutorials/networks/wlan/
from network import WLAN
import machine

def Wifi():
    wlan = WLAN(mode=WLAN.STA)

    wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
    while not wlan.isconnected():
        machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())

