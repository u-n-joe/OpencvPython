# 1. 원근법(Perspective)로 원본 사진에서 원하는 부분만 가져와서 보기

import cv2
import numpy as np

img = cv2.imread('Resources/namecard.jpg')

width, height = 550, 350
print(img.shape)

pts1 = np.float32([[120,105], [930,280], [105,485], [775,680]])  # points 1 Ltop, Rtop, Lbottom, Rbottom 가져올 픽셀 좌표 지정
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])  # points 2

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))  # 이미지에 matrix를 warping함


cv2.imshow('Image',img)
cv2.imshow('Image Output',imgOutput)

cv2.waitKey(0)