mayor = None
print('antes: ', mayor)
for valor in [3,41,12,9,74,15,1]:
    if mayor is None or valor < mayor:
        mayor = valor
    print('bucle: ',valor, mayor)
print('mayor: ', mayor)