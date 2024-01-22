import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'bird3.png')
img = cv2.imread(image_path)

# colorspaces
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# visualize image
print("visualize image...")

cv2.imshow('original', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_hsv', img_hsv)

cv2.moveWindow('img_gray', 100,100)
cv2.moveWindow('img_rgb', 200,200)
cv2.moveWindow('img_hsv', 300,300)

# waiting
print("- wait 2 sec")
cv2.waitKey(2000)   # waiting 2sec=2000ms
# cv2.waitKey(0)    # waiting unlimited..

cv2.destroyAllWindows()