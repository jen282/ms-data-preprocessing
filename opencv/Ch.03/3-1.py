import cv2 as cv
import numpy as np

# 1.이미지 불러오기
img = cv.imread('./opencv/Ch.03/RGB.jpg')
if img is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다.")

# 2. 이미지 출력하기
img = cv.resize(img, (400,400))
cv.imshow('Original image', img)
cv.imshow('Blue channel', img[:,:,0])
cv.imshow('Green channel', img[:,:,1])
cv.imshow('Red channel', img[:, :, 2])

# 3. 키 입력 대기 후 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()