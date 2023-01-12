import cv2 as cv
file = 'messi.jpg' #nombre del archivo
img = cv.imread(file, cv.IMREAD_COLOR) #carga el archivo con su color especifico 
cv.imshow('window', img) #crea la ventana
text = f'file name: {file}\n\
width: {img.shape[1]}\n\
height: {img.shape[0]}\n\
channels: {img.shape[2]}'
cv.displayOverlay('window', text) #overlay con el texto
cv.waitKey(0) #desplega la ventana
cv.destroyAllWindows() # destruye todas la imagenes