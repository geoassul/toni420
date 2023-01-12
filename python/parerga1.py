palabra = input('>ingrese la palabra')
vocales = ['a','e','i','o','u']
for letra in palabra:
    if letra in vocales:
        continue
    print(letra)

    