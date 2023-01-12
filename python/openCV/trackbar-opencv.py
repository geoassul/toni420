import cv2 as cv
#funcion que se otorga al trackbar
def trackbar(x):
    """Trackbar callback function."""
    x = x * 2
    text = f'Trackbar: {x}'
    cv.displayOverlay('window', text, 1000)
    cv.imshow('window', img)
#cargamos la imagen en el objeto img
img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
#creamos la ventana para img
cv.imshow('window', img)
#creamos el trackbar
cv.createTrackbar('toni', 'window', 100, 255, trackbar)
#desplegamos la ventana con el objeto img
cv.waitKey(0)
cv.destroyAllWindows()