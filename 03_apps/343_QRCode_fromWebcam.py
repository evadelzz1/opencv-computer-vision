import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('./data/QRBarTest.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)



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
