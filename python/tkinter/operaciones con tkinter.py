from tkinter import *

def operacion():
    numero = num.get()
    if opcion.get() == 1:
        total = numero * 10
    elif opcion.get() == 2:
        total = numero * 20
    elif opcion.get() == 3:
        total = numero * 30
    elif opcion.get() == 4:
        total = numero * 40
    elif opcion.get() == 5:
        total = numero * 50
    else:
        total = numero * numero
    print('el total de la operacion es: ' + str(total))

ventana = Tk()
opcion = IntVar()
num = IntVar()
ventana.title('RadioButton en Tkinter')
ventana.geometry('400x300')
etiqueta1 = Label(ventana, text='Escribe el numero: ').place(x=20, y=20)
CajaNumero = Entry(ventana, textvariable=num).place(x=150, y=20)
etiqueta2 = Label(ventana, text='Escribe tu opcion: ').place(x=20, y=50)
x10 = Radiobutton(ventana, text="X10", value=1, variable=opcion).place(x=20, y=80)
x10 = Radiobutton(ventana, text="X20", value=2, variable=opcion).place(x=80, y=80)
x10 = Radiobutton(ventana, text="X30", value=3, variable=opcion).place(x=140, y=80)
x10 = Radiobutton(ventana, text="X40", value=4, variable=opcion).place(x=20, y=110)
x10 = Radiobutton(ventana, text="X50", value=5, variable=opcion).place(x=80, y=110)
cuadrado = Radiobutton(ventana, text='cuadrado', value=6, variable=opcion).place(x=140,y=110)
boton = Button(ventana, text='Realiza operacion', command=operacion).place(x=20, y=140)
ventana.mainloop()














