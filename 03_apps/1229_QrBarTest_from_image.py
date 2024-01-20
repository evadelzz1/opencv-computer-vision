import cv2
import numpy as np
from pyzbar.pyzbar import decode

# brew install bar
# brew install zbar

img = cv2.imread('./data/QRBarTest.png')

code=decode(img)
print(code)

for barcode in decode(img):
    print(barcode.data)

for barcode in decode(img):
    print(barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)


# https://www.youtube.com/watch?v=SrZuwM705yE&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=17

