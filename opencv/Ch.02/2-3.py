import cv2 as cv
import sys

img = cv.imread('./opencv/Ch.02/soccer.jpg')

if img is None:
    sys.exit('File Not Found')

# 이미지 축소하기 -배율
Small_image = cv.resize(img, dsize=(0,0), fx=0.3, fy=0.3) # 가로, 세로 30% 축소 

# 이미지 축소하기 - 지정된 사이즈로
resized = cv.resize(img, (200, 300))  # 너비 400, 높이 300

# 이미지 출력
cv.imshow('Image Display', Small_image)
cv.imshow('small Image Display', resized)

# 키 입력 대기
cv.waitKey()

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyWindow()