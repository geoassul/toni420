from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread('bob-marley.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.ylim([0, 2090])
plt.show()
cv.waitKey(0)