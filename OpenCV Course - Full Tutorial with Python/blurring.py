import numpy as np
import cv2

img = cv2.imread('cats.jpg')
cv2.imshow('img',img)

# sample 1: averaging blur
average = cv2.blur(img,(3,3))
cv2.imshow('averaging blur',average)

# sample 2: Gaussian blur
Gaussian = cv2.GaussianBlur(img,(3,3),0)           # sigmaX 先設 0 就好
cv2.imshow('Gaussian blur', Gaussian)

# sample 3: median blur
median = cv2.medianBlur(img, 3)
cv2.imshow('median blur',median)

# sample 4: bilateral blur
bilateral = cv2.bilateralFilter(img, 3, 35, 25)             # 給直徑不是內核
cv2.imshow('bilateral blur',bilateral)

cv2.waitKey(0)