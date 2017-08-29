#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley

from gpiozero import LED
from gpiozero import Button
from time import sleep
import sys
import subprocess

ledPin = LED(1) # Pin for simple status LED
powerButtonPin = Button(2) # Pin for power switch for restart
statusButtonPin = Button(3) # Pin for showing the status of the server on the LED

def Poweroff():
    wiringpi.softPwmWrite(pinOn,0)
    Clean()
    time.sleep(1)
    command = "/usr/bin/sudo /sbin/reboot now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print (str(output))
    print ("end")

while True:
    if powerButtonPin.is_pressed:
        ledPin.on()
        time.sleep(0.5)
        ledPin.off()
        Poweroff()
        
    
