import cv2 as cv
import numpy as np

# 1. 빈 캔버스 생성
canvas = np.ones( (200, 600), dtype=np.uint8) *255

# 2. 'Signature' 텍스트를 붓글씨 폰트로 그리기
cv.putText(canvas, 'Signature', (30,130), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (0,), 8, cv.LINE_AA)

# 3. 이미지 이진화 (글씨는 흰색으로, 배경은 검정색으로 반전)
_, binary = cv.threshold(canvas, 127, 255, cv.THRESH_BINARY_INV)

# 4. 모폴로지용 커널 생성 (원형, 크기 7*7)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))

# 5. 모폴로지 연산 수행
erosion = cv.erode(binary, kernel, iterations=1)
dilation = cv.dilate(binary, kernel, iterations=1)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)

# 6. 결과 출력
cv.imshow('Original Binary', binary)
cv.imshow('Erosion', erosion)
cv.imshow('Dilation', dilation)
cv.imshow('Opening', opening)
cv.imshow('Closing', closing)

# 7. 키 대기 및 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()

