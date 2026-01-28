import cv2 as cv
import sys

img = cv.imread('./opencv/Ch.02/girl.jpg')

if img is None:
    sys.exit('File Not Found')

# 이미지에 사각형 그리기
cv.rectangle(img, (330,470), (530, 640), color=(255,0,0), thickness=3)

# 이미지에 텍스트 쓰기
cv.putText(img, 'Hello OpenCV', org=(330,450), fontFace=cv.FONT_HERSHEY_SIMPLEX,
           fontScale=1, color=(225,20,200), thickness=2)

# 이미지 출력
cv.imshow('Image Display', img)

# 키 입력 대기
cv.waitKey()

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyWindow()