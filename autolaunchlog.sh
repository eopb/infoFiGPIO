#!/bin/sh
# Author : Ethan Brierley
sudo rm -f /home/pi/logs/cronlog5
sudo mv /home/pi/logs/cronlog4  /home/pi/logs/cronlog5
sudo mv /home/pi/logs/cronlog3  /home/pi/logs/cronlog4
sudo mv /home/pi/logs/cronlog2  /home/pi/logs/cronlog3
sudo mv /home/pi/logs/cronlog  /home/pi/logs/cronlog2
sudo rm -f /home/pi/logs/cronlog

