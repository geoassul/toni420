// ENTRADAS Y SALIDAS DE DATOS 
#include<stdio.h>

int main(){
	//de esta manera colocamos varios tipo de datos en un printf
	int a = 10;
	float b = 102.32;
	char letra = 'c';
	printf("%i\n%f\n%c\n",a,b,letra);  	//la cantidad de formatos tiene que ser igual
										// a la cantidad de valores a llamar.
	
		
	// Asi pedimos informacion al usuario:
	int m;
	float n;
	char l;
	
	printf("escribe el dato: \n");
	scanf("%i",&m);
	
	printf("escribe el dato: \n");
	scanf("%c",&l);
	
	printf("escribe el dato: \n");
	scanf("%f",&n);
	
	printf("%i %c %.1f \n",m,l,n);
	
	//asi pedimos datos mas grandes
	
	char s[50];		// el numero entre los corchetes indica la cantidad de caracteres que tendra la variable "s"
	
	printf("ingresa el dato: \n");
	gets(s);		// el gets permite obtener cadenas de caracteres sin el problema que posee
					// "scanf()" que no permite hacerlo. 
	printf("este es su entrada: %s",s); //para imprimir cadena de caracteres usamos el caracter %s
										// a comparacion del caracter %c que solo imprime uno.
	
	return 0;
}
