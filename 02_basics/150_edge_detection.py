import os
import cv2
import numpy as np

# read image
print("read image...")
img = cv2.imread(os.path.join('.', 'data', 'basketball-player1.png'))
                    
img_edge = cv2.Canny(img, 100, 200)
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)

cv2.moveWindow('img_edge', 200,200) 
cv2.moveWindow('img_edge_d', 400,400) 
cv2.moveWindow('img_edge_e', 600,600) 

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()