import cv2 as cv

#cargamos las imagenes en el programa
img = cv.imread('messi.jpg')

#cambiamos de color la imagen 'messi.jpg'
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('messi.png', img)
cv.imwrite('messi_gray.png',gray)
#creamos las ventanas para las imagenes cargadas
cv.imshow('toni',gray) 
cv.imshow('totoni',img)
#mostramos las imagenes
cv.waitKey(0)
cv.destroyAllWindows()
