import cv2 as cv

# 이미지 불러오기 
img = cv.imread('./opencv/Ch.03/dog.jpg')

# 확대할 크기 지정 - 2배 확대
new_size = (img.shape[1]*2, img.shape[0]*2)

# 보간 방법
# 1. Nearest
res_nearest = cv.resize( img, new_size, interpolation=cv.INTER_NEAREST)
# 2. Linear
res_linear = cv.resize(img, new_size, interpolation=cv.INTER_LINEAR)
# 3. Cubic
res_cubic = cv.resize(img, new_size, interpolation=cv.INTER_CUBIC)

# 결과 출력 
cv.imshow('Original', img)
cv.imshow('Inter Nearest', res_nearest)
cv.imshow('Inter Linear', res_linear)
cv.imshow('Inter Cubic', res_cubic)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()