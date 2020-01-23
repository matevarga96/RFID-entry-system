#!/usr/bin/env python      #megadja a terminálnak, hogyan fordítsa a filet, és hogy pythont használjon

import RPi.GPIO as GPIO                #Rpi.GPIO-ban vannak azok a funkciók, amik a Pinekkel foglalkoznak, szükségünk lesz ezekre hogy futás után üres legyen minden
from mfrc522 import SimpleMFRC522      #a SimpleMFRC522 könyvtárt fogjuk használni, hogy kommunikáljunk az RFID RC522-vel, amit könnyebb használni a chip alapkönyvtáránál 

reader = SimpleMFRC522()               #csinál egy objektumot a könyvtárból, és meghívja a setup funkcióját

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
