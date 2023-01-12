//directivas del procesador y variables

//todas las librerias empiezan con la palabra "include"
#include<stdio.h> //sirve para imprimir datos con printf y dar y recibir datos del computador


//MACROS : siven para definir una variable que se usara en todo el programa
//las macros empiezan con la palabra "define"
#define decimal	1.2142 //las macros sirven para asignarle el valor a una variable y nunca cambara su valor

int	y = 10;			// esto es una variable global
				//
int main(){  	// esta es la funcion principal donde ejecutaremos el programa principal..
				//"int" quiere decir que es una funcion con valor tipo entero y "main" es el nombre el programa
	
	int	x = 10;		//esto es una variable local(esta dentro de una funcion)
	float suma = 0;
	
	suma = decimal + x;
	
	printf("esto es una suma: %.2f",suma); 
		
	return 0;	//es una buena practica de programacion colocar esta sentencia de programa
				//indicamos a la funcion principal que el programa termino.(de un modo correcto)
}





