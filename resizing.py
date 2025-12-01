import os
import cv2

img = cv2.imread((os.path.join('.', 'data','t.png')))
print(img.shape)

resize_image = cv2.resize(img,(1000,1000))
print(resize_image.shape)
cv2.imshow('image',resize_image)
cv2.waitKey(0)

