import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('./data/QRCodeTest1.png')

code=decode(img)
print(code)

for barcode in decode(img):
    print(barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)




##########################################################################################
# Install QRCode on MacOS
#
# brew install bar
# brew install zbar
#
#
# # Error : (MacBook M1):raise ImportError('Unable to find zbar shared library')
#
# mkdir ~/lib
# ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
#
# # https://stackoverflow.com/questions/71984213/macbook-m1raise-importerrorunable-to-find-zbar-shared-library-importerror


##########################################################################################
# https://www.youtube.com/watch?v=SrZuwM705yE&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=17
