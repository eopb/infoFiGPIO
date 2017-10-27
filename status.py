#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley
#services are dnsmasq, hostapd, apache2

print ("Importing libraries")

from gpiozero import LED
from gpiozero import Button
import time
import sys
import subprocess

ledPin = LED(17) # Pin for simple status LED
powerButtonPin = Button(27) # Pin for power switch for restart
statusButtonPin = Button(22) # Pin for showing the status of the server on the LED

start_time = time.time()

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

def checkForKeyWords(service):
    if "dnsmasq" not in service:
        return False
    if "hostapd" not in service:
        return False
    if "apache2" not in service:
        return False
    return True

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
    if checkForKeyWords(tmp) == False:
        return 2
    return 1

def moveLogs():
	pass
	#Code that moves logs.
	
	





clean()
while True:
    if powerButtonPin.is_pressed:
        ledPin.on()
        Poweroff()
    while statusButtonPin.is_pressed:
        status = checkStatus()
        if status == 4:
            # Flash and then no light.
            print("The status is 4")
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
            print("The status is 1")
            while statusButtonPin.is_pressed:
                ledPin.on()
            ledPin.off()
    if time.time() - start_time > 86400: #86400 is the number of seconds in 24hours.
		moveLogs()
