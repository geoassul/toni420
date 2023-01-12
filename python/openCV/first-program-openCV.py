import cv2 as cv
import numpy

class App:
    
    global help
    wins = []
    win = None
    
    def __init__(self):
        cv.namedWindow('tototoni')
        self.shortcuts = { 'h': help,'i': self.inspect}
        
    def run(self):
        key = ''
        while key != 'q':
            k = cv.waitKey(0)
            key = chr(k)
            print(k,key)
            
        cv.destroyAllWindows()
    def inspect(self):
        print('--- INSPECT ---')
        #print('App.wins', App.wins)
        #print('App.win', App.win)
        
class Window:
    
    def __init__(self, win=None, img=None):
        App.wins.append(self)
        App.win = self
        self.objs = []
        self.obj = None
        if img==None:
            img = np.zeros((200, 600, 3), np.uint8)
        if win == None:
            win = 'window' + str(App.win_id)
        App.win_id += 1
        self.win = win
        self.img = img
        self.img0 = img.copy()
        cv.imshow(win, img)
        
if __name__ == '__main__':
    App().run()
    window()

