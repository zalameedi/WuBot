import os
import picamera
import subprocess
import time


def main():

    cam = picamera.PiCamera()
    cam.vflip=True
    cam.start_preview()
    time.sleep(5)
    cam.stop_preview()
    exit()




if __name__ == '__main__':
    main()