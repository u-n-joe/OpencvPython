import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

#################
widthImg, heightImg = 640, 480
#################

cap = cv2.VideoCapture(0) # 경로를 넣으면 비디오재생 0을넣으면 웹캠 실행
# 사이즈지정
cap.set(3,frameWidth)
cap.set(4,frameHeight)
# 밝기 지정
cap.set(10,150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres
    #return imgCanny

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # RETR_EXTERNAL = 아웃 코너 사용할때 좋은 함수이다.
    for count in contours:
        area = cv2.contourArea(count)
        print(f'area : {area}')
        if area > 5000:
            #cv2.drawContours(imgContour, count, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(count,True)  # 적분을 통해 길이를 구한다. 곡선의 길이를 말함.
            approx = cv2.approxPolyDP(count, 0.02*peri, True)  # approxPolyDP 함수로 다각형을 검출 할 수 있다.
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 10)
    return biggest

# Contour 좌표값이 순서없이들어오기 때문에 Warp 하기전에 좌표값의 순서를 먼저 정리하는 함수
def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))  # (4,1,2) -> (4,2)
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    # print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print("NewPoints",myPointsNew)
    return myPointsNew

def getWarp(img, biggest):
    biggest = reorder(biggest)
    print(biggest.shape)
    pts1 = np.float32(biggest)  # points 1 Ltop, Rtop, Lbottom, Rbottom 가져올 픽셀 좌표 지정
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # points 2 에서

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))  # 이미지에 matrix를 warping함
    return imgOutput


while True:
    success, img = cap.read()  # success는 bool이다.
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    imgWarped = getWarp(img,biggest)

    cv2.imshow('video', imgWarped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break