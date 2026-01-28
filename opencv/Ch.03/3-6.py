import cv2 as cv

# 이미지 불러오기 (흑백으로)
img = cv.imread('./opencv/Ch.03/dog.jpg')

# 가우시안 블러 적용(커널 크기 5*5, 시그마 0은 자동 계산)
blurred = cv.GaussianBlur(img, (5,5), 0)

# 작은 필터 적용해보기
small_kernel = cv.GaussianBlur(img, (1,1), 0)

# 큰 필터 적용해보기
big_kernel = cv.GaussianBlur(img, (11,11), 0)

# 원본 이미지 vs 블러 이미지 출력
cv.imshow('Original image', img)
cv.imshow('Gaussian Blured Image', blurred)
cv.imshow('Gaussian Blured Image_small kernel', small_kernel)
cv.imshow('Gaussian Blured Image_big kernel', big_kernel)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()