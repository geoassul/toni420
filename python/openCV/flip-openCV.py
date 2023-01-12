import cv2 as cv
img = cv.imread('bob-marley.jpg')
cv.imshow('window', img)
while True:
    k = cv.waitKey(0)
    if k == ord('q'):
        break
    elif k == ord('v'):  #flip around the x axis
        img = cv.flip(img, 0)
        print('quefue mano')
    elif k == ord('h'): #flip around the y axis
        img = cv.flip(img, 1)
    elif k == ord('j'): #flip around the both axes
        img = cv.flip(img, -1)
    cv.imshow('window', img)
cv.destroyAllWindows()