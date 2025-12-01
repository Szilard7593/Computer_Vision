import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype="uint8")
    upperLimit = np.array(upperLimit, dtype="uint8")

    return lowerLimit, upperLimit

color = [0,255,255]
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLmit, upperLimit = get_limits(color)

    mask = cv2.inRange(hsv_image, lowerLmit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    cv2.imshow("frame", mask)

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

    frame = cv2.flip(frame, 1)
    cv2.imshow("frame", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
