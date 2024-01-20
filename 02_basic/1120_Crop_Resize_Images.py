import cv2

path = "data/dog1.png"
img  = cv2.imread(path)
print(img.shape)

width, height = 650 , 800
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped = img[120:650, 150:800]  # img[ y: y + h, x: x + w ]
imCropResize  = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))

cv2.imshow("original",img)
cv2.imshow("Resized",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.imshow("Cropped_Resized",imCropResize)

cv2.moveWindow('Resized', 200,200)
cv2.moveWindow('Cropped', 400,400)
cv2.moveWindow('Cropped_Resized', 600,600)

cv2.waitKey(0)
