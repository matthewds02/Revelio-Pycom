#https://docs.pycom.io/tutorials/networks/wlan/
from network import WLAN
import machine

def wifi_connect():
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid='Ken', auth=(WLAN.WPA2, 'Welcome2hpcds'))
    while not wlan.isconnected():
        machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())
