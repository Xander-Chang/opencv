import numpy as np 
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('cats.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle_mask = cv2.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked = cv2.bitwise_and(gray,gray, mask=circle_mask)

# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
cv2.imshow('circle_mask',circle_mask)
cv2.imshow('masked',masked)


gray_hist = cv2.calcHist([gray], [0], circle_mask, [256], [0,256])


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



cv2.waitKey(0)                  # 放最後，不然圖關掉，才會跑圖表的程式碼，才會跑出圖表

