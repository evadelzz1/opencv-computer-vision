import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'dog1.png')
img = cv2.imread(image_path)

print(f"- image type : {type(img)}")
print(f"- image type : {img.shape}")

# crop image
print("crop image...")
cropped_img = img[120:650, 150:800]  # img[ y: y + h, x: x + w ]

# visualize image
print("visualize image...")
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)

# waiting
print("- wait 10 sec")
cv2.waitKey(10000)  # waiting 10sec=10000ms
# cv2.waitKey(0)    # waiting unlimited..

