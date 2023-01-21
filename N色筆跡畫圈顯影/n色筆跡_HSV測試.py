import cv2
import numpy as np


cap = cv2.VideoCapture(0)
track_bar = cv2.namedWindow('track_bar')
cv2.resizeWindow('track_bar', 640,320)

def empty():
    pass

cv2.createTrackbar('hue_min', 'track_bar',0, 179, empty)
cv2.createTrackbar('hue_max', 'track_bar',179, 179, empty)
cv2.createTrackbar('saturation_min', 'track_bar',0, 255, empty)
cv2.createTrackbar('saturation_max', 'track_bar',255, 255, empty)
cv2.createTrackbar('value_min', 'track_bar',0, 255, empty)
cv2.createTrackbar('value_max', 'track_bar',255, 255, empty)

while True:
    hue_min = cv2.getTrackbarPos('hue_min', 'track_bar')
    hue_max = cv2.getTrackbarPos('hue_max', 'track_bar')
    saturation_min = cv2.getTrackbarPos('saturation_min', 'track_bar')
    saturation_max = cv2.getTrackbarPos('saturation_max', 'track_bar')
    value_min = cv2.getTrackbarPos('value_min', 'track_bar')
    value_max = cv2.getTrackbarPos('value_max', 'track_bar')
    
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (hue_min, saturation_min, value_min), (hue_max, saturation_max, value_max))
    
    result = cv2.bitwise_and(frame,frame, mask=mask)
    
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)