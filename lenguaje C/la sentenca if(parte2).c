//SENTENCIA IF

#include <stdio.h>

int main(){
	
	float examen;
	
	printf("ingrese su nota: ");
	scanf("%f",&examen);
	
	if (examen > 10.5)
		puts("aprobado"); //la funcion de puts es imprimir pero solo dentro de un condicional.
		
	return 0;
}

