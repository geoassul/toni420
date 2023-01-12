# Le damos un nombre a la libreria de openCV
import cv2 as cv 
# le otorgamos a la variable la imagen
img = cv.imread('messi.jpeg') 
#mostramos la ventana donde se insertara la img
cv.imshow('cosa',img)
#muestra la img y el parametro indica en ms el uso de botones en la ventana
cv.waitKey(10000)
#destruye todas la ventanas en el programa
cv.destroyAllWindows