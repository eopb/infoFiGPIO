import subprocess
import sys
import time
import RPi.GPIO as GPIO
import re

#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley
# services are dnsmasq, hostapd, apache2

print("Importing libraries")


powerButtonPin = None  # No longer needed.
# Pin for showing the status of the server on the LED
statusButtonPin = None

start_time = time.time()

GPIO.setmode(GPIO.BCM)


def setup_pin(num):
    GPIO.setup(num, GPIO.OUT)
    GPIO.output(num, 0)


setup_pin(4)
setup_pin(17)
setup_pin(27)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)


def light(num, status):
    if status:
        GPIO.output(num, 1)
    else:
        GPIO.output(num, 0)


def red(status):
    light(4, status)


def green(status):
    light(17, status)


def blue(status):
    light(27, status)


def power_off():
    clean()
    blue(True)
    time.sleep(1)
    print("Shutting down")
    command = "/usr/bin/sudo /sbin/poweroff"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(str(output))
    print("end")


def clean():
    print("Cleaning Pins")
    red(False)
    green(False)
    blue(False)


def checkForKeyWords(service):
    r = re.compile('.*apache2.*')
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
    if not any(re.match(r, serv) for serv in service):
        print("apache2 not found")
        return False
    return True


def check_status():
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


def move_logs():
    print("Reorganizing logs and removing old logs. ")
    pass
    # Code that moves logs.


while True:
    print(GPIO.input(23) != GPIO.HIGH)
    if GPIO.input(23) != GPIO.HIGH:
        power_off()
    if check_status() == 2:
        clean()
        for i in range(1, 100):
            red(True)
            time.sleep(0.1)
            red(False)
            time.sleep(0.1)
        print("debug stuff")
    else:
        clean()
        green(True)
        time.sleep(0.5)
        clean()
    # 86400 is the number of seconds in 24hours.
    if time.time() - start_time > 86400:
        print("Script has been running for 24 hours")
        start_time = time.time()
        move_logs()
    clean()
    time.sleep(10)


GPIO.cleanup()
