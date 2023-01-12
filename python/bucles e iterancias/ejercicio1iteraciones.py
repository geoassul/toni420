
numero = []
while True:
        try:
            n = input('>Introduzca un numero: ')
            if n != 'fin':
                numero.append(int(n))
            else:
                #numero.remove(0)
                print(min(numero))
                print(max(numero))
                print(sum(numero))
                print(len(numero))
                print(sum(numero)/len(numero))
                break
        except:
            print('entrada invalida')
print(sum(numero),len(numero),sum(numero)/len(numero))
"""
suma = 0
contador = -1
while True:
    numero = input('ingrese un numero: ')
    if numero != '0':
        suma = suma + int(numero)
    contador = contador + 1
    if numero == '0':
        print(suma)
        print(contador)
        print(suma/contador)
        break
"""
