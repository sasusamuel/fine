import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.output(11,True)
time.sleep(1)
GPIO.output(11, False)
time.sleep(1)
GPIO.output(11,True)
time.sleep(1)
GPIO.setwarnings(False)
GPIO.cleanup()
