horas = int(input('introduza horas de trabajo\n'))
tarifa = int(input('introduzca su tarifa\n'))
if horas > 40:
    bono = horas - 40
    salario = ((horas - bono) * tarifa) + bono * (1.5 * tarifa)
else:
    salario= (horas*tarifa)

print('su salario'+ ':'+str(salario))