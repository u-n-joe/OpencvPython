#3.

import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    print(rows)
    cols = len(imgArray[0])
    print(cols)
    rowsAvailable = isinstance(imgArray[0], list)
    print(rowsAvailable)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# 이미지 윤곽(contours)과 계층(hierarchy)을 이용한 함수
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # RETR_EXTERNAL = 아웃 코너 사용할때 좋은 함수이다.
    for count in contours:
        area = cv2.contourArea(count)
        print(f'area : {area}')
        if area > 500:
            cv2.drawContours(imgContour, count, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(count,True)  # 적분을 통해 길이를 구한다. 곡선의 길이를 말함.
            print(f'peri : {peri}')  # 각 윤곽점을 찍음
            approx = cv2.approxPolyDP(count, 0.02*peri, True)  # approxPolyDP 함수로 다각형을 검출 할 수 있다.
            print(f'approx : {len(approx)}')  # 각 꼭지점의 갯수를 알 수 있다.
            objCor = len(approx)  # 코너  수 변수 선언
            x, y, w, h = cv2.boundingRect(approx)  # boundingRect 바운딩 박스 만들어주는 부분

            if objCor == 3: objectType = 'tri'
            elif objCor == 4:  # 직사각형과 정사각형 변수처리
                aspRatid = w/float(h)
                if aspRatid > 0.95 and aspRatid < 1.05 : objectType = 'Square'
                else:objectType='Rectangle'
            elif objCor>4 : objectType='Circle'

            else: objectType='None'

            cv2.rectangle(imgContour, (x,y), (x+w,y+h),(0,255,0),3)  # rectangle함수로 각 이미지에 x,y(0,0)좌표를 찍고, 높이와 넓이를 넣어줘서 박스르 그림
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0,0,100),2)



path = 'Resources/Shape.png'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgStack = stackImages(0.8, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))

# cv2.imshow('Image',img)
# cv2.imshow('Image imgGray',imgGray)
# cv2.imshow('Image imgBlur',imgBlur)

cv2.imshow('Image_Stack', imgStack)

cv2.waitKey(0)

#2. 윤곽(Contour) 찾아내는 함수 사용 >> cv2.findContours
'''
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
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
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
        hor = np.hstack(imgArray)
        ver = hor
    return ver

# 이미지 윤곽(contours)과 계층(hierarchy)을 이용한 함수
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # RETR_EXTERNAL = 아웃 코너 사용할때 좋은 함수이다.
    for count in contours:
        area = cv2.contourArea(count)
        print(area)
        cv2.drawContours(imgContour, count, -1, (255, 0, 0), 3)
        

path = 'Resources/Shape.png'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

# cv2.imshow('Image',img)
# cv2.imshow('Image imgGray',imgGray)
# cv2.imshow('Image imgBlur',imgBlur)

cv2.imshow('Image_Stack',imgStack)

cv2.waitKey(0)
'''

#1. 이미지 Stack
'''
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

path = 'Resources/Shape.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgBlank,imgBlank]))

# cv2.imshow('Image',img)
# cv2.imshow('Image imgGray',imgGray)
# cv2.imshow('Image imgBlur',imgBlur)

cv2.imshow('Image_Stack',imgStack)

cv2.waitKey(0)
'''