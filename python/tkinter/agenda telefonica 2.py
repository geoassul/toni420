#Agenda II
from tkinter import *
from tkinter import messagebox
lista = []
def guardar():
    n = nombre.get()
    ap = app.get()
    am = apm.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
    nombre.set("")
    app.set("")
    apm.set("")
    correo.set("")
    telefono.set("")
    consultar()

def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if conteliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)

def consultar():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    nombres = []
    r.insert(INSERT, "Nombre\tApellidos P\t\tApellido M\t\tTeléfono\t\tCorreo\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        nombres.append(arreglo[0])
        r.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=260)
    spinTelefono = Spinbox(ventana, value=valores,textvariable=conteliminar).place(x=450,y=50)
    #spinNombres = Spinbox(ventana,value=nombres, textvariable=nombres_eliminar).place(x=450,y=150)
    if lista ==[]:
        spinTelefono = Spinbox(ventana, value=valores).place(x=450,y=50)
    r.config(state=DISABLED)

def iniciarArchivo():
    archivo = open("ag.txt","a")
    archivo.close()
    
def cargar():
    archivo = open("ag.txt","r")
    linea = archivo.readline()
    while linea:
        if linea[-1]=='\n':
            linea = linea[:-1]
        lista.append(linea)
        linea = archivo.readline()
    archivo.close()
    
def escribirContacto():
    archivo = open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()
    
ventana = Tk()
nombre = StringVar()
app = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
nombres_eliminar = StringVar()
colorFondo = "#006"
colorLetra = "#FFF"
iniciarArchivo() # crea un archivo para almacenar datos
cargar()
consultar()
ventana.title("Agenda con archivos para totototoni")
ventana.geometry("700x600")
ventana.configure(background = colorFondo)
etiquetaTitulo = Label(ventana, text="Agenda con Archivos",bg=colorFondo, fg=colorLetra).place(x=270,y=10)
etiquetaN = Label(ventana, text="Nombre", bg=colorFondo,fg=colorLetra).place(x=50, y=50)
cajaN = Entry(ventana, textvariable=nombre).place(x=170, y=50)
etiquetaApp = Label(ventana, text="Apellido Paterno", bg=colorFondo,fg=colorLetra).place(x=50, y=80)
cajaApp = Entry(ventana, textvariable=app).place(x=170, y=80)
etiquetaApm = Label(ventana, text="Apellido Materno", bg=colorFondo,fg=colorLetra).place(x=50, y=110)
cajaApm = Entry(ventana, textvariable=apm).place(x=170, y=110)
etiquetaT = Label(ventana, text="Teléfono", bg=colorFondo,fg=colorLetra).place(x=50, y=140)
cajaT = Entry(ventana, textvariable=telefono).place(x=170, y=140)
etiquetaC = Label(ventana, text="Correo", bg=colorFondo,fg=colorLetra).place(x=50, y=170)
cajaC = Entry(ventana, textvariable=correo).place(x=170, y=170)
etiquetaEliminar = Label(ventana, text="Teléfono: ", bg= colorFondo,fg=colorLetra).place(x=370, y=50)
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)
botoGuardar = Button(ventana, text="Guardar", command=guardar, bg="#009",fg="white").place(x=210, y=200)
botoEliminar = Button(ventana, text="Eliminar", command=eliminar, bg="#009",fg="white").place(x=490, y=80)
mainloop()