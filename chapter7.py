
#2-3. 트랙바를 이용 해서 필터 입히기
import cv2
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    #print(rows)
    cols = len(imgArray[0])
    #print(cols)
    rowsAvailable = isinstance(imgArray[0], list)
    #print(rowsAvailable)
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
        hor = np.hstack(imgArray)
        ver = hor
    return ver

path = 'Resources/lena.png'

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)  # 이름을 같게 해줘야 resize가 가능하다. 즉이름이 변수 역할을 하는 샘이다.
# 윈도우에 트랙바 붙이기
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)  # 트랙바이름, 윈도우 이름, 미니멈, 맥시멈, 함수명
cv2.createTrackbar('Hue Max', 'Trackbar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

# 트랙바의 변동에 맞에 계속 이미지를 띄워줘야하니까 while으로 묶어줌...
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbar')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbar')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbar')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbar')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # imgHSV 이미지에 필터 입히기.
    imgResult = cv2.bitwise_and(img,img,mask=mask)  # 원본 이미지와 합치기

    # cv2.imshow('Image',img)
    # cv2.imshow('Image_HSV',imgHSV)
    # cv2.imshow('Image_mask',mask)
    # cv2.imshow('Image_Result',imgResult)

    imgStack = stackImages(0.6,([img,imgHSV], [mask,imgResult]))
    cv2.imshow('Stacked Images', imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#2-2. 트랙바를 이용 해서 필터 입히기
'''
import cv2
import numpy as np

def empty(a):
    pass

path = 'Resources/lena.png'

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)  # 이름을 같게 해줘야 resize가 가능하다. 즉이름이 변수 역할을 하는 샘이다.
# 윈도우에 트랙바 붙이기
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)  # 트랙바이름, 윈도우 이름, 미니멈, 맥시멈, 함수명
cv2.createTrackbar('Hue Max', 'Trackbar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

# 트랙바의 변동에 맞에 계속 이미지를 띄워줘야하니까 while으로 묶어줌...
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbar')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbar')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbar')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbar')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # imgHSV 이미지에 필터 입히기.

    cv2.imshow('Image',img)
    cv2.imshow('Image_HSV',imgHSV)
    cv2.imshow('Image_mask',mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
#2-1. 트랙바를 이용 해서 필터 입히기
'''
import cv2

def empty(a):
    pass

path = 'Resources/lena.png'

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)  # 이름을 같게 해줘야 resize가 가능하다. 즉이름이 변수 역할을 하는 샘이다.
# 윈도우에 트랙바 붙이기
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)  # 트랙바이름, 윈도우 이름, 미니멈, 맥시멈, 함수명
cv2.createTrackbar('Hue Max', 'Trackbar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

# 트랙바의 변동에 맞에 계속 이미지를 띄워줘야하니까 while으로 묶어줌...
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbar')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbar')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbar')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbar')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)


    cv2.imshow('Image',img)
    cv2.imshow('Image_HSV',imgHSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

#2. 트랙바를 이용 해서 필터 입히기
'''
import cv2

def empty(a):
    pass

path = 'Resources/lena.png'

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)  # 이름을 같게 해줘야 resize가 가능하다. 즉이름이 변수 역할을 하는 샘이다.
# 윈도우에 트랙바 붙이기
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)  # 트랙바이름, 윈도우 이름, 미니멈, 맥시멈, 함수명
cv2.createTrackbar('Hue Max', 'Trackbar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

# 트랙바의 변동에 맞에 계속 이미지를 띄워줘야하니까 while으로 묶어줌...
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    print(h_min)

    cv2.imshow('Image',img)
    cv2.imshow('Image_HSV',imgHSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
#1. 필터 입히기
'''
import cv2

path = 'Resources/lena.png'
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow('Image',img)
cv2.imshow('Image_HSV',imgHSV)

cv2.waitKey(0)
'''