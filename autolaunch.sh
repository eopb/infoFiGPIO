#!/bin/sh
# This script is for 
# Navigate to home directory, then to the home directory, then make a logs folder, then execute python script, then back home.

cd /
cd home/pi
sudo mkdir logs
sudo python status.py
cd /
