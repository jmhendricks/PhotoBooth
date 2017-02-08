#!/usr/bin/env python

import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg', format=None, use_video_port=False, resize=None, splitter_port=0)):
            print(filename)
            time.sleep(1)
            if i == 2:
                break
    finally:
        camera.stop_preview()