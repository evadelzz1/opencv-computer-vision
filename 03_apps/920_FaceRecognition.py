import cv2
import threading
from deepface import DeepFace

print("read reference_img...")
reference_img = cv2.imread("./data/reference.png")
# cv2.imshow('frame', reference_img)
# cv2.waitKey(0)

print("read webcam...")
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(), )).start()
            except ValueError:
                pass
        
        counter += 1
    
        if face_match:
            screenText = "MATCH"
        else:
            screenText = "NO MATCH"
        
        cv2.putText(frame, screenText, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        
        cv2.imshow('frame', frame)
        key = cv2.waitKey(30)
        if key == 27:   # ESC key
            break
    
cap.release()
cv2.destroyAllWindows()

