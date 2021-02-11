
# 2. 이미지 붙이는 함수 선언
import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    print(rows)
    cols = len(imgArray[0])
    print(cols)
    rowsAvailable = isinstance(imgArray[0], list)
    print(rowsAvailable)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread('Resources/lena.png')

hor = np.hstack((img, img))  # 이미지 horizontally 붙여줌
ver = np.vstack((img, img))  # 이미지를 vertically 붙여줌

cv2.imshow('Image',img)
cv2.imshow('Image_hor',hor)
cv2.imshow('Image_ver',ver)

cv2.waitKey(0)


# 1. 이미지 붙이기
'''
import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

hor = np.hstack((img, img))  # 이미지 horizontally 붙여줌
ver = np.vstack((img, img))  # 이미지를 vertically 붙여줌

cv2.imshow('Image',img)
cv2.imshow('Image_hor',hor)
cv2.imshow('Image_ver',ver)

cv2.waitKey(0)
'''