// LA SENTENCIA IF
/* 
	if(condicion){
		accion
	}
 * */
 
#include <stdio.h>
//ejercicio de prueba de divisibilidad

int main(){
	int n1,n2;
	printf("digite dos numero: ");
	scanf("%i %i",&n1,&n2);
	
	if (n1 % n2 == 0){
		printf("el numero %i es divisible con %i",n1,n2);
	}
}



