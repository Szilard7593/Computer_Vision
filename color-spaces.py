import os
import cv2

img = cv2.imread((os.path.join('.','data','t.png')))
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gra = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('image',img_hsv)
cv2.waitKey(0)