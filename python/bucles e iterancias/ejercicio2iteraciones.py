lista = []

while True:
    
    try:
        cantidad = int(input('cantidad de numeros de la lista: '))
        for i in range(0,cantidad):
            while True:
                try:
                    numero=int(input('> '))
                    """if numero == int(numero):
                        lista.append(numero)
                        break"""
                    lista.append(numero)
                    break
                except:
                    print('ingrese un numero')
                
        print(lista)
                
        #resultado del bucle
        #print('Maximo numero: ' + str(max(lista))+'\n'+'Minimo numero: ' + str(min(lista)))
        break
    
    except:
        print('ingrese un numero')
print('Maximo numero: ' + str(max(lista))+'\n'+'Minimo numero: ' + str(min(lista)))
