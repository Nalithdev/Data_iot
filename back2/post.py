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
temperature = ADC(Pin(34))
led = Pin(24, Pin.OUT)

positioning = "middle"
while not wlan.isconnected():
    print('noco')
    time.sleep(1)

while True :


    time.sleep(0.3)
    temps = temperature.read_u16()/65535*24
    if temps >= 20:
        led.on()

    else:
        let.off()


    try:
        print("GET")

        dataP = {"position": str(xposi)}
        r = urequests.get("http://192.168.100.131:3000/")

        print(r.json())

        r.close()
        time.sleep(1)
    except Exception as e:
        print(e)
