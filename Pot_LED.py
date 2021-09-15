import serial
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

p = GPIO.PWM(3,100)

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    s= str((int(ser.readline(),11)))
    print(s)
    p.start(int (s) )
