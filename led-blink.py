import RPi.GPIO as GPIO
import time

ledPin = 11 # RPI Board pin11

def setup():
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(ledPin, GPIO.OUT) # Set ledPin's mode is output
    GPIO.output(ledPin, GPIO.LOW) # Set ledPin low to off led
    print ('using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH) # led on
        print ('...led on')
        time.sleep(1) # delay 1 second
        GPIO.output(ledPin, GPIO.LOW) # led off
        print ('led off...')
        time.sleep(1)

def destroy():
    GPIO.output(ledPin, GPIO.LOW) # led off
    GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the subprogram destroy() will be executed.
        destroy()
