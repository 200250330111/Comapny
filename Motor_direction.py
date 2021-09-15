import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
#P=GPIO.PWM(3, 100)


while True:
    #P.start(0)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    #P.start(100)
    print("Motor in FORWARD direction")
    time.sleep(7)

    #P.start(100)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    #P.start(0)
    print("Motor in REVERSE direction\n")
    time.sleep(7)
    
