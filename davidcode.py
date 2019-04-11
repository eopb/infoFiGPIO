import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

start_time = time.time()

GPIO.output(4, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)

GPIO.output(4, 1)
time.sleep(2)
GPIO.output(4, 0)
GPIO.output(17, 1)
time.sleep(2)
GPIO.output(17, 0)
GPIO.output(27, 1)
time.sleep(2)
GPIO.output(27, 0)
time.sleep(2)
GPIO.output(4, 1)
GPIO.output(17, 1)
GPIO.output(27, 1)
time.sleep(2)

GPIO.cleanup()
