import digitalio
import board
import RPi.GPIO as GPIO
import dht11
import time
import adafruit_character_lcd.character_lcd as characterlcd

#Initialise GPIO for LCD and DHT11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


lcd_columns = 16
lcd_rows = 2

lcd_rs=digitalio.DigitalInOut(board.D26)
lcd_en=digitalio.DigitalInOut(board.D19)
lcd_d7=digitalio.DigitalInOut(board.D27)                                
lcd_d6=digitalio.DigitalInOut(board.D22)                        
lcd_d5=digitalio.DigitalInOut(board.D24)
lcd_d4=digitalio.DigitalInOut(board.D25)

#Initialize LCD class and read data using GPIO2

lcd=characterlcd.Character_LCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)

data = dht11.DHT11(pin=2)


while True:
    result=data.read()
    temp=result.temperature
    hum=result.humidity


    #clearing LCD
    lcd.clear()

    #Printing message
    lcd.message=("Welcome")
    time.sleep(2)
    lcd.message=("Yash Technologies")
    time.sleep(2)
    lcd.clear()

    #printing temperature and humidity
    if result.is_valid():
        print("Temp: %0.1f C" % result.temperature +' '+"Humid: %0.2f %%" % result.humidity)
        lcd.message=("Temp:" + str(temp)+ "C" + "\nHumidity:" +str(hum)+"%")
        time.sleep(2)
