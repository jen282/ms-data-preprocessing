import cv2 as cv
import sys

# 전역 변수 선언
drawing = False
start_point = (-1, -1)
end_point = (-1, -1)

# 마우스 콜백 함수 정의
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_point, end_point, img, temp_img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)
        temp_img = img.copy()
        print('Left Button Down')
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x,y)
            temp_img = img.copy()
            cv.rectangle(temp_img, start_point, end_point, (255, 0, 0), 2)
            print('Dragging')
        
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv.rectangle(img, start_point, end_point, (255, 0, 0), 2)
        temp_img = img.copy()
        print('Left Button Up')


img = cv.imread('./opencv/Ch.02/girl.jpg')

if img is None:
    sys.exit('File Not Found')

temp_img = img.copy()

# 윈도우 생성
cv.namedWindow('Draw Rectangle')

# 마우스 콜백 등록
cv.setMouseCallback('Draw Rectangle', draw_rectangle)

# 루프를 돌면서 이미지 표시
while True:
    cv.imshow('Draw Rectangle', temp_img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:   #esc키를 누르면 종료
        break

# 열려 있는 모든 OpenCV 창 닫기 
cv.destroyAllWindows()