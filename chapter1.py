#3 웹캠 켜기
import cv2

cap = cv2.VideoCapture(0) # 경로를 넣으면 비디오재생 0을넣으면 웹캠 실행
# 사이즈지정
cap.set(3,640)
cap.set(4,480)
# 밝기 지정
cap.set(10,100)

while True:
    success, img = cap.read()  # success는 bool이다.
    cv2.imshow('video',img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


#2 동영상 재생
'''
import cv2

cap = cv2.VideoCapture('Resources/test.mp4')
while True:
    success, img = cap.read()  # success는 bool이다.
    cv2.imshow('video',img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
'''


#1 사진 열기
'''
import cv2
print("start")

img = cv2.imread('Resources/lena.png')

cv2.imshow('output', img)
cv2.waitKey(0)
'''