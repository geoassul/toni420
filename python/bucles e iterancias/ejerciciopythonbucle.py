while True:
    try:
        edad = int(input('ingrese su edad :'))
        n=1
        if edad == 1234:
            break
        while True:
            
            if edad >= n:
                print(n)
                n= n +1
            if edad == n:
                print(n)
                break
    except:
        print('ingrese un numero oe reconchatumare')