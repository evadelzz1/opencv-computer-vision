import cv2
import numpy as np
from pyzbar.pyzbar import decode

with open('./data/AuthWithQRCode_AuthorizedDataFile.txt') as f:
    authorizedDataList = f.read().splitlines()

imgLists = ['./data/QR-ID-111111.png', './data/QR-ID-111113.png', './data/QR-ID-211113.png', './data/QR-ID-222111.png']

for imgList in imgLists:
    img = cv2.imread(imgList)
    code=decode(img)
    print('#' * 50)
    # print(f"Image : {imgList}")
    # print(f"Decode Image : {code}")
    
    for barcode in decode(img):
        # print(barcode.data)
        readData = barcode.data.decode('utf-8')
        print(readData)

        if readData in authorizedDataList:
            checkOutput = 'Authorized'
        else:
            checkOutput = 'Un-Authorized'
    
    print(checkOutput)             


