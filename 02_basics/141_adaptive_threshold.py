import os
import cv2

# read image
print("read image...")
img = cv2.imread(os.path.join('.', 'data', 'handwritten.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
ret, simple_thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, simple_thresh3 = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)

# adaptive threshold
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('simple_thresh', simple_thresh)
cv2.imshow('simple_thresh2', simple_thresh2)
cv2.imshow('simple_thresh3', simple_thresh3)
cv2.imshow('adaptive_thresh', adaptive_thresh)

cv2.moveWindow('simple_thresh', 200,200)
cv2.moveWindow('simple_thresh2', 300,300)
cv2.moveWindow('simple_thresh3', 400,400)
cv2.moveWindow('adaptive_thresh', 500,500) 

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()
