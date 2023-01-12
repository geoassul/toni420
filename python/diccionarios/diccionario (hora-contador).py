#texto = input('ingrese un texto: ')
fhand = open('mbox-short.txt')
d = dict()
lista = []
for linea in fhand:
    if linea.startswith('From'):
        linea = linea.split()
        if len(linea) > 2:
            lista.append(linea[5])
#print(lista)
lista_t = []
for i in lista:
    i = i[:2]
    d[i] = d.get(i,0) + 1
for hora,contador in list(d.items()):
    lista_t.append((hora,contador))
lista_t.sort()
for i,c in lista_t:
    print(i,c)
    
'''        
for palabra in lista:
        d[palabra] = d.get(palabra,0) + 1
### este es el codigo que agregue.
lista_t = []
for c, e in list(d.items()):
    lista_t.append((e,c))
#print(max(lista_t))
lista_t.sort(reverse = True)
e,c = lista_t[0]
print(e,c)
#print(lista_t[0])
#valor = max(d.values())
#for palabra in d:
#    if d.get(palabra) == valor:
#        clave = palabra
#print(clave, valor)'''