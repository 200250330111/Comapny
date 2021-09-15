# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**connect to raspberry pi
# 16: LCD Backlight GND

import time 
import board 
import digitalio 
import adafruit_character_lcd.character_lcd as characterlcd 

# Modify this if you have a different sized character LCD 
lcd_columns = 16 
lcd_rows = 2


#Pin Config: 
lcd_rs = digitalio.DigitalInOut(board.D26) 
lcd_en = digitalio.DigitalInOut(board.D19) 
lcd_d7 = digitalio.DigitalInOut(board.D27) 
lcd_d6 = digitalio.DigitalInOut(board.D22) 
lcd_d5 = digitalio.DigitalInOut(board.D24) 
lcd_d4 = digitalio.DigitalInOut(board.D25) 
lcd_backlight = digitalio.DigitalInOut(board.D15)

 # Initialise the LCD class
lcd = characterlcd.Character_LCD_Mono( lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight )

#Power up
lcd.message= "Powering up"
time.sleep(0.75)
lcd.clear()
lcd.message="Start LCD \n  Testing"
time.sleep(0.75)
lcd.clear()

#check backlight
lcd.message ="Checking \nBacklight"
time.sleep(0.75)
lcd.clear()
lcd.backlight = False
time.sleep(0.5)
lcd.backlight = True
time.sleep(0.5)
lcd.backlight = False
time.sleep(0.5)
lcd.backlight = True
lcd.message =" Backlight is OK..."
time.sleep(0.5)
lcd.clear()

# Display cursor 
lcd.clear()
lcd.message = "Checking Cursor"
time.sleep(0.75)
lcd.clear()
lcd.cursor = True 
time.sleep(0.5)
lcd.cursor = False
time.sleep(0.5)
lcd.message= "Cursor is Ok"
time.sleep(0.75)

#Blink cursor
lcd.clear()
lcd.message ="Blink \ntesting"
time.sleep(0.5)
lcd.clear()
lcd.blink =True
time.sleep(0.5)
lcd.blink =False
lcd.message ="Blink is Ok"
time.sleep(0.5)
lcd.clear()

#test cursor and position
st="A"
lcd.message= "Testing cursor\n Position"
time.sleep(0.5)
lcd.clear()
for i in range(16):
    lcd.cursor_position(i,0)
    print(i)
    lcd.message = st
    lcd.blink = True
    time.sleep(0.005)
for j in range(16):
    lcd.cursor_position(j,1)
    lcd.blink =True
    lcd.message= str(j)
    time.sleep(0.005)
    
lcd.clear()
lcd.blink = False
lcd.cursor = False
lcd.cursor_position(0,0)
lcd.message= "Cursor position \nOK......"
time.sleep(0.5)
lcd.clear()

#LCD display Line i.e.16*2
lcd.message="Testing Display\nLines....."
time.sleep(0.5)
lcd.clear()
lcd.message="1234567890123456\nabcdefghijklmnop"
time.sleep(0.5)
lcd.clear()
lcd.message="Line 1 is Ok....\nLine 2 is Ok...."
time.sleep(0.75)
lcd.clear()

# Create message to scroll
lcd.message="Test Scrolling"
time.sleep(0.35)
lcd.clear()
scroll_msg = "<-- Scroll_left"
lcd.message = scroll_msg 

# Scroll message to the left 
for i in range(len(scroll_msg)): 
    time.sleep(0.05) 
    lcd.move_left() 
lcd.clear()

#scroll to right
scroll_msg ="Scroll_right-->"
lcd.message = scroll_msg
for i in range(len(scroll_msg)):
    time.sleep(0.05)
    lcd.move_right()
lcd.clear()

#Scroll to left
lcd.message = "Scrolling is \ngood!"
time.sleep(0.5)
lcd.clear()

lcd.message ="Clearing Screen"
time.sleep(0.5)
lcd.clear()

lcd.message= "Turning Off\nBacklight "
time.sleep(0.5)
lcd.clear()

# Turn backlight off
lcd.backlight = False 
time.sleep(1)

