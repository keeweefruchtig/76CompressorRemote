# Imports Servo und Schrittmotor Treiber
from __future__ import division
import time

import RPi.GPIO as GPIO
# Import the PCA9685 module.
import Adafruit_PCA9685



# Initialisierung Servo Treiber
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 380  # Min pulse length out of 4096
servo_max = 500  # Max pulse length out of 4096
servo_half = 440  # Halbstellung


# Helper function to make setting a servo pulse width simpler.


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000  # 1,000,000 us per second
    pulse_length //= 60  # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096  # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Initialisierung Schrittmotoren

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# INPUT
A = 40
B = 38
C = 36
D = 32

# OUTPUT
E = 37
F = 35
G = 33
H = 31

# ATTACK
I = 22
J = 18
K = 16
L = 12

# RELEASE
M = 15
N = 13
O = 11
P = 7

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)

GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)

GPIO.setup(I, GPIO.OUT)
GPIO.setup(J, GPIO.OUT)
GPIO.setup(K, GPIO.OUT)
GPIO.setup(L, GPIO.OUT)

GPIO.setup(M, GPIO.OUT)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(O, GPIO.OUT)
GPIO.setup(P, GPIO.OUT)


def GPIO_SETUP1(a, b, c, d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.002)


def GPIO_SETUP2(e, f, g, h):
    GPIO.output(E, e)
    GPIO.output(F, f)
    GPIO.output(G, g)
    GPIO.output(H, h)
    time.sleep(0.002)


def GPIO_SETUP3(i, j, k, l):
    GPIO.output(I, i)
    GPIO.output(J, j)
    GPIO.output(K, k)
    GPIO.output(L, l)
    time.sleep(0.002)


def GPIO_SETUP4(m, n, o, p):
    GPIO.output(M, m)
    GPIO.output(N, n)
    GPIO.output(O, o)
    GPIO.output(P, p)
    time.sleep(0.002)


# MOVEMENTS

