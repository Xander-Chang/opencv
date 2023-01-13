import cv2
import numpy as np

# find_pen_HSV = [[]]
draw_points = []

def find_pen(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 45, 255), (9, 160, 255))
    
    pen_x, pen_y = find_comtour(mask)
    if pen_x != -1:                             # 如果有找到輪廓(x != -1), 把值加到 draw_points[] 裡面
        draw_points.append([pen_x, pen_y])
        for draw_p in draw_points:
            cv2.circle(frame, (draw_p[0],draw_p[1]),10,(0,100,255), cv2.FILLED)
    

def find_comtour(mask):
    cnts, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = -1,-1,-1,-1   # ???
    for cnt in cnts:
        # area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, perimeter*0.01, True)
        x,y,w,h = cv2.boundingRect(vertices)
    return x,y







cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret:
        
        find_pen(frame)
        # img_contour = frame.copy()
        # cv2.imshow('img_contour',img_contour)
        cv2.imshow('frame',frame)
        print('播放中')
    else:
        print('不存在 / 播放完')
        break
    
    if cv2.waitKey(90) == ord('q') or cv2.waitKey(90) == 27:
        print('離開')
        break