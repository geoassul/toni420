texto = input('ingrese el archivo: ')
fhand = open(texto)
lista = []
d = dict()
for linea in fhand:
    if linea.startswith('From'):
        linea = linea.split()
        if len(linea) >= 3:
            lista.append(linea[2])
for palabra in lista:
    d[palabra] = d.get(palabra,0) + 1
print(d)
    
        