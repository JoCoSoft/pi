import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
control_pins = [7, 11, 13, 15]

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


def rotateMotor(clockwise, degrees=360):
    halfstepRange = range(8) if clockwise else reversed(range(8))
    pinRange = range(4) if clockwise else reversed(range(4))

    for _ in range(512):
        for halfstep in halfstepRange:
            for pin in pinRange:
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)


def openVent(degrees=360):
    print "Opening " + str(degrees) + " degrees"
    rotateMotor(False, degrees)


def closeVent(degrees=360):
    print "Closing " + str(degrees) + " degrees"
    rotateMotor(True, degrees)
