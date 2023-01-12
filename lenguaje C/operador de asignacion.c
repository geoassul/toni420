// OPERADORES DE ASIGNACION: estos operadores nos permites simplificar 
// algunas operaciones matematicas haciendo que nuestro codigo sea mas facil
// de leer y escribir

#include <stdio.h>

int main(){
	int a,b,c;	// de esta podemos simplificar la asignacion de tipo de variable int a varias variables.
	a=b=c=10;	//de esta forma tambien podemos asignar valores a las variables
	
	a += 10;// a = a + 10; operacion de suma
	a -= 5; // a = a - 5 ; operacion de resta
	a *= 2; // a = a * 2 ; operacion de multiplicacion
	a /= 2; // a = a / 2 ; operacion de division
	
	printf("%i",a);
	return 0;
}
