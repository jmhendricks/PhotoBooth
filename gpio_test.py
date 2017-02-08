#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import atexit

#Variables to change as needed
led1_pin = 15 # LED 1
led2_pin = 19 # LED 2
led3_pin = 21 # LED 3
led4_pin = 23 # LED 4
button1_pin = 22 # pin for the big red button
button2_pin = 18 # pin for button to shutdown the pi
button3_pin = 16 # pin for button to end the program, but not shutdown the pi

#GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1_pin,GPIO.OUT) # LED 1
GPIO.setup(led2_pin,GPIO.OUT) # LED 2
GPIO.setup(led3_pin,GPIO.OUT) # LED 3
GPIO.setup(led4_pin,GPIO.OUT) # LED 4
GPIO.setup(button1_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button 1
GPIO.setup(button2_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button 2
GPIO.setup(button3_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button 3
GPIO.output(led1_pin,True);
GPIO.output(led2_pin,True);
GPIO.output(led3_pin,True);
GPIO.output(led4_pin,True);
    
def cleanup():
  print('Goodbye.')
  GPIO.cleanup()
atexit.register(cleanup) 
	  
print('Push Buttons to start/stop')
print('Press Ctrl+C to exit')

while True:
	
	GPIO.wait_for_edge(button1_pin, GPIO.FALLING)
	print("Button 1 released")
      
