import subprocess
import sys
import time
from gpiozero import Button
from gpiozero import LED
+
#!/usr/bin/env python2
# Python script for controling status light and shutdown button on raspberry pi
# Author : Ethan Brierley
# services are dnsmasq, hostapd, apache2

print("Importing libraries")


ledPin = LED(14)  # Pin for simple status LED
powerButtonPin = Button(18)  # No longer needed.
# Pin for showing the status of the server on the LED
statusButtonPin = Button(22)

greenPin = LED(4)
bluePin = LED(27)
redPin = LED(17)

start_time = time.time()


def Poweroff():
    ledPin.on()
    time.sleep(1)
    print("Shutting down")
    command = "/usr/bin/sudo /sbin/reboot now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(str(output))
    print("end")


def clean():
    print("Cleaning Pins")
    ledPin.off()
    redPin.off()
    greenPin.off()


def checkForKeyWords(service):
    print(service)
    if "dnsmasq" not in service:
        print("dnsmasq not found")
        return False
    if "hostapd" not in service:
        print("hostapd not found")
        return False
    if "apache2" not in service:
        print("apache2 not found")
        if "systemd+apache22apache226apache2" not in service:
            print("systemd+apache22apache226apache2 not found")
            return False
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


clean()
numberOfRuns = 0
while True:
    numberOfRuns = numberOfRuns + 1
#    if powerButtonPin.is_pressed:
#        ledPin.on()
#        Poweroff()
    while statusButtonPin.is_pressed:
        pass
    if checkStatus() == 2:
        redPin.on()
        print("debug stuff")
    else:
        redPin.off()
        if numberOfRuns > 2:
            greenPin.on()
            time.sleep(1)
            greenPin.off()
            numberOfRuns = 0
    # 86400 is the number of seconds in 24hours.
    if time.time() - start_time > 86400:
        print("Script has been running for 24 hours")
        start_time = time.time()
        moveLogs()
    time.sleep(15)
