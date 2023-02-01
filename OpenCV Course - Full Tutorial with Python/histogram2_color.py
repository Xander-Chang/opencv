import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cats.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow('img',img)
cv2.imshow('masked',masked)



plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.xlim((0,256))

colors = ('b','g','r')
for i , col in enumerate(colors):
    color_hist = cv2.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(color_hist, color=col)
    
plt.show()

cv2.waitKey(0)