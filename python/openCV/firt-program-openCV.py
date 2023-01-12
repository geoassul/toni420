import cv2 as cv
import numpy

def help():
        print('--- HELP ---')
class App:
    def __init__(self):
        cv.namedWindow('totototoni')
        self.shortcuts = { 'h': help,
                           'i': self.inspect,}
    def key(self, k):
        if k in self.shortcuts: self.shortcuts[k]()
    def help():
        print('--- HELP ---')
    def inspect(self):
        print('--- INSPECT ---')
        print('App.wins', App.wins)
        print('App.win', App.win)
            
    def run(self):
        key = ''
        while key != 'q':
            k = cv.waitKey(0)
            key = chr(k)
            print(k,key)
            
        cv.destroyAllWindows()

        
if __name__ == '__main__':
    App().run()
