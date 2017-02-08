#!/usr/bin/env python

import subprocess
import time

fps = 1 # delay between pics
total_pics = 4 # number of pics  to be taken
file_path = '/home/pi/photobooth/' #where do you want to save the photos

now = time.strftime("%Y%m%d%H%M%S") #get the current date and time for the start of the filename
file_name = file_path + now + '.jpg'
print file_name
subprocess.call(["raspistill","-f","-vf","-o",file_name,"-sa","-100","-w","500","-h","375"])
  
print "Done"
