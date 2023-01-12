# Color histogram
from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread('bob-marley.jpg')
chans = cv.split(img)
colors = 'b', 'g', 'r'
lines = '-.','--',':'
plt.figure()
plt.title('Flattened color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
acc = 0
for (chan, color,line) in zip(chans, colors,lines):
    acc = acc + 1
    hist = cv.calcHist([chan], [0], None, [256], [0, 255])
    plt.plot(hist, color=color,linestyle=line)
    plt.xlim([0, 256])
    plt.ylim([0, 2000])
    print(color,chan.shape)
print(acc)
plt.show()
cv.waitKey(0)