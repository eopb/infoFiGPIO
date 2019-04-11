import subprocess
import sys
import time
import RPi.GPIO as GPIO

#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley
# services are dnsmasq, hostapd, apache2

print("Importing libraries")


powerButtonPin = None  # No longer needed.
# Pin for showing the status of the server on the LED
statusButtonPin = None


GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(4, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)
start_time = time.time()


def Poweroff():
    time.sleep(1)
    print("Shutting down")
    command = "/usr/bin/sudo /sbin/reboot now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(str(output))
    print("end")


def clean():
    print("Cleaning Pins")
    GPIO.cleanup()


def checkForKeyWords(service):
    print(service)
    if "dnsmasq" not in service:
        print("dnsmasq not found")
        return False
    if "hostapd" not in service:
        print("hostapd not found")
        return False
    if "wpa_supplicant" not in service:
        print("wpa_supplicant not found")
        return False
    if "apache2" not in service:
        print("apache2 not found")
        if "systemd+apache22apache226apache2" not in service:
            print("systemd+apache22apache226apache2 not found")
            if "apache25apache2" not in service:
                print("apache25apache2 not found")
                return False
            return True
        return True
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
    print("Reorganizing logs and removing old logs. ")
    pass
    # Code that moves logs.

000
numberOfRuns = 0
while True:
    numberOfRuns = numberOfRuns + 1
#    if powerButtonPin.is_pressed:
#        ledPin.on()
#        Poweroff()
    if checkStatus() == 2:
        GPIO.output(27, 1)
        print("debug stuff")
    else:
        clean()
        if numberOfRuns > 2:
            GPIO.output(4, 1)
            time.sleep(1)
            clean()
            numberOfRuns = 0
    # 86400 is the number of seconds in 24hours.
    if time.time() - start_time > 86400:
        print("Script has been running for 24 hours")
        start_time = time.time()
        moveLogs()
    GPIO.output(17, 1)
    time.sleep(15)


GPIO.cleanup()
