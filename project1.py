import cv2
import numpy as np
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)  # 경로를 넣으면 비디오재생 숫자0을넣으면 안쪽웹캠 실행 1은 바깥
# 사이즈지정
cap.set(3,frameWidth)  # id 지정 3
cap.set(4,frameHeight)  # id 4
# 밝기 지정
cap.set(10,130)  # id 10

# 색 추가 리스트
myColors = [[133, 93, 124, 179, 255, 255], #Red
            [39, 0, 122, 83, 255, 255], #Green
            [88, 100, 75, 132, 235, 255]] #Blue
myColorVal = [[0,0,255],[0,255,0],[255,51,51]]   # BGR

# 포인트 받는 리스트
myPoints = []  # [x, y, colorId]

def findColor(img, myColors, myColorVal):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)  # imgHSV 이미지에 필터 입히기.
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorVal[count], cv2.FILLED)  # 바운딩 박스의 센터에 꼭지점을 띄워준다. 색을지정한다.
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

# 이미지 윤곽(contours)과 계층(hierarchy)을 이용한 함수
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # RETR_EXTERNAL = 아웃 코너 사용할때 좋은 함수이다.
    x,y,w,h = 0,0,0,0
    for count in contours:
        area = cv2.contourArea(count)
        if area > 500:
            # cv2.drawContours(imgResult, count, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(count,True)  # 적분을 통해 길이를 구한다. 곡선의 길이를 말함.
            approx = cv2.approxPolyDP(count, 0.02*peri, True)  # approxPolyDP 함수로 다각형을 검출 할 수 있다.
            x, y, w, h = cv2.boundingRect(approx)  # boundingRect 바운딩 박스 만들어주는 부분
    return x+w//2, y  # 센터점 을 return

def drawOnCanvas(myPoints, myColorVal):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorVal[point[2]], cv2.FILLED)   # 바운딩 박스의 센터에 꼭지점을 띄워준다. 색을지정한다.



while True:
    success, img = cap.read()  # success 는 bool 이다.
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorVal)
    if len(newPoints) != 0:  # Point 가 있는지 없는지 확인한다.
        for newP in newPoints:  # 반복문은 사용하는 이유는 return 으로 list 형태를 받기 때문이다.
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorVal)

    cv2.imshow('video',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break