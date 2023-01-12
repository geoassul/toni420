from tkinter import *
from tkinter import messagebox    
        
ventana = Tk()
ventana.title('toni')
ventana.geometry('700x600')

lista = []
titulos = []

def base_datos():
    archivo = open('ejerciciotkinter1.txt')
    for linea in archivo:
        linea.rstrip()
        linea = linea.split('$')
        lista.append(linea[0]+'$'+linea[1]+'$'+linea[2]+'$'+linea[3]+'$'+linea[4])
    archivo.close()

def ingresar_dato():
    archivo = open('ejerciciotkinter1.txt','a')
    t = titulo.get()
    a = autor.get()
    e = editorial.get()
    np = numpag.get()
    f = fecha.get()
    dato = t+'$'+a+'$'+e+'$'+str(np)+'$'+f+'\n'
    archivo.write(dato)
    archivo.close()
    lista.append(t+'$'+a+'$'+e+'$'+str(np)+'$'+f)
    print('ok')
    colocar_ventana()
    print(lista)
def colocar_ventana():
    r = Text(ventana, width=80, height=15)
    archivo = open('ejerciciotkinter1.txt')
    r.insert(INSERT, "\ttitulo de libro\n"+('-'*80))
    for linea in archivo:
        linea.rstrip()
        linea = linea.split('$')
        r.insert(INSERT,'\t\t'+linea[0]+'\n'+
                'Autor:'+linea[1]+'\t'+
                'Editorial:'+linea[2]+'\t'+
                'Num. pag.:'+linea[3]+'\t'+
                'Fecha:'+linea[4]+('-'*80))
        titulos.append(linea[0])
    CajaRevision = Spinbox(ventana,textvariable=revisador,values=titulos,width=46).place(x=110,y=480)
    r.place(x=10,y=200)
    r.config(state=DISABLED)
    archivo.close()
    
#__ Eliminar libros
def eliminar_libro():
    archivo = open('ejerciciotkinter1.txt','w')
    dato = revisador.get()
    for linea in lista:
        i = linea.rstrip()
        i = i.split('$')
        if dato == i[0]:
            print('ok')
            lista.remove(linea)
            titulos.remove(dato)
            continue
        archivo.write(linea+'\n')
    archivo.close()
    print(lista)
    colocar_ventana()
    
#__variables del programa
        
titulo = StringVar()
autor = StringVar()
editorial= StringVar()
numpag = IntVar()
fecha = StringVar()
revisador = StringVar()

base_datos()
colocar_ventana()
#__Cuerpo de la ventana
titulo_programa = Label(ventana,text='relacion de libros que tengo que leer').place(x=220,y=10)
etiquetaTitulo=Label(ventana,text='Titulo:').place(x=10,y=50)
etiquetaAutor=Label(ventana,text='Autor:').place(x=10,y=80)
etiquetaEd=Label(ventana,text='Editorial:').place(x=10,y=110)
etiquetaNumpag=Label(ventana,text='Numero de paginas:').place(x=10,y=140)
etiquetaFecha=Label(ventana,text='Fecha limite:').place(x=10,y=170)

#__Entradas del programa
CajaTitulo = Entry(ventana,textvariable=titulo,width=42).place(x=160,y=50)
CajaAutor = Entry(ventana,textvariable=autor).place(x=160,y=80)
CajaEditorial = Entry(ventana,textvariable=editorial).place(x=160,y=110)
CajaNumpag = Entry(ventana,textvariable=numpag).place(x=160,y=140)
CajaFecha = Entry(ventana,textvariable=fecha).place(x=160,y=170)

#__botones
BotonGuardar = Button(ventana,text='añadir libro',command=ingresar_dato).place(x=550,y=47)
BotonEliminar = Button(ventana,text='libro ya leido',command=eliminar_libro).place(x=550,y=477)
BotonApagado = Button(ventana,text='apagar',width=10,height=6).place(x=400,y=77)

#__ventana de texto para mostrar datos en la ventana de programa
'''r = Text(ventana, width=80, height=15)
r.insert(INSERT, "\ttitulo de libro\n"+('-'*80))
r.place(x=10,y=200)
r.config(state=DISABLED)'''

#__spinbox para revisar contenido
EtiquetaRevision = Label(ventana,text='Titulo leido:').place(x=10,y=480)
CajaRevision = Spinbox(ventana,textvariable=revisador,values=titulos,width=46).place(x=110,y=480)


mainloop()