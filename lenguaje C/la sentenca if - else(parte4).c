// la sentecia if de dos alternativas: if else

/*	if (sentecia)
 * 		accion
 * 	else(sentencia)
 * 		accion
 * */
 
//LA SENTENCI IF - ESLE 
#include <stdio.h>

int main(){
	
	float nota;
	
	printf("ingrese su nota: ");
	scanf("%f",&nota);
	
	if (nota < 10.5)
		puts("ud ha desaprobado");
	else
		puts("ud ha aprobado");
		
	return 0;
}
