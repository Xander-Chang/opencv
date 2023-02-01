import numpy as np
import cv2

img = cv2.imread('cats.jpg')
# cv2.split
b,g,r = cv2.split(img)
cv2.imshow('blue', b)
cv2.imshow('green',g)
cv2.imshow('red',r)
# cv2.merge
merged = cv2.merge([r,g,b])             # 顏色會變成 rgb
merged = cv2.merge([b,g,r])
cv2.imshow('merged',merged)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# 填上顏色
blank = np.empty(img.shape[:2], dtype='uint8')
# 填上黑色
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('blue', blue)
cv2.imshow('green',green)
cv2.imshow('red',red)

cv2.waitKey(0)