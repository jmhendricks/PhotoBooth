#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD) 

printername = "printer1"	

button1_pin = 22 #big red button
button2_pin = 16 #exit python
button3_pin = 18 #shutdown button 
led1_pin = 15 # LED 1
led2_pin = 19 # LED 2
led3_pin = 21 # LED 3
led4_pin = 23 # LED 4
led5_pin = 11 # LED 5

GPIO.setup(led1_pin,GPIO.OUT) # LED 1
GPIO.setup(led2_pin,GPIO.OUT) # LED 2
GPIO.setup(led3_pin,GPIO.OUT) # LED 3
GPIO.setup(led4_pin,GPIO.OUT) # LED 4
GPIO.setup(led5_pin,GPIO.OUT) # LED 5

GPIO.output(led1_pin,True); #turn off the lights
GPIO.output(led2_pin,True);
GPIO.output(led3_pin,True);
GPIO.output(led4_pin,True);
GPIO.output(led5_pin,True);

def whichprinter(): # return Fibonacci series up to n
	global printername    # Needed to modify global copy of globvar
	"Return a list containing the Fibonacci series up to n."
	if printername == "printer1":
		#os.system('lp -d Canon_CP900 /home/pi/temp_montage2.jpg')
		printername = "printer2"
		return "Canon_CP900"
	else: 
		printername = "printer1"
		#os.system('lp -d Canon_CP760 /home/pi/temp_montage2.jpg')
		return "Canon_CP760"

  
# button1_pin & button2_pin set up as inputs, pulled up to avoid false detection.  
# Both ports are wired to connect to GND on button press.  
# So we'll be setting up falling edge detection for both  
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #big red button


GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# button3_pin set up as an input, pulled down, connected to 3V3 on button press  
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
	print "falling edge detected on button1_pin--Big Red Button" +whichprinter()+" fasdfasdf"  
  
def my_callback2(channel):  
    print "falling edge detected on button2_pin"  
   
def my_callback3(channel):  
    print "falling edge detected on button2_pin"    
  
print "Make sure you have a button connected so that when pressed"  
print "it will connect " + str(button1_pin) + " to GND\n"   
print "You will also need a second button connected so that when pressed"  
print "it will connect " + str(button2_pin) + " to GND"  
print "You will also need a third button connected so that when pressed"  
print "it will connect " + str(button3_pin) + " to 3V3 (pin 1)\n" 
raw_input("Press Enter when ready\n>")  
  
# when a falling edge is detected on button1_pin, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=my_callback, bouncetime=300)  
  
# when a falling edge is detected on button2_pin, regardless of whatever   
# else is happening in the program, the function my_callback2 will be run  
# 'bouncetime=300' includes the bounce control written into interrupts2a.py  
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=my_callback2, bouncetime=300)  

whichprinter()
  
try:  
    print "Waiting for rising edge on button3_pin"  
    GPIO.wait_for_edge(button3_pin, GPIO.RISING)  
    print "Rising edge detected on " + str(button3_pin) + ". Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit


