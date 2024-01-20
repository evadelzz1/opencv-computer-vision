import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'dog1.png')
img = cv2.imread(image_path)

# resize image
print("resize image...")
resized_img = cv2.resize(img, (500, 500))

print(f"- ASIS image shape : {img.shape}")
print(f"- TOBE image shape : {resized_img.shape}")

# visualize image
print("visualize image...")
cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)

# waiting
print("- wait 5 sec")
cv2.waitKey(5000)  # waiting 5sec=5000ms
# cv2.waitKey(0)    # waiting unlimited..