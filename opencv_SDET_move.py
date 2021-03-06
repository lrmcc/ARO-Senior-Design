import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep 

import numpy as np
import cv2
import time

# -------------
# Stepper Setup
# -------------
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 2  # Steps per Revolution (360 / 7.5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
step_count = SPR
delay = .050
# -----------------
# Stepper Setup end
# -----------------

frame_rate = 20
prev = 0

center = (240,320)
center_bottom = (240,450)

cap = cv2.VideoCapture(0)


#fourcc https://www.fourcc.org/
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frames_per_second = 30.0
size = (640,480)
out = cv2.VideoWriter('ouputTest.avi', fourcc, frames_per_second, size)

font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 0.7
red_color = (0, 0, 255) 
thickness = 2

#deploy = False
distance = 0
#false will be left(CCW), True will be right(CW)
direction = False 

def moveSDET(direction):
    GPIO.output(DIR, direction)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

def drawImageLines(frame):
    frame = cv2.arrowedLine(frame, (0,240),(320,240),(240,86,10),3)
    frame = cv2.arrowedLine(frame, (320,480),(320,240),(240,86,10),3)
    frame = cv2.arrowedLine(frame, (640,240),(320,240),(240,86,10),3)
    frame = cv2.arrowedLine(frame, (320,0),(320,240),(240,86,10),3)
    frame = cv2.rectangle(frame, (310,230),(330,250),(10,20,255),3)
    frame = cv2.circle(frame,(320,240), 35,(63,240,10),2)
    return frame

def checkColor(i,j):
    target = False
    curr = frame[i][j] 
    b,g,r = curr
    if (20 < b < 60):
        if (25 < g < 65):
            if (141 < r < 191):
                return True
    return False

def targetText(i,j,frame):
    org = (i, j) 
    frame = cv2.putText(frame, 'Target Aquired', org, font, fontScale, red_color, thickness, cv2.LINE_AA) 
    return frame

def processImage(frame):
    target_aquired_x = []
    target_aquired_y = []
        
    for i in range(20, len(frame)-20,10):
        y=i
        for j in range(20, len(frame[0])-20,10):
            x=j
            if (checkColor(i,j)):
                target_aquired_x.append(x)
                target_aquired_y.append(i)
            
    if (len(target_aquired_x) > 5):
        print("TARGET AQUIRED")

        # Collecting useful points
        target_min_x = min(target_aquired_x)
        target_max_x = max(target_aquired_x)
        target_x_delta = target_max_x - target_min_x
        target_min_y = min(target_aquired_y)
        target_max_y = max(target_aquired_y)
        target_y_delta = target_max_y - target_min_y
        target_center  = ((target_min_x + int(target_x_delta/2)), (target_min_y) + int(target_y_delta/2))
        
        # draw circle at center and label target
        frame = cv2.circle(frame,target_center, 30,red_color,2)
        frame = targetText(target_min_x -20 ,target_max_y + 10,frame)
        print("target_center[0]: ", target_center[0])
        print("center[0]: ", center[0])

        if (target_center[0] < center[0]-15):
            frame = cv2.putText(frame, 'Target Left', center_bottom, font, fontScale, red_color, thickness, cv2.LINE_AA)
            direction = False
            moveSDET(direction)
        elif (target_center[0] > center[0]+15):  
            frame = cv2.putText(frame, 'Target Right', center_bottom, font, fontScale, red_color, thickness, cv2.LINE_AA)
            direction = True
            moveSDET(direction)
        elif (target_center[0] > center[0]-15):
            if(target_center[0] < center[0]+15):
	        #deploy = True
                frame = cv2.putText(frame, 'Target Lock', center_bottom, font, fontScale, red_color, thickness, cv2.LINE_AA)

    print("len(target_aquired): ", len(target_aquired_x))
    #if (deploy):
     #   print("DEPLOY ARMOUR")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.imread('sticknote.png')

    frame = drawImageLines(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time_elapsed = time.time() - prev
    if time_elapsed > 1./frame_rate:
        prev = time.time()
        processImage(frame)
  
    # Display the resulting frame
    cv2.imshow('frame',frame)
    out.write(frame)

# When everything done, release the capture
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
