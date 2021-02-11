# 2. Edge Detection
import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
kernel = np.ones((5,5), np.uint8)  # uint8 : 0 ~ 255

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # opencv 는 BGR으로 리턴됨
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img,100,100)
imgCanny2 = cv2.Canny(img,150,200)
imgDialatain = cv2.dilate(imgCanny, kernel, iterations=1)  # 엣지의 매트릭스를 확장시켜 커널로 1을 넣어줘서 엣지의 굵기를 넓힘
imgEroded = cv2.erode(imgDialatain, kernel, iterations=1)  # 엣지의 군데 마다 자리를 차지함


cv2.imshow('GrayImage', imgGray)
cv2.imshow('BlurImage', imgBlur)
cv2.imshow('CannyImage', imgCanny)
cv2.imshow('CannyImage2', imgCanny2)
cv2.imshow('DialatainImage', imgDialatain)
cv2.imshow('ErodedImage', imgEroded)



cv2.waitKey(0)

# 1. Gray Scale and Blur
'''
import cv2

img = cv2.imread('Resources/lena.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opencv 는 BGR으로 리턴됨
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

cv2.imshow('GrayImage', imgGray)
cv2.imshow('BlurImage', imgBlur)
cv2.waitKey(0)
'''