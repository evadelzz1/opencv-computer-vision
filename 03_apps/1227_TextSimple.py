import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

# https://www.youtube.com/watch?v=6DjFscX4I_c

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
img = cv2.imread('data/textsimple.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))

#############################################
#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

cv2.imshow('img', img)
cv2.waitKey(0)

# brew install tesseract
# pip install pytesseract
