try:
    horas = int(input('introduza horas de trabajo\n'))
    tarifa = int(input('introduzca su tarifa\n'))
    
    def salario(horas,tarifa):
        if horas > 40:
            bono = horas - 40
            calculo_salario = ((horas - bono) * tarifa) + (bono * (1.5 * tarifa))
        else:
            calculo_salario= horas * tarifa
        
        return calculo_salario
    
    su_salario = salario(horas,tarifa)
    print('su salario : ' + str(su_salario))
    
    #if horas > 40:
    #    bono = horas - 40
    #    salario = ((horas - bono) * tarifa) + (bono * (1.5 * tarifa))
    #else:
    #    salario= (int(horas)*int(tarifa))
        
    #print('su salario'+ ':'+str(salario))

except:
    print('por favor, introduzca un numero')