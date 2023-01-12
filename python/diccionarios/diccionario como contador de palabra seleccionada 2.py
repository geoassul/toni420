from collections import Counter
import operator

man_a = open('mbox-short.txt')

lista = []

for linea in man_a:
    if linea.startswith('From: '):
        linea = linea.split()
        lista.append(linea[1])
        
diccionario = dict((i, lista.count(i))for i in lista)
print (diccionario)
max_value = max(diccionario.values())
max_valuekey = max(diccionario, key = diccionario.get)
key = diccionario.get
#print(key)
print(max_valuekey, max_value)
