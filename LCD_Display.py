import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RS = 32
En = 26
D4 = 24
D5 = 22
D6 = 18
D7 = 16

lcd = LCD.Adafruit_CharLCD(RS, EN, D4, D5, D6, D7, 0, 16, 2)

lcd.message("Hello World!")
