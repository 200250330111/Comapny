import adafruit_character_lcd.character_lcd as characterlcd
import RPi.GPIO as GPIO
import digitalio
import board
import time
import dht11

def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
#def lcd_display_config():
lcd_columns = 16
lcd_rows = 2
    
#def lcd_gpio_config():
lcd_rs=digitalio.DigitalInOut(board.D26)
lcd_en=digitalio.DigitalInOut(board.D19)
lcd_d7=digitalio.DigitalInOut(board.D27)                                
lcd_d6=digitalio.DigitalInOut(board.D22)                        
lcd_d5=digitalio.DigitalInOut(board.D24)
lcd_d4=digitalio.DigitalInOut(board.D25)
    
#def lcd_class():
lcd=characterlcd.Character_LCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)
data = dht11.DHT11(pin=2)

def ChangeCase(dir,mode):
        if mode == "Normal":
            if dir == 'd':
                newMode = 'FanControl'
                lcd.clear()
                lcd.message='FanControl'
                return newMode
            elif dir == 'a':
                newMode ='Normal'
                lcd.clear()
                lcd.message='Normal'
                return newMode
            elif dir == 's':
                newMode ='Normal'
                lcd.clear()
                lcd.message='Normal'
                return newMode
            elif dir == 'w':
                newMode = 'Normal'
                lcd.clear()
                lcd.message='Normal'
                return newMode

        if mode == "FanControl":
            if dir == 'd':
                newMode = 'Temperature'
                lcd.clear()
                lcd.message='Temperature'
                return newMode
            elif dir == 'a':
                newMode = 'Normal'
                lcd.clear()
                lcd.message='Normal'
                return newMode
            elif dir == 's':
                newMode = 'FanSpeed'
                lcd.clear()
                lcd.message='FanSpeed'
                return newMode
            elif dir == 'w':
                newMode ='FanControl'
                lcd.clear()
                lcd.message='FanControl'
                return newMode

        if mode == "FanSpeed":
            if dir == "d":
                newMode = 'FanRPM'
                lcd.clear()
                lcd.message='FanRPM'
                return newMode
            elif dir == "w":
                newMode = 'FanControl'
                lcd.clear()
                lcd.message='FanControl'
                return newMode
            elif dir == 's':
                newMode ='FanRPM'
                lcd.clear()
                lcd.message='FanRPM'
                return newMode
            elif dir == 'd':
                newMode = 'FanRPM'
                lcd.clear()
                lcd.message='FanRPM'
                return newMode

        if mode == "FanRPM":
            if dir == "a":
                newMode = 'FanSpeed'
                lcd.clear()
                lcd.message='FanSpeed'
                return newMode
            elif dir == "w":
                newMode = 'FanControl'
                lcd.clear()
                lcd.message='FanControl'
                return newMode
            elif dir == 's':
                newMode ='FanRPM'
                lcd.clear()
                lcd.message='FanRPM'
                return newMode
            elif dir == 'd':
                newMode = 'FanRPM'
                lcd.clear()
                lcd.message='FanRPM'
                return newMode

        if mode == "Temperature":
            if dir == "a":
                newMode = 'FanControl'
                lcd.clear()
                lcd.message='FanControl'
                return newMode
            elif dir == 's':
                newMode = 'Temperature'
                lcd.message='Temperature'
                lcd.clear()
                return newMode
            elif dir == 'w':
                newMode = 'Temperature'
                lcd.clear()
                lcd.message='Temperature'
                return NewMode
            elif dir == 'd':
                newMode = 'Temperature'
                lcd.clear()
                lcd.message='Temperature'
                return newMode


def DisplayMode(mode):
    if mode == 'FanSpeed':
        print("Adjusting Fan speed\n")
        time.sleep(2)
        lcd.clear()
        lcd.message='Adjusting Fan \nspeed'
    if mode == 'FanRPM':
        print("Display Fan Rpm\n")
        time.sleep(2)
        lcd.clear()
        lcd.message='Display Fan Rpm'
    if mode == 'Temperature':
        print("Display Temperature\n")
        time.sleep(2)
        lcd.clear()
        lcd.message='Display Temperature'
        time.sleep(1)
        lcd.clear()
        display_dht11_message(temp,hum)

def read_dht11():
    print("Inside read_dht11")
    result=data.read()
    temp=result.temperature
    hum=result.humidity
    if result.is_valid():
        return (temp,hum)
    else:
        return read_dht11()

def display_dht11_message(temp,hum):
        lcd.message=("Temp:" +str(temp)+"C" +"\nHumidity:" +str(hum)+"%")
        time.sleep(1)
  
    


newMode = 'Normal'
lcd.message='Normal'
init_gpio()


while True:
    temp,hum=read_dht11()
    dir = input()
    Mode = ChangeCase(dir,newMode)
    newMode = Mode
    print("Changed to",Mode," mode")
    DisplayMode(Mode)
    

