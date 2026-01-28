import cv2 as cv

# 마우스 이벤트 콜백 함수
def draw(event, x, y, flags, param):
    global drawing_left, drawing_right, img
    
    # 왼쪽 버튼 클릭 -> 그리기 시작
    if event == cv.EVENT_LBUTTONDOWN:
        drawing_left = True
    
    # 왼쪽 버튼 드래그 -> 그 경로대로 그리기
    elif event == cv.EVENT_MOUSEMOVE and drawing_left:
        cv.circle( img, (x,y), 5, (255,0,0), -1) #파란색 원
    
    # 왼쪽 버튼 떼기 -> 그리기 종료 
    elif event == cv.EVENT_LBUTTONUP:
        drawing_left = False
    
    # 오른쪽 버튼 클릭 -> 그리기 시작
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_right = True
    
    # 오른쪽 버튼 드래그 -> 그 경로대로 그리기
    elif event == cv.EVENT_MOUSEMOVE and drawing_right:
        cv.circle( img, (x,y), 5, (0,0,255), -1) #빨간색 원

    #오른쪽 버튼 떼기 -> 그리기 종료 
    elif event == cv.EVENT_RBUTTONUP:
        drawing_right = False


# 이미지 호출
img = cv.imread('./opencv/Ch.01/soccer.jpg')

if img is None:
    print('File Not Found')
    exit()

# 드래그 상태 플래그 설정
drawing_left = False
drawing_right = False

# 윈도우 생성
cv.namedWindow('Draw Circles')

# 마우스 콜백 등록
cv.setMouseCallback('Draw Circles', draw)

# 루프를 돌면서 이미지 표시
while True:
    cv.imshow('Draw Circles', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:   #esc키를 누르면 종료
        break

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyAllWindows()