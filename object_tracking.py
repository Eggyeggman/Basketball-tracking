from sre_constants import SUCCESS
from xml.sax import saxutils
import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking using raytracing 4k ultra hd graphics", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)
def drawbox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x + w, y + h),(0,0,0),3)
    cv2.putText(img,"Tracking using raytracing 4k ultra hd graphics",(100,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(250,250,250),10)


while True:
    check,img = video.read()   
    SUCCESS,bbox = tracker.update(img)
    if SUCCESS:
        drawbox(img,bbox)
    else:
        cv2.imshow("You failed. booooooooooo")

    cv2.imshow("Results from tracking using raytracing 4k ultra hd graphics",img)

    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break



video.release()
cv2.destroyALLwindows()