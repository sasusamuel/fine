import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
num_to_blick= int(input("Enter number of time to blick"))
for i in range (0,num_to_blick):
    GPIO.output(13, 1)
    time.sleep(0.1)
    GPIO.output(13, 0)
    time.sleep(0.1)
GPIO.cleanup()

