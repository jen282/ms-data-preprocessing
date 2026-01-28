import cv2 as cv
import numpy as np

# 1. 검정 배경 생성 (300*300)
img = np.zeros( (300, 300, 3), dtype=np.uint8)

# 2. 사각형 좌표 정의: 좌상단(100, 100) -> 우하단 (200, 200)
start_point = (100, 100)
end_point = (200, 200)

# 3. 흰색 사각형 그리기
cv. rectangle(img, start_point, end_point, (255,255,255), -1)

# 4. 이동(translation) : 오른쪽으로 50px, 아래로 30px
tx, ty = 50, 30
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv.warpAffine(img, translation_matrix, (300, 300))

# 5. 회전(rotation) : 중심 기준 45도 회전
center = (150, 150)
angle = 45
scale = 1.0
rotation_matrix = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(translated, rotation_matrix, (300, 300))

# 6. 결과 출력
cv.imshow('Original', img)
cv.imshow('Translated', translated)
cv.imshow('Rotated', rotated)

# 아무 키나 누르면 종료
cv.waitKey(0)
cv.destroyAllWindows()