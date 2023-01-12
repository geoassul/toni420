from tkinter import *

ventana = Tk()
ventana.title('hola toni')
ventana.geometry('400x200')
button = Button(ventana, text='minimizar',fg='yellow',command=ventana.iconify).place(x=30, y=37)
button2 = Button(ventana, text='dame click para saludar',fg='green',command = lambda: print('hola mundo')).place(x=30, y=75)
etiqueta = Label(ventana, text='primer texto').place(x= 250, y=37)
etqueta2 = Label(ventana, text='segundo texto').place(x=250, y=75)
ventana.mainloop()