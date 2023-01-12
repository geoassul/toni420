lista_de_items = []
while True:
    item = input('ingrese un item: ')
    if item == 'regresar' or item == 'salir' or item == 'regresar':
        break
    
    lista_de_items.append(item)
    
    if item == 'borrar':
         while True:
            item_borrado= input('item que se borrara: ')
            if item_borrado == 'fin':
                break
            lista_de_items.remove(item_borrado)
         lista_de_items.remove('borrar')
            
    #lista_de_items.append(item)
    print(lista_de_items)
print(lista_de_items)

while True:
    
    lista_final = []
    try:
        for valor in lista_de_items:
            costo = int(input('costo del item: '))
            cantidad = int(input('stock del item: '))
            caracteristicas_item = [valor,costo,cantidad]
            lista_final.append(caracteristicas_item)
            
            print(valor, costo, cantidad)
            print(lista_final)
            
        break
    except:
        print('corrija los precios por favor...')
    
    
        