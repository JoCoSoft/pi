# import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BOARD)
control_pins = [7, 11, 13, 15]
# for pin in control_pins:
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, 0)
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


def openVent(degree=180):
    print "Opening " + str(degree) + " degrees"
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                continue
                #GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)


def closeVent(degree=180):
    print "Closing " + str(degree) + " degrees"
    for i in range(512):
        for halfstep in range(8):
            for pin in reversed(range(4)):
                continue
                #GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
