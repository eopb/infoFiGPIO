# infoFiGPIO
GPIO python script for InfoFi.

Author : Ethan Brierley

# What it does.

This python script checks for sevices and shows a status on a single LED. It also powers off the Raspberry Pi in the event a button is presssed.


# How it works.

The script runs the bash command pstree that output the sevices that are running. The script then checks for the services apache2, hostapd and dnsmasq.


# What are the status.

status 1 = Everything is working = Light stays on while button is pressed.

status 2 = Some stuff are working but one or more of the services have crashed. = Light flashes on and off.

status 3 = Nothing set. = Flashes in a morse code rhythm of dot dash dot dash dot dash.

status 4 = Nothing set. = Turns of for a short amount of time then stays off.

# Other info.

Layout = GPIOzero

Python version = 2
