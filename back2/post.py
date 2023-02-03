from machine import ADC, Pin
import network
import urequests
import ujson
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Nalith'
password = 'Drakspears'
wlan.connect(ssid, password)
url = "http://192.168.100.131:3000/pos"
"""
ssid = 'PLTEL'
password = '12345678'
wlan.connect(ssid, password)
url = "http://192.168.43.90:3000/pos"

ssid = 'Pierro-Access-point'
password = '123456789'
wlan.connect(ssid, password)
url = "http:/192.168.4.9:3000/pos"
"""
vertical = ADC(Pin(28))

positioning = "middle"
while not wlan.isconnected():
    print('noco')
    time.sleep(1)

while True :


    time.sleep(0.3)
    xposi = vertical.read_u16()
    if xposi >= 30000 and xposi <= 40000:
        positioning = "middle"

    elif xposi <= 70000 and xposi >= 36000:
        positioning = "up"

    elif xposi >= 600 and xposi <= 30000:
        positioning = "down"

    print(xposi)
    try:
        print("POST")

        dataP = {"position": str(xposi)}
        #r = urequests.get("http://192.168.100.131:3000/")
        r = urequests.post(url, headers = {'content-type': 'application/json'},data=dataP)
        print(r.json())

        r.close()
        time.sleep(1)
    except Exception as e:
        print(e)
