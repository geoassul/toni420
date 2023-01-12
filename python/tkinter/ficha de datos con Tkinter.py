from tkinter import *

def saludo():
    print('Hola!',nombre.get(),apellidop.get(),apellidom.get(),'\ntu edad es:',edad.get(),'\ntu sexo es:',sexo.get())
ventana = Tk()
nombre = StringVar()
apellidop = StringVar()
apellidom = StringVar()
edad = IntVar()
sexo = BooleanVar()
nombre.set('escribe tu nombre')
apellidop.set('apellido paterno')
apellidom.set('apellido materno')
edad.set('¿Que edad tienes?')
#sexo.set('¿Cual es tu sexo')
ventana.title('Entradas en Tkinter')
ventana.geometry('600x400')
etiqueta1 = Label(ventana,text='Escribe tu nombre').place(x=10, y=10)
nombreCaja = Entry(ventana, textvariable=nombre).place(x=220, y=10)
etiqueta2 = Label(ventana,text='escribe tu apellido paterno').place(x=10, y=40)
apellidopCaja = Entry(ventana, textvariable=apellidop).place(x=220, y=40)
etiqueta3 = Label(ventana,text='Escribe tu apellido materno').place(x=10, y=70)
apellidomCaja = Entry(ventana, textvariable=apellidom).place(x=220, y=70)
etiqueta4 = Label(ventana,text='Escribe tu edad').place(x=10, y=100)
edadCaja = Entry(ventana,textvariable=edad).place(x=220, y=100)
etiqueta5 = Label(ventana,text='Escribe tu sexo').place(x=10, y=130)
sexoCaja = Entry(ventana,textvariable=sexo).place(x=220, y=130)
boton = Button(ventana,text='Saludo Personalizado',command = saludo).place(x=10, y=160)

ventana.mainloop()




















