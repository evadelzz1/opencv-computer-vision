################### Stacking images without Function ################
import cv2
import numpy as np

# img1 = cv2.imread('../Resources/lena.png',0)
# img2 = cv2.imread('../Resources/land.jpg')
img1 = cv2.imread('./data/basketball-player2.png',0)
img2 = cv2.imread('./data/basketball-player2.png')
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
hor= np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow('Vertical', ver)
cv2.imshow('Horizontal', hor)

cv2.waitKey(0)


# https://www.youtube.com/watch?v=Wv0PSs0dmVI&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=6

