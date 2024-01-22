import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from os import path

# https://www.youtube.com/watch?v=6DjFscX4I_c

if path.exists('/usr/local/bin/tesseract'):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
elif path.exists('/opt/homebrew/bin/tesseract'):
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
else:
    print('check a tesseract binary')
    quit(1)

img = cv2.imread('data/textsimple.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

##############################################
##### Image to String   ######
##############################################
print(pytesseract.image_to_string(img))

##############################################
##### Detecting ONLY Digits  ######
##############################################
hImg, wImg,_ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

#############################################
#### View Image  ######
#############################################
cv2.imshow('Image', img)

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()


#############################################
# Install tesseract on MacOS
#############################################

# brew install imagemagick
# brew install tesseract
# brew install tesseract-lang
# tesseract --list-langs

# which tesseract
# --> /opt/homebrew/bin/tesseract

# pip install pytesseract
# pip install Pillow
