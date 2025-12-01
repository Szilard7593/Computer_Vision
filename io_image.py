import os
import cv2

#citirea unei imagini
#image_path = os.path.join('.', 'data','t.png')
#imag = cv2.imread(image_path)

#scrierea unei imagini
#cv2.imwrite(os.path.join('.', 'data','t_out.png'),imag)

#vizualizarea unei imagini
#cv2.imshow('image',imag)
#cv2.waitKey(0) #(0) -> cat timp tinem pop-ul deschis

#deschiderea unui video
"""
video_path = os.path.join('.', 'data','video.mp4')
video = cv2.VideoCapture(video_path)

#vizualizarea unui video
ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('video',frame)
        cv2.waitKey(40) #in milisecunde

video.release()
cv2.destroyAllWindows()
"""

camera = cv2.VideoCapture(0) #(numar:int) <- numarul camerei pe care vrem sa o accesam

while True:
    ret, frame = camera.read()
    cv2.imshow('camera',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

camera.release()
