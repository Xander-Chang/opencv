import numpy as np
import cv2



# 找筆
def Find_Pen(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    upper = np.array([138, 216, 165])
    lower = np.array([57, 69, 53])
    mask = cv2.inRange(hsv, lower, upper)
    
    result = cv2.bitwise_and(frame,frame, mask = mask)
    
    pen_x, pen_y = Find_Contour(mask)
    cv2.circle(img_contour, (pen_x,pen_y), 10, (255,0,0), cv2.FILLED)
    
    cv2.imshow('result',result)



def Find_Contour(frame):
    contours, hierachy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = -1,-1,-1,-1
    for cnt in contours:
        cv2.drawContours(img_contour, cnt, -1, (255,0,0), 2)
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, perimeter*0.01, True)
            x,y,w,h = cv2.boundingRect(vertices)
            
            return x, y+w//2




# 播放
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        img_contour = frame.copy()
        Find_Pen(frame)
        
        print('開始播放')
        cv2.imshow('frame', frame)
        cv2.imshow('img_contour', img_contour)
    else:
        print('finish')
        break
    
    if cv2.waitKey(90) == ord('q') or cv2.waitKey(90) == 27:    # Esc
        print('離開')
        break
        


