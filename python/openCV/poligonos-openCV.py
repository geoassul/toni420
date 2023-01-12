import cv2 as cv
import numpy as np
RED = (0, 0, 255)
pts =  [(50, 50), (300, 190), (400, 10),(16,120)]
img = np.zeros((200, 500, 3), np.uint8)
cv.polylines(img, np.array([pts]),True, RED, 5)
cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()