import cv2 as cv

# 웹캠 열기 (기본 장치는 0번)
cap = cv.VideoCapture(0)

# 웹캠 열기 실패 여부 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read() # 한 프레임 읽기 
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break

    cv.imshow('Live Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv.destroyAllWindows()