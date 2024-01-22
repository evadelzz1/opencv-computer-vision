import cv2
import numpy as np
from PIL import ImageGrab

def captureScreen(bbox=(50,50,690,530)):
    screenshot = ImageGrab.grab(bbox)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

while True:
    timer = cv2.getTickCount()
    img = captureScreen()
    # img = captureScreen(bbox=(50,50,1024,720))
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    cv2.putText(img,'FPS {}'.format(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 230, 20), 2)
    cv2.imshow('Screen Capture',img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
