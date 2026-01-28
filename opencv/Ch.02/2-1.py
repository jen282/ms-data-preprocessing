import cv2 as cv
import sys

# 이미지 플래그 지정
# 이름 또는 숫자로 지정
img = cv.imread('./opencv/Ch.02/soccer.jpg', cv.IMREAD_GRAYSCALE)

# 이미지가 없는 경우 오류 메시지 출력 후 종료
if img is None:
    sys.exit('File Not Found')

# 이미지를 출력
cv.imshow('Image Display', img)

# 이미지를 새로운 파일로 저장
cv.imwrite('./opencv/Ch.02/soccer2.jpg', img)

# 키 입력 대기
cv.waitKey()

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyWindow()