import RPi.GPIO as GPIO
import time
import serial


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
if __name__ =='__main__':    
    ser= serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()

    while True:
        # s= ser.readline.decode('utf-8').rstrip()
        if ser.in_waiting > 0:
            s= (ser.readline().decode('utf-8').rstrip())
            #s= str(((ser.readline(),2)))
            print(s)
            if float (s) > 33:
                print("Temperature:-%f ", s)
                GPIO.output(3, GPIO.HIGH)
            else:
                GPIO.output(3, GPIO.LOW)

        
