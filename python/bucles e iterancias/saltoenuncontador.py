numero = int(input('ingresa un numero: '))
contador = 1
while numero != 0:
    print(contador,end=' ')
    if contador % 5 == 0:
        print('\n')
    if contador == numero:
        break
    contador = contador + 1
"""
numero = ''
for x in range(1,51):
    numero = f'{numero} {x}'
    if x % 5 == 0:
        print(numero)
        numero = ''
"""