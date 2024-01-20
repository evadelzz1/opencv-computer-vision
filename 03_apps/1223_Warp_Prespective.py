import cv2
import numpy as np

path = "data/cards.png"
img =  cv2.imread(path)

width, height = 400,500
pts1 = np.float32([[235,465],[615,390],[330,1025],[750,930]])
print(pts1)

# cv2.circle(img,(int(pts1[0][0]),int(pts1[0][1])),15,(0,255,0),cv2.FILLED) # only 1 point
for x in range (0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),15,(0,255,0),cv2.FILLED)

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
print(pts2)

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original Image ", img)
cv2.imshow("Output Image ", imgOutput)
cv2.waitKey(0)

# https://www.youtube.com/watch?v=Tm_7fGolVGE&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=7
