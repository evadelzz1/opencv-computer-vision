import time
from PIL import ImageGrab

for i in range(1, 6):
    print(f"Capture ... {i}/5")
    screenshot = ImageGrab.grab()   # capture a screen
    # screenshot = np.array(screenshot)                           # pil로 저장된걸 opencv로 바로 사용할 수 없어서 넘파이로 변환을 해줘야 한다.
    # screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)    # 또 opencv는 BRG로 저장하기 때문에 변환해줘야 한다.
    screenshot.save("./data/zScreenCapture{}.png".format(i))
    print(">> Captured : ./data/zScreenCapture{}.png".format(i))
    time.sleep(1)
