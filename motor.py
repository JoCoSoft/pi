import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


control_pins = [
    7,      # GPIO 04 (Pin 7)
    11,     # GPIO 17 (Pin 11)
    13,     # GPIO 27 (Pin 13)
    15      # GPIO 22 (Pin 15)
]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfstep_seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


def rotateMotor(clockwise, degrees):
    fullRotationSteps = 512
    fullRotationDegrees = 360
    halfstepExecutions = int(fullRotationSteps *
                             (float(degrees) / float(fullRotationDegrees)))

    print "Looping for " + str(halfstepExecutions) + " half step executions"

    for _ in range(halfstepExecutions):
        for halfstep in range(8) if clockwise else reversed(range(8)):
            for pin in range(4) if clockwise else reversed(range(4)):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0008)


def openVent(degrees):
    print "Rotating " + str(degrees) + " degrees counter-clockwise"
    rotateMotor(False, degrees)


def closeVent(degrees):
    print "Rotating " + str(degrees) + " degrees clockwise"
    rotateMotor(True, degrees)
