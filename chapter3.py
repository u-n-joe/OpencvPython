
# 2. cropping

import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
print(img.shape)  # 350x612x3(y,x,c)

imgResize = cv2.resize(img,(300,200))  # (x,y)  # 200x300x3(y,x,c)으로 사이즈 조정
print(imgResize.shape)

imgCropped = img[0:200, 200:500]  # y축, x축 이미지의배열이 (y,x,c) 순으로 되어있으므로 y먼저 넣어줘야 한다.

cv2.imshow('Image',img)
cv2.imshow('Image Resize ',imgResize)
cv2.imshow('Image Cropped ',imgCropped)


cv2.waitKey(0)

# 1. resizing
'''
import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
print(img.shape)  # 350x612x3(y,x,c)

imgResize = cv2.resize(img,(300,200))  # (x,y)  # 200x300x3(y,x,c)으로 사이즈 조정
print(imgResize.shape)

cv2.imshow('Image',img)
cv2.imshow('Image Resize ',imgResize)

cv2.waitKey(0)
'''