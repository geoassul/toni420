while True:
    
    tipo= input('tipo de prenda\n')
    
    if tipo == 'fin':
        break
    try:
        if tipo == 'polera':
            tipo = 'polera'
        elif tipo == 'polo':
            tipo = 'polo'
        elif tipo == 'bibidi':
            tipo = 'bibidi'
        else:
            print(a)
    except:
        print('por favor, introduzca un prenda')

    try:
        cantidad=int(input('prendas vendidas\n'))
    except:
        print('dato incorrecto')
    try:
        costo=float(input('costo de la prenda\n'))
    except:
        print('dato incorrecto')

    poleras=20
    if tipo == 'polera':
        poleras = poleras - cantidad

    costo_polera=25

    polos=50
    if tipo == 'polo':
        polos = polos - cantidad
    costo_polo=15

    bibidis=20
    if tipo == 'bibidi':
        bibidis = bibidis - cantidad
    costo_bibidi=10

    total_prendas=poleras+polos+bibidis
    ingreso=cantidad*costo
    ingreso_esperado=(poleras*costo_polera)+(polos*costo_polo)+(bibidis*costo_bibidi)

    print('total_prendas'+':'+str(total_prendas))
    #print(ingreso)
    #print(ingreso_esperado)
    if tipo == 'polo':
        print('polos'+':'+str(polos))
    else :
        print('no se vendio')
    if tipo == 'polera':
        print('poleras'+':'+str(poleras))
    else :
        print('no se vendio')
    if tipo == 'bibidi':    
        print('bibidis'+':'+str(bibidis))
    else :
        print('no se vendio\n')
