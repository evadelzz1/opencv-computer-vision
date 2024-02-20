import os
import cv2

# read image
print("read image...")
image_path = './data/dog1.png'
# image_path = os.path.join('.', 'data', 'dog1.png')
img = cv2.imread(image_path)

# resize image
print("resize image...")
resized_img = cv2.resize(img, (500, 500))

print(f"- ASIS image shape : {img.shape}")
print(f"- TOBE image shape : {resized_img.shape}")

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('resized_img', resized_img)

cv2.moveWindow('resized_img', 600,400)

# waiting
print("- wait 2 sec")
cv2.waitKey(2000)   # waiting 2sec=2000ms
# cv2.waitKey(0)    # waiting unlimited..

cv2.destroyAllWindows()