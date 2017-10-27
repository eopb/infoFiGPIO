# InfoFiGPIO

GPIO Python 2 script for the [TechResort](http://techresorteb.com/) Info-Fi project.

*Script written by Ethan Brierley*

*Extra contributions by David Bi (hardware) and Sean Firth (documentation edits)*

## What it does

This Python 2 script checks to see if services are running and shows a status on a single LED to the end user, to check if there is a problem. It also features the option to power off the Raspberry Pi if a button, connected to the GPIO pins on the Pi, is pressed.

This script is designed to be as easy as possible for a fault to be diagnosed (eg, the required services are not running) and then safely shuts down or reboots the Pi if necessary. 

## How it works

The script runs the bash command `pstree` that outputs all of the sevices that are running on the Pi. The script then checks for the services `apache2`, `hostapd` and `dnsmasq`.

## Status codes

status 1 = Everything is working = Light stays on while button is pressed.

status 2 = Crashed services = The Pi is running but one or more of the services have crashed, the light flashes on and off.

status 3 = Nothing set = Flashes in a morse code rhythm of **dot** *dash* **dot** *dash* **dot** *dash*.

status 4 = Nothing set = Flashes for a short amount of time then stays off.

The inclusion of status codes 3 and 4 allow for simple expansion should we need to in the future.

## Python/GPIO information

Required Python libraries:

* [gpiozero](https://gpiozero.readthedocs.io/en/stable/)

* [time](https://docs.python.org/2.7/library/time.html)

* [sys](https://docs.python.org/2/library/sys.html)

* [subprocess](https://docs.python.org/2/library/subprocess.html)

All of these are imported at the top of the *status.py* file, and come as standard on the latest [Raspbian Download](https://www.raspberrypi.org/downloads/).

Python 2.x.x is used for this project.

The GPIO naming scheme used is the Broadcom (BCM) pin numbering layout. A chart converting board (physcial) pin numbers to their BCM names can be found [here](https://i.imgur.com/TCTy4v9.png).



