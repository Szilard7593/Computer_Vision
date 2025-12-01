import os
import cv2

img = cv2.imread((os.path.join('.','data','t.png')))
print(img.shape)
crop_img = img[100:400,100:400] #imaginile sunt nd-array-uri deci acessam numai partea care ne trebuie la crop-uri
cv2.imshow('image',crop_img)
cv2.waitKey(0)



