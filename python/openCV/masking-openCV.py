"""Masking."""
import cv2 as cv
import numpy as np
img = cv.imread('bob-marley.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_NEAREST)
mask = np.zeros(img.shape[:2], dtype='uint8')
cv.circle(mask, (60, 53), 30, 255, -1)#src,sizesrc,center,radio,color,filled
masked = cv.bitwise_and(img, img, mask=mask)
img2 = np.hstack([img, masked])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()