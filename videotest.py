#!/usr/bin/env python

import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.start_recording('full_res.h264', resize=(1024, 768))
    camera.wait_recording(10)
    camera.stop_recording()