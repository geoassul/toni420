import cv2 as cv
import numpy as np
def hue(x):
    img[:, :, 1] = x
    rgb = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    cv.imshow('window', rgb)
def saturation(x):
    img[:, :, 2] = x
    rgb = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    cv.imshow('window', rgb)
img = np.zeros((180, 256, 3), dtype=np.uint8)
for i in range(180):
    img[i, :, 0] = i
cv.imshow('window', img)
cv.createTrackbar('hue', 'window', 0, 255,hue)
cv.createTrackbar('saturation', 'window', 0, 255, saturation)
cv.waitKey(0)
cv.destroyAllWindows()