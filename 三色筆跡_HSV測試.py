import numpy as np
import cv2



# 
cap = cv2.VideoCapture(0)

TrackBar = cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640,320)

def empty():
    pass

cv2.createTrackbar('hue_max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('hue_min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('saturation_max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('saturation_min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('value_max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('value_min', 'TrackBar', 0, 255, empty)

#
while True:
    hue_max = cv2.getTrackbarPos('hue_max', 'TrackBar')
    hue_min = cv2.getTrackbarPos('hue_min', 'TrackBar')
    saturation_max = cv2.getTrackbarPos('saturation_max', 'TrackBar')
    saturation_min = cv2.getTrackbarPos('saturation_min', 'TrackBar')
    value_max = cv2.getTrackbarPos('value_max', 'TrackBar')
    value_min = cv2.getTrackbarPos('value_min', 'TrackBar')

    #
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    upper = np.array([hue_max, saturation_max, value_max])
    lower = np.array([hue_min, saturation_min, value_min])
    mask = cv2.inRange(hsv, lower, upper)
    
    result = cv2.bitwise_and(frame,frame, mask = mask)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    
    cv2.waitKey(1)




