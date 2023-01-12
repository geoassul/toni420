import math
int_senal = 9
int_ruido = 10
relacion = float(int_senal/int_ruido)
decibelios = 10 * math.log10(relacion)
print(decibelios)