# 5. 텍스트 입력하기

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.circle(img, (400,50),30 ,(0,255,0), 5)  # img, Center, Radius, color, thickness
cv2.putText(img, 'opencv', (140,256), cv2.FONT_HERSHEY_DUPLEX , 2 , (0,0,255),2)

cv2.imshow('color_img', img)

cv2.waitKey(0)


# 4. 원 그리기
'''
import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.circle(img, (400,50),30 ,(0,255,0), 5)  # img, Center, Radius, color, thickness

cv2.imshow('color_img', img)

cv2.waitKey(0)
'''

# 3. 사각형 그리기
'''
import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img2 = np.zeros((512,512,3), np.uint8)
img3 = np.zeros((512,512,3), np.uint8)
img4 = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (300,300), (0,255,0), 3)  # img, pt1(startPoint), pt2(endPoint), color, thickness
cv2.line(img2, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)  # img, pt1(startPoint), pt2(endPoint), color, thickness
cv2.rectangle(img3, (0,0), (250,350), (0,0,255), 3)
cv2.rectangle(img4, (0,0), (250,350), (0,0,255), cv2.FILLED)

cv2.imshow('color_img', img)
cv2.imshow('color_img2', img2)
cv2.imshow('color_img3', img3)
cv2.imshow('color_img4', img4)

cv2.waitKey(0)
'''

# 2. 라인 그리기
'''
import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img2 = np.zeros((512,512,3), np.uint8)


cv2.line(img, (0,0), (300,300), (0,255,0), 3)  # img, pt1(startPoint), pt2(endPoint), color, thickness
cv2.line(img2, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)  # img, pt1(startPoint), pt2(endPoint), color, thickness


cv2.imshow('color_img', img)
cv2.imshow('color_img2', img2)

cv2.waitKey(0)
'''
# 1. 픽셀값 변경하기
'''
import cv2
import numpy as np

gray_img = np.zeros((512,512))  # 채널을 안 넣어줌
print(gray_img.shape)

color_img = np.zeros((512,512,3), np.uint8)  # 채널을 넣어줌
print(color_img.shape)
color_img[:] = 255,0,0  # 전체 범위
print(color_img.shape)

color_img2 = np.zeros((512,512,3), np.uint8)  # 채널을 넣어줌
print(color_img.shape)
color_img2[200:300, 100:300] = 255,0,0  # 범위 지정 
print(color_img.shape)

cv2.imshow('gray_img', gray_img)
cv2.imshow('color_img', color_img)
cv2.imshow('color_img2', color_img2)


cv2.waitKey(0)
'''