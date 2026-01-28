import cv2 as cv

# 이미지 불러오기
img = cv.imread('./opencv/Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

# 오추 이진화 적용
ret, binary_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print('자동 계산된 임계값: ', ret)

# 결과 출력
cv.imshow('Original', img)
cv.imshow('Otsu Thresholding', binary_img)

# 키 대기 및 닫기
cv.waitKey(0)
cv.destroyAllWindows()