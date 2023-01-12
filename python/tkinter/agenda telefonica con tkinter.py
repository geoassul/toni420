from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
    print('hola')
def eliminar():
    print('hola')
    
ventana = Tk()
nombre = StringVar()
app = StringVar()
apm = StringVar()
telefono = StringVar()
correo = StringVar()
conteliminar = StringVar()
colorFondo = '#006'
colorLetra = '#FFF'
ventana.title('agenda de archivos')
ventana.geometry('700x500')
ventana.configure(background = colorFondo)
etiquetaTitulo = Label(ventana, text='Agenda de archivos', bg=colorFondo, fg= colorLetra).place(x=270,y=10)
etiquetaN = Label(ventana, text='nombre', bg=colorFondo, fg= colorLetra).place(x=50,y=50)
etiquetaAP = Label(ventana, text='Apellido paterno', bg=colorFondo, fg= colorLetra).place(x=50,y=80)
etiquetaAM = Label(ventana, text='Apellido materno', bg=colorFondo, fg= colorLetra).place(x=50,y=110)
etiquetaTEL = Label(ventana, text='telefono', bg=colorFondo, fg= colorLetra).place(x=50,y=140)
etiquetaCOR = Label(ventana, text='correo', bg=colorFondo, fg= colorLetra).place(x=50,y=170)
cajaNombre = Entry(ventana, textvariable=nombre).place(x=180,y=50)
cajaAP = Entry(ventana, textvariable=app).place(x=180,y=80)
cajaAM = Entry(ventana, textvariable=apm).place(x=180,y=110)
cajaTEL = Entry(ventana, textvariable=telefono).place(x=180,y=140)
cajaCOR = Entry(ventana, textvariable=correo).place(x=180,y=170)

etiquetaCOR = Label(ventana, text='telefono', bg=colorFondo, fg= colorLetra).place(x=370,y=50)
spinTEL = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=50)
botGuardar = Button(ventana, text= 'guardar',command=guardar).place(x=180,y=200)
botBorrar = Button(ventana, text= 'eliminar',command=eliminar).place(x=450,y=80)

mainloop()
