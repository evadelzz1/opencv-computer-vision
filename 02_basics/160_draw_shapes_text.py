import os
import cv2

# read image
print("read image...")
img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))

print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

# circle
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

cv2.imshow('Image', img)

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()