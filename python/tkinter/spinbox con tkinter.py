from tkinter import *

def obtener():
    print(valor.get())
    
ventana = Tk()
valor = StringVar()
ventana.title('uso del spinbox con tkinter')
ventana.geometry('600x400')
etiqueta1 = Label(ventana,text='ejemplo1').place(x=20,y=20)
etiqueta2 = Label(ventana,text='ejemplo2').place(x=20,y=80)
combo = Spinbox(ventana, values=('123456')).place(x=20,y=50)
combo2 = Spinbox(ventana, from_=1, to=10, textvariable=valor).place(x=20,y=110)
boton = Button(ventana,text='obtener valor spinbox',command=obtener).place(x=80,y=140)
mainloop()