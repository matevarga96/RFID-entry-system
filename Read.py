#!/usr/bin/env python                           #megadja a terminálnak, hogyan fordítsa a filet, és hogy pythont használjon

                                
import RPi.GPIO as GPIO                         #Rpi.GPIO-ban vannak azok a funkciók, amik a Pinekkel foglalkoznak

reader = SimpleMFRC522()                        #csinál egy objektumot a könyvtárból, és meghívja a setup funkcióját

try:
        id, text = reader.read()                #a read funkció meghívása, beolvasás
        print(id)                               
        print(text)                             #beolvasott adatok megjelenítése
finally:                                        #try után fut le
        GPIO.cleanup()                          #feltakarítunk magunk után
