#texto = input('ingresa el nombre de archivo: ')
fhand = open('mbox-short.txt')
d = dict()
lista = []
for linea in fhand:
    if linea.startswith('From:'):
        linea = linea.split()
        lista.append(linea[1])
for palabra in lista:
    #index = palabra.find('@')
    #palabra = palabra[index +1 :]
    d[palabra] = d.get(palabra,0) + 1
### este es el codigo que agregue.    
valor = max(d.values())
for palabra in d:
    if d.get(palabra) == valor:
        clave = palabra
print(clave, valor)
#print (d)