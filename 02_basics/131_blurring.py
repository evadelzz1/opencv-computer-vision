
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "data/basketball-player2.png"
img =  cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel , iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

cv2.imshow("Lena",img)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("Img Blur",imgBlur)
cv2.imshow("Img Canny",imgCanny)
cv2.imshow("Img Dialation",imgDilation)
cv2.imshow("Img Erosion",imgEroded)

cv2.moveWindow('GrayScale', 100,100)
cv2.moveWindow('Img Blur', 200,200)
cv2.moveWindow('Img Canny', 300,300)
cv2.moveWindow('Img Dialation', 400,400)
cv2.moveWindow('Img Erosion', 500,500)

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()