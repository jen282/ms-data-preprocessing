import cv2 as cv
import numpy as np

# 이미지 불러오기 (흑백으로)
img = cv.imread('./opencv/Ch.03/girl.jpg', cv.IMREAD_GRAYSCALE)

# 엠보싱 커널 정의
kernel = np.array([[-2, -1, 0],
                   [-1, 1, 1],
                   [0, 1, 2]], dtype = np.float32)

# 엠보싱 필터(커널) 적용
embossed = cv.filter2D(img, -1, kernel)

# 적용한 이미지 출력
cv.imshow('Original', img)
cv.imshow('Embossed', embossed)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()