import os
import cv2
import numpy as np

img = cv2.imread((os.path.join('.','data','b.png')))

img_edge = cv2.Canny(img,100,200)

img_edge_d = cv2.dilate(img_edge,np.ones((5,5),np.uint8))

img_edge_e = cv2.erode(img_edge_d,np.ones((5,5),np.uint8))




cv2.imshow('image',img_edge_d)
cv2.waitKey(0)