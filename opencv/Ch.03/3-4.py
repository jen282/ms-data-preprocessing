import cv2 as cv
import numpy as np

# 감마 보정 함수 정의 (단일 이미지 처리)
def adjust_gamma(image, gamma):
    image1 = image / 255.0
    return np.uint8(255 * (image1 ** gamma))

# 이미지 불러오기
img = cv.imread('./opencv/Ch.03/dog.jpg')
img = cv.resize(img, (300, 300))

# 테스트할 감마값 리스트
gammas = [0.5, 0.75, 1, 2, 3]

# 각 감마값에 대해 이미지 처리 및 표시
for gamma in gammas:
    adjusted = adjust_gamma(img, gamma)
    window_name = f'Gamma {gamma}'
    cv.imshow(window_name, adjusted)

# 키 값 대기 및 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()