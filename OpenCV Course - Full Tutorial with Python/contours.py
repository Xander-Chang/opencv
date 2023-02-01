import numpy as np
import cv2

img = cv2.imread('cats.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 125, 175)

ret, thresh = cv2.threshold(gray, 125,255, cv2.THRESH_BINARY)

# find contours
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# draw contours
blank = np.empty(img.shape, dtype='uint8')
cv2.drawContours(blank, contours, -1, (0,255,0), 1)



cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny edge', canny)
# cv2.imshow('thresh', thresh)
cv2.imshow('contours draw', blank)      # 用canny去找輪廓，畫出來會很像canny圖

 

cv2.waitKey(0)