def RIGHT_TURN1(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP1(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP1(1, 0, 0, 0)
        GPIO_SETUP1(1, 1, 0, 0)
        GPIO_SETUP1(0, 1, 0, 0)
        GPIO_SETUP1(0, 1, 1, 0)
        GPIO_SETUP1(0, 0, 1, 0)
        GPIO_SETUP1(0, 0, 1, 1)
        GPIO_SETUP1(0, 0, 0, 1)
        GPIO_SETUP1(1, 0, 0, 1)
        degree -= 1


def LEFT_TURN1(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP1(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP1(1, 0, 0, 1)
        GPIO_SETUP1(0, 0, 0, 1)
        GPIO_SETUP1(0, 0, 1, 1)
        GPIO_SETUP1(0, 0, 1, 0)
        GPIO_SETUP1(0, 1, 1, 0)
        GPIO_SETUP1(0, 1, 0, 0)
        GPIO_SETUP1(1, 1, 0, 0)
        GPIO_SETUP1(1, 0, 0, 0)
        degree -= 1


def RIGHT_TURN2(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP2(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP2(1, 0, 0, 0)
        GPIO_SETUP2(1, 1, 0, 0)
        GPIO_SETUP2(0, 1, 0, 0)
        GPIO_SETUP2(0, 1, 1, 0)
        GPIO_SETUP2(0, 0, 1, 0)
        GPIO_SETUP2(0, 0, 1, 1)
        GPIO_SETUP2(0, 0, 0, 1)
        GPIO_SETUP2(1, 0, 0, 1)
        degree -= 1


def LEFT_TURN2(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP2(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP2(1, 0, 0, 1)
        GPIO_SETUP2(0, 0, 0, 1)
        GPIO_SETUP2(0, 0, 1, 1)
        GPIO_SETUP2(0, 0, 1, 0)
        GPIO_SETUP2(0, 1, 1, 0)
        GPIO_SETUP2(0, 1, 0, 0)
        GPIO_SETUP2(1, 1, 0, 0)
        GPIO_SETUP2(1, 0, 0, 0)
        degree -= 1


def RIGHT_TURN3(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP3(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP3(1, 0, 0, 0)
        GPIO_SETUP3(1, 1, 0, 0)
        GPIO_SETUP3(0, 1, 0, 0)
        GPIO_SETUP3(0, 1, 1, 0)
        GPIO_SETUP3(0, 0, 1, 0)
        GPIO_SETUP3(0, 0, 1, 1)
        GPIO_SETUP3(0, 0, 0, 1)
        GPIO_SETUP3(1, 0, 0, 1)
        degree -= 1


def LEFT_TURN3(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP3(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP3(1, 0, 0, 1)
        GPIO_SETUP3(0, 0, 0, 1)
        GPIO_SETUP3(0, 0, 1, 1)
        GPIO_SETUP3(0, 0, 1, 0)
        GPIO_SETUP3(0, 1, 1, 0)
        GPIO_SETUP3(0, 1, 0, 0)
        GPIO_SETUP3(1, 1, 0, 0)
        GPIO_SETUP3(1, 0, 0, 0)
        degree -= 1


def RIGHT_TURN4(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP4(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP4(1, 0, 0, 0)
        GPIO_SETUP4(1, 1, 0, 0)
        GPIO_SETUP4(0, 1, 0, 0)
        GPIO_SETUP4(0, 1, 1, 0)
        GPIO_SETUP4(0, 0, 1, 0)
        GPIO_SETUP4(0, 0, 1, 1)
        GPIO_SETUP4(0, 0, 0, 1)
        GPIO_SETUP4(1, 0, 0, 1)
        degree -= 1


def LEFT_TURN4(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP4(0, 0, 0, 0)

    while degree > 0.0:
        GPIO_SETUP4(1, 0, 0, 1)
        GPIO_SETUP4(0, 0, 0, 1)
        GPIO_SETUP4(0, 0, 1, 1)
        GPIO_SETUP4(0, 0, 1, 0)
        GPIO_SETUP4(0, 1, 1, 0)
        GPIO_SETUP4(0, 1, 0, 0)
        GPIO_SETUP4(1, 1, 0, 0)
        GPIO_SETUP4(1, 0, 0, 0)
        degree -= 1


# MAIN

print('Moving everything, press Ctrl-C to quit...')
while True:
    # Move Steppers.
    GPIO_SETUP1(0, 0, 0, 0)
    GPIO_SETUP2(0, 0, 0, 0)
    GPIO_SETUP3(0, 0, 0, 0)
    GPIO_SETUP4(0, 0, 0, 0)

    RIGHT_TURN1(60)
    GPIO_SETUP1(0, 0, 0, 0)
    LEFT_TURN1(120)
    GPIO_SETUP1(0, 0, 0, 0)
    RIGHT_TURN1(60)
    GPIO_SETUP1(0, 0, 0, 0)
    time.sleep(1)

    RIGHT_TURN2(60)
    GPIO_SETUP2(0, 0, 0, 0)
    LEFT_TURN2(120)
    GPIO_SETUP2(0, 0, 0, 0)
    RIGHT_TURN2(60)
    GPIO_SETUP2(0, 0, 0, 0)
    time.sleep(1)

    RIGHT_TURN3(60)
    GPIO_SETUP3(0, 0, 0, 0)
    LEFT_TURN3(120)
    GPIO_SETUP3(0, 0, 0, 0)
    RIGHT_TURN3(60)
    GPIO_SETUP3(0, 0, 0, 0)
    time.sleep(1)

    RIGHT_TURN4(60)
    GPIO_SETUP4(0, 0, 0, 0)
    LEFT_TURN4(120)
    GPIO_SETUP4(0, 0, 0, 0)
    RIGHT_TURN4(60)
    GPIO_SETUP4(0, 0, 0, 0)
    time.sleep(1)

    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(1, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(1, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(2, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(2, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(3, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(3, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(4, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(4, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(5, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(5, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(6, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(6, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(7, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(7, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(8, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(8, 0, servo_max)
    time.sleep(1)
