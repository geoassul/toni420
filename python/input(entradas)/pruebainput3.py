ques='¿a que temperatura ambiente en celsius te encuentras?\n'
try:
    temperatura = int(input(ques))
    farenheit= 1.8 * int(temperatura) + 32 #formula de tranformacion de C° a F°
    f = 'temperatura en farenheit'
    float(farenheit)
    print(f + ': ' + str(farenheit))
except:
    print('por favor, introduzca un numero')