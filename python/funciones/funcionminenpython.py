while True:
    try:
        linea=input('> ')
        
        if linea == 'fin':
            print('suma,contador,promedio')
        valor= int(linea)  
        valor = valor + 1
        print(valor)
    except:
        print('error')