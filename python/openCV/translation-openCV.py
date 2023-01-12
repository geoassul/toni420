import cv2 as cv
import numpy as np
M = np.float(0)
def rotar(event, x, y, flags, param):
    if event == 0:
        M = np.float32([[1, 0, x], [0, 1, y]])
        rotated = cv.warpAffine(img, M, (w, h))
        cv.imshow('window', rotated)
    return M
img = cv.imread('bob-marley.jpg')
h, w = img.shape[:2]
center = w//2, h//2
cv.imshow('window', img)
cv.createTrackbar('jeje','window',0,180, lambda x: print(x+1))
cv.setMouseCallback('window', rotar)
cv.waitKey(0)
cv.destroyAllWindows()