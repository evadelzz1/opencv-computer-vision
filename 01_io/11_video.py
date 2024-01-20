import os
import cv2
import time

# read video

video_path = os.path.join('.', 'data', 'monkey.mp4')
video = cv2.VideoCapture(video_path)

# visualize video
print("visualize video...")
time_start = time.time()

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(30) # 비디오를 프레임 단위로 읽어서 화면에 표시하고, 
                        # 각 프레임 간의 시간 간격을 조절하기 위해 cv2.waitKey(30)을 사용
                        # 30 밀리초 동안 기다리면서 사용자 입력을 기다리기 때문에 비디오 재생 속도 조절 가능
                        # 숫자를 바꾸면 실행시간을 체크해보면 알 수 있음
        

video.release()
cv2.destroyAllWindows()

time_end = time.time()
print(f"play time : {time_end - time_start}")