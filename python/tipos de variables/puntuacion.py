try:
    
    puntuacion = float(input('ingrese una puntuacion \n'))
    
   #filtro de puntaje 
    if puntuacion >= 0.0 and puntuacion <= 1.0:
        pass
    else:
        print('puntuacion incorrecta')
        
    #puntuacion
    def calculo_puntuacion(puntuacion):
        
        if puntuacion > 0.9 and puntuacion <= 1.0:
            print('sobresaliente')
        if puntuacion > 0.8 and puntuacion <= 0.9:
            print('notable')
        if puntuacion > 0.7 and puntuacion <= 0.8:
            print('bien')
        if puntuacion > 0.6 and puntuacion <= 0.7:
            print('suficiente')
        if puntuacion <= 0.6:
            print('insuficiente')
    
    calculo_puntuacion(puntuacion)
    
except:
    print('puntuacion incorrecta')        