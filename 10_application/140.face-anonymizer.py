import os
import cv2
import mediapipe as mp

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'face-anonymizer-sample.png')
img = cv2.imread(image_path)

H, W, _ = img.shape

# detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    print(out.detections)
    
    for detection in out.detections:
        location_data = detection.location_data
        bbox = location_data.relative_bounding_box

        x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

        x1 = int(x1 * W)
        y1 = int(y1 * H)
        w = int(w * W)
        h = int(h * H)
        
        img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)

        # blur faces
        img = cv2.blur(img, (10, 10))

    cv2.imshow('img', img)

    # waiting
    print("### if you want exit, press a 'q' key ###")
    while(True):
        if cv2.waitKey(100) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
            
            # save image
            cv2.imwrite(os.path.join('.', 'output', 'output.png'), img)
            print("check a output file.")
            
            cv2.destroyAllWindows()
            break


# https://github.com/computervisioneng/face-anonymizer-ptyhon