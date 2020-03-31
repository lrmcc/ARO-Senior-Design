import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep # import function sleep for delay

# -------------
# Stepper Setup
# -------------
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 60  # Steps per Revolution (360 / 7.5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
step_count = SPR
delay = .050
# -----------------
# Stepper Setup end
# -----------------

# -----------
# Latch Setup 
# -----------
GPIO.setmode(GPIO.BCM) # GPIO numbering
GPIO.setwarnings(False) # enable warning from GPIO
lAN2 = 12 # set pwm2 pin on MDDS10 to GPIO 12 - blue
lAN1 = 13 # set pwm1 pin on MDDS10 to GPIO 13 - grey
lDIG2 = 25 # set dir2 pin on MDDS10 to GPIO 25 - purple
lDIG1 = 26 # set dir1 pin on MDDS10 to GPIO 26

GPIO.setup(lAN2, GPIO.OUT)
GPIO.setup(lAN1, GPIO.OUT) 
GPIO.setup(lDIG2, GPIO.OUT) 
GPIO.setup(lDIG1, GPIO.OUT) 
sleep(1) # delay for 1 seconds
lp1 = GPIO.PWM(lAN1, 100) 
lp2 = GPIO.PWM(lAN2, 100) 
# ---------------
# Latch Setup end
# ---------------


# ---------------------
# Linear Actuator Setup 
# ---------------------
AN2 = 17 # set pwm2 pin on MDDS10 to GPIO 17
AN1 = 18 # set pwm1 pin on MDDS10 to GPIO 18
DIG2 = 22 # set dir2 pin on MDDS10 to GPIO 22
DIG1 = 23 # set dir1 pin on MDDS10 to GPIO 23
GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(AN1, GPIO.OUT) 
GPIO.setup(DIG2, GPIO.OUT) 
GPIO.setup(DIG1, GPIO.OUT) 
sleep(1) # delay for 1 seconds
p1 = GPIO.PWM(AN1, 100) #side
p2 = GPIO.PWM(AN2, 100) #lower
# -------------------------
# Linear Actuator Setup end
# -------------------------

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


# -------------
# LATCH UNLOCK 
# -------------
print("Unlock")
GPIO.output(lDIG1, GPIO.HIGH) 
GPIO.output(lDIG2, GPIO.HIGH)
lp1.start(50)
sleep(0.05)
lp2.start(50)
sleep(1)

# -------------------
# Linear Actuator out
# -------------------

print("Deploying Armour")
GPIO.output(DIG1, GPIO.HIGH) 
GPIO.output(DIG2, GPIO.LOW)

p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
# maybe about here we should deenergize the latch.
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
# -------------
# LATCH DEENERGIZE 
# -------------
print("Lock")
GPIO.output(lDIG1, GPIO.LOW) 
GPIO.output(lDIG2, GPIO.LOW)
lp1.start(0)
sleep(0.05)
lp2.start(0)
sleep(1)
# --------------------
# LATCH DEENERGIZE end
# --------------------

p2.start(50)
sleep(1)
p2.start(50)
sleep(1)
p2.start(50)
sleep(1)
p2.start(50)
sleep(1) 

p1.start(0) # set speed M1=0
p2.start(0) # set speed M2=0
print("exit")
# -------------------
# Linear Actuator end
# -------------------

print("Signal to return happens here")
sleep(1)


# -------------------
# Linear Actuator in
# -------------------
print("Stowing Armour")
GPIO.output(DIG1, GPIO.LOW) 
GPIO.output(DIG2, GPIO.HIGH)

p2.start(50)
sleep(1)
p2.start(50)
sleep(1)
p2.start(50)
sleep(1)
p2.start(50)
sleep(1) 
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)
p1.start(50)
sleep(1)


p1.start(0) # set speed M1=0
p2.start(0) # set speed M2=0
print("exit")
# -------------------
# Linear Actuator end
# -------------------

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

