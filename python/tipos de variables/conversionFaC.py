try:
    ent = input('intrduzca una temperatura farenheit:\n')    
    fahr = float(ent)
    cel = (fahr - 32.0) * 5.0/9.0
    print(cel)
except:
    print('por favor, introduzca un numero')