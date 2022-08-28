from picamera import PiCamera
from os import system
from time import sleep


# Variables
previewTime = 3 # Preview to adjust camera in seconds
numberPics = 12 # Number of pictures to be taken during timelapse.
sleepTime = 2 # Break between pictures
resolution = (1024, 768) #(720, 480) (800, 600) (1024, 768)(1280, 720) (1280, 1024)(1600, 1200) (1920, 1080)
frameDelay = 10 # Time between frames in 1/100 second, in gif file.
picsFolder = '/home/pi/Desktop/timelapse/pics'


cam = PiCamera()
cam.resolution = resolution 

def preview(ptime):
    cam.start_preview(fullscreen=False, window = (100, 20, 640, 480)) # Window parameter = (x,y,width,height) xy = position on screen 
    sleep(ptime)
    cam.stop_preview()

def makeTimeLapse():
    try:
        for i in range(numberPics): 
            print("Photo {} of {}".format(i+1, numberPics))
            cam.capture('{picsfolder}/image{0:04d}.jpg'.format(i, picsfolder=picsFolder))
            sleep(sleepTime)
    except FileNotFoundError:
        print('There seems to be a problem with a folder, Your filepath should be like this "/home/pi/Desktop/timelapse/pics/".')
        print('Ending.')
        exit()

def makeGif():
    try:
        print('Converting files to Gif...')
        system('convert -delay {delay} -loop 0 {picsFolder}/image*.jpg /home/pi/Desktop/timelapse/animation.gif'.format(delay=frameDelay, picsFolder=picsFolder)) 
        print('Gif file ready.')
    except FileNotFoundError:
        print('There seems to be a problem with a folder, Your filepath should be like this "/home/pi/Desktop/timelapse/pics/".')
        print('Ending.')
        exit()

def makeMovie():
    try:
        print('Converting files to mpeg movie...')
        system('ffmpeg -r 20 -i {picsFolder}/image%04d.jpg -qscale 2 /home/pi/Desktop/timelapse/animation.mp4'.format(picsFolder=picsFolder))
        # -r 20 = 20 frames per second
        print('Movie file ready.')
    except FileNotFoundError:
        print('There seems to be a problem with a folder, Your filepath should be like this "/home/pi/Desktop/timelapse/pics/".')
        print('Ending.')
        exit()    

print("Adjust the camera to position.")
sleep(2)
preview(previewTime)

fileFormat = input('Press "1" for gif format or "2" for mp4 format or "3" for both formats: ')
ready = input("Start timelapse? y or n: ")

if ready.lower() == 'y':
    print('Starting timelapse.')
    makeTimeLapse()
    print('Finish making pictures.')

    if fileFormat == '1':
        makeGif()
    elif fileFormat == '2':
        makeMovie()
    elif fileFormat == '3':
        makeGif()
        makeMovie()
    else:
        print('You didnt press 1 or 2 or 3')
else:
    print('Ending')
print('Scipt closing.')


'''
if ready.lower() == 'y':
    
    print('Starting timelapse.')
    makeTimeLapse()
    print('Finish making pictures.')
    
    fileFormat = input('Press "1" for gif format or "2" for mp4 format or "3" for both formats: ')
    if fileFormat == '1':
        makeGif()
    elif fileFormat == '2':
        makeMovie()
    elif fileFormat == '3':
        makeGif()
        makeMovie()
    else:
        print('You didnt press 1 or 2 or 3')
else:
    print('Ending.')
    '''