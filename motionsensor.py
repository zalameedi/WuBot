"""
WuBot can now turn on LED lights based on a distance sensor!
"""

import RPi.GPIO as GPIO
import time

class MotionSensor():
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        self.blue = 21
        self.red = 20
        self.green = 16
        GPIO.setmode(GPIO.BCM) # Set board
        GPIO.setup(self.blue, GPIO.OUT) # Activate blue + red + green pin
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)

        # Set distance sensors
        GPIO.setup(18, GPIO.IN)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)


    def green_light(self):
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.red, False)
        GPIO.output(self.blue, False)


    def blue_light(self):
        GPIO.output(self.blue, GPIO.HIGH)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.red, GPIO.LOW)


    def red_light(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)

    def light_test(self):
        self.red_light()
        time.sleep(3)
        self.blue_light()
        time.sleep(3)
        self.green_light()
        time.sleep(3)
        print("Light testing complete.")

    def get_distance(self):
        GPIO.output(4, True)
        time.sleep(0.00001)
        GPIO.output(4, False)
        while GPIO.input(18) == False:
            start = time.time()
        while GPIO.input(18) == True:
            end = time.time()
        sig_time = end-start
        distance = sig_time / 0.000058
        return distance


def main():
    ms = MotionSensor()
    ms.light_test()
    while True:
        distance = ms.get_distance()
        time.sleep(0.05)
        print(distance)
        if distance >= 30:
            ms.green_light()
        elif 30 > distance > 10:
            ms.blue_light()
        elif distance <= 10:
            ms.red_light()


if __name__ == '__main__':
    main()