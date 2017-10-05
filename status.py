#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley

from gpiozero import LED
from gpiozero import Button
import time
import sys
import subprocess

ledPin = LED(17) # Pin for simple status LED
powerButtonPin = Button(27) # Pin for power switch for restart
statusButtonPin = Button(22) # Pin for showing the status of the server on the LED

def Poweroff():
    ledPin.on()
    time.sleep(1)
    print ("Shutting down")
    command = "/usr/bin/sudo /sbin/reboot now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print (str(output))
    print ("end")

def clean():
    print ("Cleaning Pins")
    ledPin.off()

def checkStatus():
    proc = subprocess.Popen('pstree', stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    tmp = tmp.replace("|", "")
    tmp = tmp.replace("-", "")
    tmp = tmp.replace("{", "")
    tmp = tmp.replace("}", "")
    tmp = tmp.replace("[", "")
    tmp = tmp.replace("]", "")
    tmp = tmp.replace(" ", "")
    tmp = tmp.replace("`", "")
    tmp = tmp.replace("*", "")
    tmp = tmp.replace("(", "")
    tmp = tmp.replace(")", "")
    tmp = tmp.replace("|", "")
    tmp = tmp.split("\n")
    for service in tmp:
        if service == "gmain":
            status = 2
            return status
        else pass
            
        



clean()
while True:
    if powerButtonPin.is_pressed:
        ledPin.on()
        Poweroff()
    while statusButtonPin.is_pressed:
        status = checkStatus()
        if status == 1:
            # Flash and then no light.
            print("The status is 1")
            ledPin.on()
            time.sleep(0.2)
            while statusButtonPin.is_pressed:
                ledPin.off()
            ledPin.off()
        if status == 2:
            # Flashing
            print("The status is 2")
            while statusButtonPin.is_pressed:
                ledPin.on()
                time.sleep(0.3)
                ledPin.off()
                time.sleep(0.3)
        if status == 3:
            # Dot Dash Dot Dash Dot
            print("The status is 3")
            while statusButtonPin.is_pressed:
                ledPin.on()
                time.sleep(0.3)
                ledPin.off()
                time.sleep(0.3)
                ledPin.on()
                time.sleep(0.9)
                ledPin.off()
                time.sleep(0.3)
        if status == 1:
            # solid light.
            print("The status is 4")
            while statusButtonPin.is_pressed:
                ledPin.on()
            ledPin.off()
    #Finding the status goes here!
            
        
    
