import cv2 as cv

# 웹캠 열기 (기본 장치는 0번)
cap = cv.VideoCapture(0)

# 웹캠 열기 실패 여부 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 이미지 캡쳐 저장할 리스트
captured_images = []

print("> 'a':한 장 캡쳐, 'q': 캡쳐 이미지 보기 및 종료")

while True:
    ret, frame = cap.read() # 한 프레임 읽기 
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break

    cv.imshow('Live WebCam', frame)
    key = cv.waitKey(1) & 0xFF

    # 'a'키 누르면 현재 프레임 복사해서 저장
    if key == ord('a'):
        captured_images.append(frame.copy())
        print(f'{len(captured_images)}번째 이미지 캡쳐됨')

    elif key == ord('q'):
        print(f' 총 {len(captured_images)}장의 이미지가 캡쳐되었습니다')
        break

# 사용한 자원 해제
cap.release()
cv.destroyAllWindows()

# 캡쳐된 이미지들 하나씩 보여주기
for idx, img in enumerate(captured_images):
    cv.imshow(f'Captured Image {idx+1}', img)
    cv.waitKey(0) #아무 키나 누르면 다음 이미지로

cv.destroyAllWindows()