Senior Design SDET programs readme by Luke McConnell 5.4.2020
-----------------------------------------------------------------------------
There are 3 main programs to be used for testing:

1. SDET_MOVE.py
This program is a demo of stepper motor rotation.

2. SDET_RUN.py
This program is a demo of stepper motor and deployment and stowage

3. SDET_FINAL.py (AKA final_main.py on github) 
This program is a demo of Computer Vision control for movement and deployment.
It is designed to be run on the SDET 2019/2020 Sr. Design Raspberry Pi.
The program will lauch and will react to red targets within the webcam's field-of-view
-----------------------------------------------------------------------------
In order to launch a python program:

1. Open a terminal
 (can click on the terminal icon on the left side in the top menu bar)

2. Navigate to the directory (AKA folder) that contains the file.
Navigate by using 'cd' command
Check present working directory by using 'pwd' command
Check directory contents by using 'ls' command

3. Launch program with the command: python file_name.py
Where 'file_name.py' is replaced with the desired file

------------------------------------------------------------------------------
EXAMPLE:

pi@raspberrypi:~ $ pwd
/home/pi
pi@raspberrypi:~ $ ls
 2020-01-25-193516_1920x1080_scrot.png   opencv-4.2.0
 bcm2835-1.62                            Pictures
 Desktop                                 Public
 Documents                               Scratch
 Downloads                              'SDET testing'
 helpful_resources.txt                   SDET_work
 MagPi                                   startup_aro.service
 Music                                   Templates
 myservice.service                       test_service.sh
 opencv-4.1.0                            Videos
pi@raspberrypi:~ $ cd Desktop/
pi@raspberrypi:~/Desktop $ ls
github         output_videos  remote         SDET_MOVE.py
ir_control.py  README.md      SDET_FINAL.py  SDET_RUN.py
pi@raspberrypi:~/Desktop $ python SDET_MOVE.py 



