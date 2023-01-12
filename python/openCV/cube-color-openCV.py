import cv2 as cv
import numpy as np
def funcion(parametro):
    img[:, :, 2] = parametro
    cv.imshow('window', img)
img = np.zeros((256, 256, 3), dtype=np.uint8)
for i in range(256):
    img[i, :, 1] = i
    img[:, i, 0] = i
cv.imshow('window', img)
cv.createTrackbar('red', 'window', 0, 255, funcion)
cv.waitKey(0)
cv.destroyAllWindows()