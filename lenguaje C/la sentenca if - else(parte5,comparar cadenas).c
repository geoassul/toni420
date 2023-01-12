//LA SENTENCI IF - ESLE 

#include <stdio.h>
#include <string.h>

int main(){
	char nombre[30],signo[20];
	printf("digite su nombre: ");
	gets(nombre);
	printf("digite su signo: ");
	gets(signo);
	
	if (strcmp(signo,"aries")==0)
		printf("%s es %s",nombre,signo);
	else
		printf("%s no es aries",nombre);
	
	return 0;
}
