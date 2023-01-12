// OPERACIONES ARITMETICAS 
// ejercicio.. pedir dos numeros y usar los operadores de asignacion
#include <stdio.h>

int main(){
	int n1,n2,suma=0,resta=0,mult=0,div=0;
	printf("ingrese dos numeros: ");
	scanf("%i %i",&n1,&n2);
	suma = n1 + n2;
	resta = n1 - n2;
	mult = n1 * n2;
	div = n1 / n2;
	
	printf("suma: %i\nresta: %i\nmult: %i\ndiv: %i\n",suma,resta,mult,div);


// conversor de grados a farenheit
	int cel,far;
	printf("ingrese la temperatura(C°): ");
	scanf("%i",&cel);
	far = ((cel*9)/5)+32;
	
	printf("temperatura en Farenheit: %i",far);
	return 0;
}
