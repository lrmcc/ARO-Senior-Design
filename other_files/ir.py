mport RPi.GPIO as GPIO
from datetime import datetime

#Static program vars
pin = 11 #Input pin of sensor (GPIO.BOARD)

Buttons = [0x300ff6897L, 0x300ff30cfL, 0x300ff18e7L, 0x300ff7a85L, 0x300ff10efL, 0x300ff38c7L, 0x300ff5aa5L, 0x300ff42bdL, 0x300ff4ab5L, 0x300ff52adL, 0x300ff629dL, 0x300ffa857L, 0x300ffc23dL, 0x300ff22ddL, 0x300ff906fL, 0x300ffe01fL, 0x300ff9867L, 0x300ffb04fL, 0x300ffa25dL, 0x300ff02fdL]
ButtonsNames = ["0","1","2","3","4","5","6","7","8","9","VOL+","VOL-","right","left","up","down","EQ","ST/REPT","play-pause"]


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

def getBinary():
  num1s = 0
  binary = 1
  command = []
  previousValue = 0
  value = GPIO.input(pin)
  
  while value:
    value = GPIO.input(pin)
  
  startTime = datetime.now()

  while True:
    if previousValue != value:
      now = datetime.now()
      pulseTime = now - startTime
      startTime = now
      command.append((previousValue, pulseTime.microseconds))

    if value:
      num1s += 1
    else:
      num1s = 0

    if num1s > 10000:
      break

    previousValue = value
    value = GPIO.input(pin)
  
  for (typ, tme) in command:
    if typ == 1:
      if tme > 1000:
        binary = binary * 10 + 1
      else:
        binary *=10
  
  if len(str(binary)) > 34:
    binary = int(str(binary)[:34])

  return binary

def convertHex(binary





