import cv2 as cv

# 이미지 불러오기 (흑백으로)
img = cv.imread('./opencv/Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

# 히스토그램 평활화
equalized = cv.equalizeHist(img)

# 결과 보이기
cv.imshow('Original image', img)
cv.imshow('Histogram Equalized Image', equalized)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()
