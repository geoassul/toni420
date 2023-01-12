import cv2 as cv
import numpy as np
import time
import os
import urllib.request

url='http://192.168.0.118/cam-lo.jpg'
cv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
face_detector = os.path.join(cv_base_dir, 'data/haarcascade_upperbody.xml')
face_detector = cv.CascadeClassifier(face_detector)
RED = (0, 0, 255)
#path = 'cascades/haarcascade_frontalface_default.xml'
#face_detector = cv.CascadeClassifier(path)
def detect():
    rects = face_detector.detectMultiScale(gray_s,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) > 1 :
        print(f'found {len(rects)} face(s)')
    for rect in rects:
       cv.rectangle(gray_s,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]), RED, 2)
#cap = cv.VideoCapture((http://192.168.1.111/cam-hi.jpg))
#t0 = time.time()
#M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
#size = (400,300)
while True:
# Capture frame-by-frame
    #time.sleep(0.110)
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv.imdecode(imgnp,-1)
    #ret, frame = cap.read()
    gray_s = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gray_s = cv.warpAffine(gray, M, size)
    detect()
    cv.imshow('window', gray_s)
    #cv.displayOverlay('window', f'time={t-t0:.3f}')
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
#cap.release()
cv.destroyAllWindows()
