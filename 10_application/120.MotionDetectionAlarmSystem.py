import cv2
import imutils

import threading
# import winsound    # for windows

def print_image_info(image):
    print('Image Size : {}'.format(image.shape))
    print('Image dtype : {}'.format(image.dtype))
    print('Image Height : {}'.format(image.shape[0]))
    print('Image Width : {}'.format(image.shape[1]))
    print('Image Pixel Count : {}'.format(image.size))

def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALARM")
        # winsound.Beep(2500, 1000)
        print("\a")
    alarm = False

print("read webcam...")
cap = cv2.VideoCapture(0)    # device(0) : webcam

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width = 500)
# print_image_info(start_frame)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

print("press 's'(switch mode) or 'ESC'")
alarm = False
alarm_mode = False
alarm_counter = 0

while True:
    _, frame = cap.read()        
    frame = imutils.resize(frame, width = 500)
    
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw
        
        print(f"threshold.sum() : {threshold.sum()}")
        if threshold.sum() > 3000000:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        
        cv2.imshow("Webcam", threshold)
    else:
        cv2.imshow("Webcam", frame)
    
    if alarm_counter > 10:
        if not alarm:
            alarm = True
            threading.Thread(target = beep_alarm).start()
            
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('s'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    elif key_pressed == 27:   # ESC key
        break

cap.release()
cv2.destroyAllWindows()


# Reference : https://www.youtube.com/watch?v=QPjPyUJeYYE