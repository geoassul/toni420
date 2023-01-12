import cv2 as cv
import numpy as np
from draw import *

def draw(x):
    global p0, p1
    d = cv.getTrackbarPos('thickness', 'window')
    d = -1 if d==0 else d
    i = cv.getTrackbarPos('color', 'window')
    color = colors[i]
    img[:] = img0
    cv.rectangle(img, p0, p1, color, d)
    cv.imshow('window', img)
    text = f'color={color}, thickness={d}'
    cv.displayOverlay('window', text)
    #print(f'{x}')
    
def mouse(event, x, y, flags, param):
    global p0, p1
    if event == cv.EVENT_LBUTTONDOWN:
        img0[:] = img
        p0 = x, y
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        p1 = x, y
    draw(12312321312)
    
cv.setMouseCallback('window', mouse)
cv.createTrackbar('color', 'window', 0, 6, draw)
cv.createTrackbar('thickness', 'window', 0, 10, draw)

cv.waitKey(0)
cv.destroyAllWindows()