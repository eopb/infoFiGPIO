#!/bin/sh
# Author : Ethan Brierley
# This script is to be started on start up with the correct cron setup.
# Navigate to home directory, then to the home directory, then make a logs folder, then execute python script, then back home.

cd /
cd home/pi
sudo mkdir logs
sh autolaunchlog.sh
sudo python status.py
cd /
