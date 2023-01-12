def ventana_datos():
    r = Text(ventana, width=80, height=15)
    datos = open('ejerciciotkinter1.txt')
    r.insert(INSERT, "\ttitulo de libro\n"+('-'*80))
    valores = []
    for i in datos:
        if i[-1] == '\n':
            i = i.rstrip()
            lista = i.split('$')
            r.insert(INSERT,'\t\t'+lista[0]+'\n'+'Autor:'+lista[1]+'\n'+('-'*80))
            valores.append(lista[0])
            print(valores)
        else:
            print('no hay datos perroooo')
            break      
    r.place(x=10,y=200)
    r.config(state=DISABLED)
    spinLibros = Spinbox(ventana,values=valores,textvariable=revisador,width=46).place(x=110,y=480)
def añadir_libro():
    archivo = open('ejerciciotkinter1.txt',"a")
    if messagebox.askquestion('pregunta','desea guardar?')=='yes':
        ventana_datos()
        #print('\t'+titulo.get()+'\n'+'Autor:'+autor.get()+' '+'Editorial:'+editorial.get()+' '+'Paginas:'+str(numpag.get())
         # +' '+'Fecha:'+fecha.get())
        datos = titulo.get()+'$'+autor.get()+'$'+editorial.get()+'$'+str(numpag.get())+'$'+fecha.get()+'\n'
        archivo.write(datos)
        messagebox.showinfo("Guardado","El contacto ha sido imprimido en pantalla")
        
    else:
        print('no quiso')
    archivo.close()

    
def eliminar_libro():
    if messagebox.askquestion('pregunta','¿desde eliminar?') == 'yes':
        print('eliminado')
        messagebox.showinfo('eliminar','el libro ha sido eliminado')
    else:
        print('no')
        