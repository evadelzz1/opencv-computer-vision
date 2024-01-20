import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'cow-salt-peper.png')
img = cv2.imread(image_path)
                              
# blur
k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)

cv2.moveWindow('img_blur', 200,200)
cv2.moveWindow('img_gaussian_blur', 400, 400)
cv2.moveWindow('img_median_blur', 600, 600)

# waiting
print("### if you want exit, press a 'q' key ###")
while(True):
    if cv2.waitKey(100) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
        cv2.destroyAllWindows()
        break
    
