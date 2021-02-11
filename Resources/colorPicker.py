import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)  # 이름을 같게 해줘야 resize가 가능하다. 즉이름이 변수 역할을 하는 샘이다.
# 윈도우에 트랙바 붙이기
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)  # 트랙바이름, 윈도우 이름, 미니멈, 맥시멈, 함수명
cv2.createTrackbar('Sat Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 0, 255, empty)
cv2.createTrackbar('Hue Max', 'Trackbar', 179, 179, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

# 트랙바의 변동에 맞에 계속 이미지를 띄워줘야하니까 while으로 묶어줌...
while True:
    _, img = cap.read()
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
    result = cv2.bitwise_and(img,img,mask=mask)  # 원본 이미지와 합치기
    #imgStack = stackImages(0.6,([img,imgHSV], [mask,imgResult]))

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()