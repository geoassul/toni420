import cv2 as cv
img = cv.imread('messi.jpg')
img[250:300, 50:550] = (0, 255, 0)
face = img[40:240, 240:360]
img[0:200, 0:120] = face
cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()