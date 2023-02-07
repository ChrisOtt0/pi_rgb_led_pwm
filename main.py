import RPi.GPIO as gpio
import time
import math

a = 50
b = 1
c = 0
d = 50

def get_brightness(x):
    return a * math.sin(b * (math.degrees(x) - c)) + d
    
red = 6
green = 26

gpio.setmode(gpio.BCM)
gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)

pwm_red = gpio.PWM(red, 500)
pwm_green = gpio.PWM(green, 500)

x1 = 0
x2 = 180

pwm_red.start(get_brightness(x1))
pwm_green.start(get_brightness(x2))

while True:
    if x1 == 361:
        x1 = 0

    if x2 == 361:
        x2 = 0

    x1 += 0.1
    x2 += 0.1

    pwm_red.ChangeDutyCycle(get_brightness(x1))
    pwm_green.ChangeDutyCycle(get_brightness(x2))

    time.sleep(0.1)
