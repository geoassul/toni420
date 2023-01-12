import cv2 as cv
import numpy as np
import time
import os
import urllib.request
url='http://192.168.1.111/cam-lo.jpg'
a = 0
while True:
    time.sleep(0.16)
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv.imdecode(imgnp,-1)
    cv.imshow('window', frame)
    cv.waitKey(166)
    print(imgnp.dtype)
    print(frame.shape)
    print(bytearray(img_resp.read()))