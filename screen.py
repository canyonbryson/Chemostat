import busio
from adafruit_mcp3xxx.analog_in import AnalogIn
import os
import glob
import board
import subprocess
import time
#time.sleep(60)
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)




# setup for the screen
# Using for SPI
spi = board.SPI()
oled_reset = digitalio.DigitalInOut(board.D17)
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_reset, oled_cs)


try: 
    # Load font.
    font = ImageFont.truetype('/home/pi/Chemostat/arial.ttf', 12)
except:
    font = ImageFont.load_default()   
    
timer = 120
while timer >= 0:
    timer -= 1
    try:
                # get the IP address
        IP = str(subprocess.check_output(["hostname", "-I"]).split()[0])
        IP = IP[2:-1]
    except:
        IP = ""
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (oled.width, oled.height))
        # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
        # Draw Some Text
    draw.text((1, 1), 'Initializing...', font = font, fill = 255)
    draw.text((1,15), str(timer), font=font, fill=255)
    draw.text((1,30), "IP: " + str(IP), font=font, fill=255)     
        # Display image
    oled.image(image)
    oled.show()
    time.sleep(1)
    
