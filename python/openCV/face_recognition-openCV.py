import cv2 as cv
import os

cv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
haar_model = os.path.join(cv_base_dir, 'data/haarcascade_frontalface_default.xml')

RED = (0, 0, 255)
img = cv.imread('messi.jpg')
img = cv.resize(img, None, fx=0.7, fy=0.7, interpolation=cv.INTER_CUBIC)
cv.imshow('window', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detector = cv.CascadeClassifier(haar_model)
face_rects = face_detector.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv.CASCADE_SCALE_IMAGE)
print(f'found {len(face_rects)} face(s)')


for rect in face_rects:
    cv.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]), RED, 2)
    
cv.imshow('window', img)
cv.waitKey(0)