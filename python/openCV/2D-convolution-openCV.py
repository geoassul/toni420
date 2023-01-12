# convolution
import cv2 as cv
import numpy as np
kernel = np.ones((5, 5), 'uint8')/25
def trackbar(x):
    """Trackbar callback function."""
    d = 2*x + 1
    kernel = np.ones((d, d), 'uint8')/(d**2)
    img1 = cv.filter2D(img, -1, kernel)
    cv.imshow('window', np.hstack([img, img1]))
    text = f'kernel=({d}x{d})'
    cv.displayOverlay('window', text)
img = cv.imread('bob-marley.jpg')
trackbar(2)
cv.createTrackbar('threshold', 'window', 2, 7, trackbar)
cv.waitKey(0)
cv.destroyAllWindows()