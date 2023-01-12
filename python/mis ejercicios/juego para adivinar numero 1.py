import random
while(True):
        nombre = input('ingrese su nombre: ')
        q = input('¿desea jugar un juego? Si o No?')
        if q.lower() == 'si':
            pass
        elif q.lower() == 'no':
            exit()
        else:
            print('responda si o no, por favor')
            continue
        try:
            numero = int(input('ingrese un numero cualquiera'))
        except:
            print('ingrese un numero por favor hdp')
            continue
        x = random.randint(0,numero)
        y = 0
        while x != y:
            try:
                suerte = int(input('adivine el numero'))
            except:
                print('numero invalido, intente de nuevo')
                continue
            if suerte == x:
                print('bien',nombre)
                y = suerte
            elif suerte > x:
                print('el numero es menor')
            else:
                print('el numero es mayor')
