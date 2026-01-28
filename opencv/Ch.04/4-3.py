import cv2 as cv
import numpy as np

# 이미지 불러오기 
img = cv.imread('./opencv/Ch.04/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 비교를 위해 윤곽선 그리기 전 이미지 출력
cv.imshow('aaa', img)

# Canny 엣지 검출
edges = cv.Canny(gray, 100, 200)

# 윤곽선 찾기
contours, _ =cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 윤곽선 길이 >= 50 인것만 원본 이미지에 그리기
for contour in contours:
    length = cv.arcLength(contour, closed=True)
    if length >= 50:
        cv.drawContours(img, [contour], -1, (0,255,0), 1) # 초록색, 두께1

# 결과 이미지(원본) 출력
cv.imshow("Contours over Original", img)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()