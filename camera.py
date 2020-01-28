#!/usr/bin/python

# Import libraries
from picamera import PiCamera
from time import sleep

# Define the object
camera = PiCamera()

# Turn on the camera preview, sleep 10 seconds, then turn off the camera
camera.start_preview()
sleep(10)
camera.stop_preview()

