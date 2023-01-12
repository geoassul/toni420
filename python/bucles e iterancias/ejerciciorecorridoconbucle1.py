while True:
    palabra = input('ingrese una palabra: ')
    try:
        z = 1
        while z < (len(palabra)+1):
            print(palabra[-z], end='')
            z = z + 1
        print()
    except:
        print('ingresa una palabra')
        
    print(palabra[::-1])
    
    a = 0
    for letra in palabra:
        a = a - 1
        print(palabra[a], end='')
    print()