import numpy as np
import cv2



# HSV: 藍、紅、黃
pen_colorHSV = [[95, 76, 81, 179, 255, 255],
                [0, 117, 82, 13, 255, 255],
                [18, 101, 93, 31, 255,214]]

pen_colorBGR = [[255,0,0],
                [0,0,255],
                [0,255,255]]

# [x, y , color_id]
draw_points = []



# 找筆、筆尖
def Find_Pen(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    for i in range(len(pen_colorHSV)):
        upper = np.array(pen_colorHSV[i][3:6])
        lower = np.array(pen_colorHSV[i][:3])
        mask = cv2.inRange(hsv, lower, upper)
        
        pen_x, pen_y = Find_Contour(mask)
        
        if pen_y != -1:
            draw_points.append([pen_x, pen_y, i])
        draw(draw_points)
        
        # result = cv2.bitwise_and(frame,frame, mask = mask)
        # cv2.imshow('result',result)




def Find_Contour(mask):
    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = -1,-1,-1,-1
    for cnt in contours:
        # cv2.drawContours(img_contour, cnt, -1, (255,0,0), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, perimeter*0.01, True)
            x,y,w,h = cv2.boundingRect(vertices)
    
    return x+w//2, y



def draw(draw_points):
    for draw_p in draw_points:
        cv2.circle(img_contour, (draw_p[0],draw_p[1]), 10, pen_colorBGR[draw_p[2]], cv2.FILLED)
    



# 播放
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        img_contour = frame.copy()
        cv2.imshow('frame', frame)
        Find_Pen(frame)
        print('開始播放')
        
        cv2.imshow('img_contour', img_contour)
    else:
        print('finish')
        break
    
    if cv2.waitKey(90) == ord('q') or cv2.waitKey(90) == 27:    # Esc
        print('離開')
        break
        


