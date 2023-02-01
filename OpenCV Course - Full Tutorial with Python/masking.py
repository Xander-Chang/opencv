import numpy as np
import cv2

img = cv2.imread('cats.jpg')
blank = np.empty(img.shape[:2], dtype='uint8')
# mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255,-1)
# masked = cv2.bitwise_and(img,img, mask=mask)
circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100,255,-1)
rectangle = cv2.rectangle(blank.copy(), (30,30),(370,370), 255,-1)
weird_shape_mask = cv2.bitwise_and(circle, rectangle)                       # 模具
weird_shape_masked = cv2.bitwise_and(img,img, mask= weird_shape_mask)       # 模具蓋原圖

cv2.imshow('img',img)
cv2.imshow('blank',blank)
# cv2.imshow('mask',mask)
# cv2.imshow('masked',masked)
cv2.imshow('circle',circle)
cv2.imshow('rectangle',rectangle)
cv2.imshow('weird_shape', weird_shape_mask)
cv2.imshow('weird_shape_masked', weird_shape_masked)
cv2.waitKey(0)



