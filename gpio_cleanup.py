#!/usr/bin/env python

import RPi.GPIO as GPIO

button1_pin = 22 # pin for the big red button
button2_pin = 18 # shutdown button 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(button1_pin, GPIO.IN) 
GPIO.setup(button2_pin, GPIO.IN) 

GPIO.cleanup()