import cv2 as cv
def mouse(event, x, y, flags, param):
    print(param)# devuelve un None
    text = f'Mouse at ({x}, {y}), flags={flags}, param={param}'
    cv.displayOverlay('window', text, 1000)
    if flags == 1:
        img[y][x] = [0, 0, 255] # img[x,y] tambien se puede
        cv.imshow('window', img)
        print(flags) #devuelve un int cada que el mouse esta siendo manipulad
        print(event) #en caso del event, retorna un int cada que se usan los botones del mouse
img = cv.imread('messi.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)
cv.waitKey(0)
cv.destroyAllWindows()