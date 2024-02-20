import cv2
import numpy as np
from PIL import ImageGrab

screenshot = ImageGrab.grab()                               # capture a screen
screenshot = np.array(screenshot)                           # pil로 저장된걸 opencv로 바로 사용할 수 없어서 넘파이로 변환을 해줘야 한다.
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)    # 또 opencv는 BRG로 저장하기 때문에 변환해줘야 한다.

cv2.imshow('Screen Capture',screenshot)

# waiting
print("- wait 2 sec")
cv2.waitKey(2000)   # waiting 2sec=2000ms
# cv2.waitKey(0)    # waiting unlimited..

cv2.destroyAllWindows()