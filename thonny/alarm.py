import network
from ssd1306 import SSD1306_I2C
import urequests
import utime
import ujson
from machine import Pin, I2C
import utime

wlan = network.WLAN(network.STA_IF)  # met la raspi en mode client wifi
wlan.active(True)  # active le mode client wifi

ssid = 'iPhone de Félix'
password = '12345678'
wlan.connect(ssid, password)  # connecte la raspi au réseau
url = "http://172.20.10.6:3000/send"


while not wlan.isconnected():
    print("pas co")
    pass


pin_button = Pin(22, mode=Pin.IN)
led = Pin(5, mode=Pin.OUT)

LARGEUR = 128
HAUTEUR = 32

i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)

oled = SSD1306_I2C(LARGEUR, HAUTEUR, i2c)


buzzer = Pin(14, Pin.OUT)

while True:
    buzzer.value(0)
    led.off()

    if pin_button.value() == 1:
        print("INTRUSION")
        oled.fill(0)
        oled.text('DETECTED !', 30, 7)
        oled.show()
        utime.sleep(3)

        for i in range(0, 6):
            oled.fill(0)
            oled.text('ALARME', 48, 4)
            oled.text('DANS', 55, 13)
            oled.text(str(5-i), 66, 22)
            oled.rect(16, 1, 112, 31, 1)
            oled.show()
            utime.sleep(1)
            oled.fill(0)

        print("GET")
        r = urequests.get(url)  # lance une requete sur l'url
        r.close()  # ferme la demande

        for i in range(0, 10):
            oled.text('WARNING', 45, 6)
            oled.show()
            buzzer.value(1)
            led.on()
            utime.sleep(1)
            led.off()
            oled.fill(0)
            oled.show()
            utime.sleep(1)
        buzzer.value(0)

    else:
        led.off()
        buzzer.value(0)
