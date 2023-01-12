// SENTENCIA IF ( LIMPIAR PANTALLA Y LIMPIAR BUFFER)

#include <stdio.h>
#include <stdlib.h>  // Esta libreria nos sirve para utilizar la funcion "system()" y "fflush()"

int main(){
	
	char tecla;
	printf("---------------__");
	printf("\n---------------__");
	printf("\n---------------__");
	printf("\n---------------__");
	printf("\ningrese una tecla: \n");
	scanf("%s",&tecla);  // podemos usar la sentencia "%c" o "%s" para llamar a una cadena o string

	if (tecla == '1'){  // es mejor utilizar las llaves para trabajar con los condicionales
						// nos sirve para mantener orden e introducir varias sentencias dentro del cuerpo 
						//del condicional.
		
		system("clear");   // esta sentencia nos sirve para limpiar la pantalla
		printf("se realizo el borrado\n");
	}
	else{
		printf("no se realizo el borrado\n");
		printf("ingrese un digito valido por favor: \n");
		fflush(stdin); // Esta sentencia sirve para limpiar el acumulador o buffer...
		
		scanf("%s",&tecla);
		
		if (tecla == '1'){ 
			system("clear");
			printf("se completo la operacion, gracias!\n");
		}
		else {
			printf("no funciono\n");
		}
		
	}
	return 0;	//siempre se coloca, es una forma de codigo limpio. 
}
