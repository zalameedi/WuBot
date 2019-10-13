import os
import picamera
import subprocess
import time
import RPi.GPIO as GP


class Pi:
    def __init__(self):
        GP.setmode(GP.BCM)
        self.GND = 18
        self.PWR = 4


    def pi_cam(self):
        cam = picamera.PiCamera()
        cam.vflip = True
        cam.start_preview()
        time.sleep(5)
        cam.stop_preview()
        exit()

    def flash_lights(self):
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

    def distance_sensor(self):
        GP.setmode(GP.BCM)
        TRIG = 4
        ECHO = 18
        while True:
            GP.setup(TRIG, GP.OUT)
            GP.setup(ECHO, GP.IN)
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


    def light_motion_sensor(self):
        while True:
            GP.setup(self.PWR, GP.OUT) # Power pin set
            GP.setup(self.GND, GP.IN) # Ground pin set
            GP.output(self.PWR, True) # Pin is turned on
            time.sleep(0.0001) # System waits for 1 ms
            GP.output(self.PWR, False) # Turned pin off
            try:
                while GP.input(self.PWR) == False:
                    start = time.time()
                while GP.input(self.PWR) == True:
                    end = time.time()
                sig_time = end-start
                distance = sig_time / 0.000058
                print("Distance: {0} cm".format(distance))
                # PUT CONDITIONS here
            except:
                GP.cleanup() 




def main():
    test_pi = Pi()
    test_pi.distance_sensor()


if __name__ == '__main__':
    main()
