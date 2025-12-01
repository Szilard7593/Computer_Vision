import os
import cv2

img = cv2.imread((os.path.join('.','data','t.png')))
ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

img_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('image',img)
cv2.imshow('image_binary',thresh)
cv2.waitKey(0)