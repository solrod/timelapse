from picamera import PiCamera
from os import system
from time import sleep

# Variables
previewTime = 10 # Preview to adjust camera in seconds
numberPics = 10 # Number of pictures to be taken during timelapse.
sleepTime = 3 # Break between pictures
resolution = (1024, 768) #(720, 480) (800, 600) (1024, 768)(1280, 720) (1280, 1024)(1600, 1200) (1920, 1080)
frameDelay = 10 # Time between frames in 1/100 second, in gif file.



cam = PiCamera()
cam.resolution = resolution 

def preview(ptime):
    cam.start_preview(alpha=255) 
    #cam.framerate = 15
    sleep(ptime)
    cam.stop_preview()

def makeTimeLapse():
    try:
        for i in range(numberPics): 
            print("Photo {} of {}".format(i+1, numberPics))
            cam.capture('/home/pi/Desktop/timelapse/pics/image{0:04d}.jpg'.format(i))
            sleep(sleepTime)
    except FileNotFoundError:
        print('There seems to be a problem with a folder, Your filepath should be like this "/home/pi/Desktop/timelapse/pics/".')
        print('Ending.')
        exit()

def makeGif():
    try:
        print('Converting files to Gif...')
        system('convert -delay {} -loop 0 /home/pi/Desktop/timelapse/pics/image*.jpg animation.gif'.format(frameDelay)) 
        print('Gif file ready.')
    except FileNotFoundError:
        print('There seems to be a problem with a folder, Your filepath should be like this "/home/pi/Desktop/timelapse/pics/".')
        print('Ending.')
        exit()

print("Adjust the camera to position.")
sleep(2)
preview(previewTime)
ready = input("Start timelapse? y or n: ")
if ready.lower() == 'y':
    print('Starting timelapse.')
    makeTimeLapse()
    print('Finish making pictures.')
    makeGif()
else:
    print('Ending.')


