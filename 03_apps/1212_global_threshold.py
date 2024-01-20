import os
import cv2

# read image
print("read image...")
img = cv2.imread(os.path.join('.', 'data', 'bear.jpg'))

# 영상의 이진화 - Binarization
#
# 영상의 이진화는 영상의 픽셀 값을 0 또는 255(1)로 만드는 연산입니다.
# 0은 검정색, 255는 흰색을 의미합니다.
#
# 이진화를 하는 이유는 1. 배경과 객체를 구분, 2. 관심 영역과 비관심 영역 구분 입니다.
# 마스크 영상도 이진 영상의 한 형태라고 볼 수 있습니다.

# 이미지 변환 : 그레이스케일
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold(임계값) 설정
# cv2.threshold(src, thresh, maxval, type, dst=None) -> retval, dst
#
# • src: 입력 영상. 다채널, 8비트 또는 32비트 실수형
# • thresh: 사용자 지정 임계값
# • maxval: cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 방법 사용 시 최댓값. 보통 255로 지정.
# • type: cv2.THRESH_ 로 시작하는 플래그. 임계값 함수 동작 지정 또는 자동 임계값 결정 방법 지정
# • retval: 사용된 임계값
# • dst: 출력 영상. src와 동일 크기, 동일 타입, 같은 채널 수
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh2 = cv2.blur(thresh, (10, 10))
ret, thresh2 = cv2.threshold(thresh2, 80, 255, cv2.THRESH_BINARY)

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh2', thresh2)

cv2.moveWindow('img_gray', 200,200) # 창 위치 변경
cv2.moveWindow('thresh', 400,400) # 창 위치 변경
cv2.moveWindow('thresh2', 600,600) 

# waiting
print("### if you want exit, press a 'q' key ###")
while(True):
    if cv2.waitKey(100) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
        cv2.destroyAllWindows()
        break