import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'bird1.png')
img = cv2.imread(image_path)

# colorspaces
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# visualize image
print("visualize image...")

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_hsv', img_hsv)

# waiting
print("- wait 10 sec")
cv2.waitKey(10000)  # waiting 10sec=10000ms
# cv2.waitKey(0)    # waiting unlimited..
