import numpy as np
import cv2

img = cv2.imread('park.jpg')
cv2.imshow('img',img)
# print(img.shape)

# sample 1: 位移- warpAffine
def translate (img,x,y):
    trans_matrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, trans_matrix, dimensions)
translted = translate(img,200,50)
# cv2.imshow('translted',translted)


# sample 2: 翻轉- rotation
def rotation(img, angle, rotPoint=None):
    if rotPoint is None:
        rotPoint = (img.shape[1]//2, img.shape[0]//2)

    rot_matrix = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, rot_matrix, dimensions)
rotated = rotation(img, -45)
# cv2.imshow('rotation', rotated)

rotated_rotated = rotation(rotated, -45)
# cv2.imshow('rotated_rotated',rotated_rotated)   # 圖片中黑色的部分也會翻轉-45度

rotated_90 = rotation(img, -90)                 # 要翻轉90度就直接翻轉90, 翻45再45會不一樣
# cv2.imshow('rotation_90', rotated_90)

# sample 3: - resizing
resized = cv2.resize(img,(500,500), interpolation=cv2.INTER_CUBIC)
# cv2.imshow("resized", resized)

# sample 4: - 翻轉- flipping
flipped = cv2.flip(img,1)                       # 0、1、-1 效果不同
cv2.imshow("flipped",flipped)







cv2.waitKey(0)