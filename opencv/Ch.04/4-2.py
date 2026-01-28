import cv2 as cv

# 이미지 불러오기 
img = cv.imread('./opencv/Ch.04/soccer.jpg', cv.IMREAD_GRAYSCALE)

# 1. 가우시안 블러 적용 -> 노이즈 제거
blurred = cv.GaussianBlur(img, (5,5), 1.4)  # 필터 사이즈, 

# 2. 케니 엣지 검출
edges = cv.Canny(blurred, 100, 200) # 임계값1, 임계값2

# 3. 결과 출력
cv.imshow('Original', img)
cv.imshow('Canny Edge', edges)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()
