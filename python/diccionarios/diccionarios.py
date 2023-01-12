texto = open('words.txt')
diccionario = dict()
for linea in texto:
    linea = linea.rsplit()
    lista = list(linea)
    
    for palabra in lista:
        diccionario[palabra] = ' '
        
print(diccionario)
print('reptitive' in diccionario)