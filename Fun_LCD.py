import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO
import digitalio
import board
import dht11

# initalize gpio mode and disable warnings
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

#lcd display configuration here 16*2 LCD module
def lcd_display_config():
    lcd_columns = 16
    lcd_rows = 2

# LCD pin config with Raspberry pi
def lcd_gpio_config():
    lcd_rs=digitalio.DigitalInOut(board.D26)
    lcd_en=digitalio.DigitalInOut(board.D19)
    lcd_d7=digitalio.DigitalInOut(board.D27)                                
    lcd_d6=digitalio.DigitalInOut(board.D22)                        
    lcd_d5=digitalio.DigitalInOut(board.D24)
    lcd_d4=digitalio.DigitalInOut(board.D25)

#defining class for LCD
def lcd_class():
    lcd=characterlcd.Character_LCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)

# Define class for DHT11 sensor
def dht_class():
    data = dht11.DHT11(pin=2)

#Display message on LCD display
def lcd_message():
    lcd.clear()
    lcd.message=("Welcome")
    delay()
    lcd.message=("Yash Technologies")
    delay()
    lcd.clear()

#Reading DHT11 sensor (temperature and Humidity)
def read_dht11():
    result=data.read()
    temp=result.temperature
    hum=result.humidity
    return (temp,hum)

#Display temperature and Humidity on LCD display
def display_dht11_message(temp,hum):
    lcd.message=("Temp:" +str(temp)+"C" +"\nHumidity:" +str(hum)+"%")
    delay()

#Delay funtion    
def delay():
    time.sleep(2)


init_gpio()
lcd_display_config()
lcd_gpio_config()
lcd_class()
dht_class()


while True:
    lcd_message()

    if result.is_valid():
         #print("Temp: %0.1f C" % result.temperature +' '+"Humid: %0.2f %%" % result.humidity)
         temp,hum=read_dht11()
         print(temp+"in C")
         print(hum+"in %")
         display_dht11_message(temp,hum)
    
