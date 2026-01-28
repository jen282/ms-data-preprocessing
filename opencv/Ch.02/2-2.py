import cv2 as cv
import sys

img = cv.imread('./opencv/Ch.02/soccer.jpg')

if img is None:
    sys.exit('File Not Found')

# 기존 이미지를 Gray 이미지로 변환
Gray_image = cv.cvtColor(img, cv.COLOR_BGR2YUV)

# 이미지 출력
cv.imshow('Image Display', Gray_image)

# 키 입력 대기
cv.waitKey()

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyWindow()