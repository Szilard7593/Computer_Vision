import cv2
import mediapipe as mp
import argparse

#citim imaginea
img_path = './data/OIP.jpg'
img = cv2.imread(img_path)
H, W, _ = img.shape

#detectsm fata
mp_face_detection = mp.solutions.face_detection
'''
with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    #print(out.detections)
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int( w * W)
            h = int( h * H)

            img = cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 10)
            #BLUR
            img[y1:y1+h,x1:x1+w,:]= cv2.blur(img[y1:y1+h,x1:x1+w,:],(2,20))


    cv2.imwrite('./data/OIP_out.jpg',img)
'''


def process_image(img,face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    # print(out.detections)
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)
            # BLUR
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (20, 20))
    return img

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        frame = process_image(frame, face_detection)

        cv2.imshow('frame', frame)
        cv2.waitKey(40)
        ret, frame = camera.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()