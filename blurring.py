import os
import cv2

img = cv2.imread((os.path.join('.','data','t.png')))
imf = cv2.blur(img,(7,7)) # -> marimea nucleului, mai exact cu cate elemente face average pentru un pixel cu ajutorul elemtelor din jur
cv2.waitKey(0)

imgf = cv2.GaussianBlur(img,(7,7),3)
immm = cv2.medianBlur(img,7)
cv2.imshow('image',img)
cv2.imshow('image_blur',imf)
cv2.imshow('image_gaussian',imgf)
cv2.imshow('image_median',immm) #median_blur sterge zgomotul din fundal
cv2.waitKey(0)

