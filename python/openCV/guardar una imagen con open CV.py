import cv2 as cv
#creamos la imagen
img = cv.imread('kdk.jpeg')
cv.imshow('window', img)
#creamos un nuevo archivo con la imagen cargada
cv.imwrite('kdk.png', img)#nombre del archivo y variable que se cargar`a
#metodo para poner a escala de grises una imagen
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#creamos un nuevo archivo de la imagen con escala de grises
cv.imwrite('knk_gray.png', gray)
#mostrar ventana
cv.waitKey(0)
cv.destroyAllWindows()