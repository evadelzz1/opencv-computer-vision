import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from os import path
import time

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
