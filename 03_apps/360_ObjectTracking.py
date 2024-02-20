import cv2

def ask_for_tracker():  # Tracker Types
    print("""
Welcome! What Tracker API would you like to use? (1~5)"

(1) BOOSTING (AdaBoost)
(2) CSRT     (Channel and Spatial Reliability)
(3) KCF      (Kernelized Correlation Filters)
(4) MOSSE    (Minimum Output Sum of Squared Error)
(5) MIL      (Multiple Instance Learning)
    """)
    choice = input("Please select your tracker: ... ") 

    if choice == '1':
        tracker = cv2.legacy.TrackerBoosting_create()
    elif choice == '2':
        tracker = cv2.TrackerCSRT_create()
    elif choice == '3':
        tracker = cv2.TrackerKCF_create()
    elif choice == '4':
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif choice == '5':
        tracker = cv2.TrackerMIL_create()
    else:
        quit(1)

    return tracker

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


tracker = ask_for_tracker() 

video_src = 0 # 비디오 파일과 카메라 선택
video_src = "./data/traffic1.mp4"

cap = cv2.VideoCapture(video_src)

# TRACKER INITIALIZATION
success, frame = cap.read()
bbox = cv2.selectROI("Tracking",frame, False)

tracker.init(frame, bbox)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    # trackerName = tracker.__class__.__name__
    # cv2.putText(img, "tracker:"+trackerName, (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
    
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break


# https://www.youtube.com/watch?v=1FJWXOO1SRI
