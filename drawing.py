import os
import cv2

img = cv2.imread((os.path.join('.', 'data', 't.png')))

#line
img_l = cv2.line(img,(0,2),(3,500),(0,255,0),3)

#rectangle
img_r = cv2.rectangle(img,(0,0),(200,200),(0,255,0),3)

#circle
cv2.circle(img,(200,200),50,(0,0,255),3)

#text
cv2.putText(img,'Hello World!',(10,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

cv2.imshow('image',img)
cv2.waitKey(0)

