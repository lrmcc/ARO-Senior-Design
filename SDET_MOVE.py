import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep 

# -------------
# Stepper Setup
# -------------
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 120  # Steps per Revolution (360 / 7.5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
step_count = SPR
delay = .050
# -----------------
# Stepper Setup end
# -----------------

print("SDET Sequence Initiated")

# --------------------
# Stepper Go To Target
# -------------------
GPIO.output(DIR, CW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
# -----------
# Stepper end
# -----------


# --------------------
# Stepper Go To Target
# -------------------
sleep(.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
# -----------
# Stepper end
# -----------

GPIO.cleanup()

