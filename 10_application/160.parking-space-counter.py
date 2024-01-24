import cv2
import numpy as np
import matplotlib.pyplot as plt

from util_for_160 import get_parking_spots_bboxes, empty_or_not

mask = './data/mask_crop.png'
video_path = './data/parking_crop_loop.mp4'

mask = cv2.imread(mask, 0)

cap = cv2.VideoCapture(video_path)

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

spots = get_parking_spots_bboxes(connected_components)

ret = True
while ret:
    ret, frame = cap.read()

    for spot in spots:
        x1, y1, w, h = spot

        spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

        spot_status = empty_or_not(spot_crop)
        
        if spot_status:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
        else:
            frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# https://github.com/computervisioneng/parking-space-counter?tab=readme-ov-file
