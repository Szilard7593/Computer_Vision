import os
import cv2

img = cv2.imread((os.path.join('.','data','t.png')))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray,80,255, cv2.THRESH_BINARY)
ftc = cv2.blur(thresh,(50,50))

adaptive_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,20)
#cv2.imshow('image',img)
#cv2.imshow('image_gray',img_gray)
cv2.imshow('image_binary',adaptive_thresh)
cv2.imshow('image_blur',thresh)
cv2.waitKey(0)