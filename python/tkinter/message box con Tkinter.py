from tkinter import *
from tkinter import messagebox

def obtener():
    messagebox.showinfo('mensajon de tonifon','usuario '+valor2.get()+' seleccionaste: '+valor.get())
    print('mensaje','usuario',valor2.get(),'seleccionaste:',valor.get())

ventana = Tk()
valor = StringVar()
valor2 = StringVar()
ventana.title('uso de spinbox con Tkinter')
ventana.geometry('400x300')
etiqueta = Label(ventana, text='ejemplo 2 de spinbox').place(x=20,y=20)
combo = Spinbox(ventana, values=('uno','dos','tres','cuatro','cinco'),textvariable=valor2).place(x=20,y=50)
etiqueta2 = Label(ventana, text='ejemplo2 de spinbox').place(x=20,y=80)
combo2 = Spinbox(ventana, from_=1,to=10,textvariable=valor).place(x=20,y=110)
boton = Button(ventana,text='obtener valor de spinbox',command=obtener).place(x=80,y=140)
mainloop()