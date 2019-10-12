import os
import picamera
import subprocess
import time
import RPi.GPIO as GP

<<<<<<< HEAD
def cam_on():
=======

def main():
>>>>>>> 81e11263c30c05aab32f2a34413ced7419706236
    cam = picamera.PiCamera()
    cam.vflip = True
    cam.start_preview()
    time.sleep(5)
    cam.stop_preview()
    exit()

def flash_lights():
    GP.setmode(GP.BCM)
    GP.setup(18, GP.OUT)
    try:
        while True:
            GP.output(18, GP.HIGH)
            time.sleep(1)
            GP.output(18, GP.LOW)
            time.sleep(1)
    except:
        GP.cleanup()

<<<<<<< HEAD
def distance_sensor():
    GP.setmode(GP.BCM)
    TRIG = 4
    ECHO = 18
    while True:
        GP.setup(TRIG, GP.OUT)
        GP.setup(ECHO,GP.IN)
        GP.output(TRIG, True)
        time.sleep(0.00001)
        GP.output(TRIG, False)
        try:
            while GP.input(ECHO) == False:
                start = time.time()
            while GP.input(ECHO) == True:
                end = time.time()
            sig_time = end-start
            distance = sig_time / 0.000058
            print('Distance: {} centimeters'.format(distance))
        except:
            GP.cleanup()


def main():
    distance_sensor()


=======
>>>>>>> 81e11263c30c05aab32f2a34413ced7419706236
if __name__ == '__main__':
    main()
