try:
    pro = input('ingrese el archivo de texto: ')
    arch = open(pro)
except:
    if pro.find('.')==-1:
        print(pro.upper(),'pa ti')
    else:
        print('no es un archivo valido: ',pro)
    exit()
lista = []
contador = 0
sumador = 0
for linea in arch:
    if linea.startswith('X-DSPAM-Confidence: '):
        posicion = linea.find(': ')
        linea = linea.rstrip()
        dato = linea[20:]
        lista.append(float(dato))
        contador = contador + 1
for dato in lista:
    a = dato
    sumador = dato + sumador
promedio = sumador/contador
print(promedio)
print(contador)