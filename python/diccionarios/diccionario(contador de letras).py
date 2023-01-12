import string
#texto = input('ingresa el texto: ')
fhand = open('mbox-short.txt')
d = dict()
for linea in fhand:
    linea = linea.translate(str.maketrans('','',string.punctuation))
    linea = linea.lower()
    #linea = linea.split()
    for letra in linea:
        d[letra] = d.get(letra,0) + 1
lista = list(d.items())
lista.sort(reverse = True)
lista = lista[:26]
lista.sort()
for a, b in lista:
    print(a , b)
#print(lista)    
    
