// TIPOS DE DATOS EN C
#include<stdio.h>

int main(){
	
/* cuando imprimimos estos tipos de variables en un printf
 * podemos hacer la concatenacion dentro de las comillas "" 
 * usando el caracter "%" y el caracter asignado al tipo de 
 * variable ( %f,%i,%c.%lf,etc) ademas el caso de los datos 
 * tipo float agregando un punto en el caracter para concatenar
 * podemos manipular la longitud del dato( %.2f,%.f(se asume como 0),etc)*/
	
	char m = 'e';					//0...255 - %c
	int	x = 10;						//-32768...32767 - %i
	float y = 10.1111;			// 4 bytes... - %f
	short c = -122; 				//rango de -128...127 - %i
	unsigned int d = 128;			//0...655535 - %i
	long e = 112324;				// 4 bytes	- %li
	double db = 123123.111112;		// 4 bytes	- %lf
	printf("tipo de dato es: %c \n",m);
	printf("tipo de dato es: %i \n",x);
	printf("tipo de dato es: %lf \n",y);
	printf("tipo de dato es: %i \n",c);
	printf("tipo de dato es: %.3lf \n",db);
	printf("tipo de dato es: %li \n",e);
	printf("tipo de dato es: %i \n",d);
	
	
	return 0;
}

