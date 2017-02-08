#!/bin/bash
montage /home/pi/photobooth/pics/*.jpg -tile 2x2 -geometry +10+10 /home/pi/temp_montage2.jpg
print "made montage"
lp -d Canon_CP900 /home/pi/temp_montage2.jpg
print "Sent to printer"
suffix=$(date +%H%M%S)
cp /home/pi/temp_montage2.jpg /home/pi/PB_archive/PB_${suffix}.jpg
rm /home/pi/photobooth/pics/*.jpg
rm /home/pi/temp*
