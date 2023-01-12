import cv2 as cv
import numpy as np
img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)#metodo para la escala de la img.
img1 = cv.Laplacian(img, 8)
cv.imshow('window', np.hstack([img, img1]))
cv.waitKey(0)
cv.destroyAllWindows()