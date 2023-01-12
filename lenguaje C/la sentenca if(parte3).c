//SENTENCIA IF
#include <stdio.h>
#define	tarifa1 1.2
#define	tarifa2	1.0
#define	tarifa3	0.8

int main(){
	float tasa,consumo;
	printf("ingrese su consumo: ");
	scanf("%f",&consumo);
	if (consumo < 1000)
		tasa = tarifa1;
	if (consumo > 1000 && consumo < 1850)
		tasa = tarifa2;
	if (consumo > 1850)
		tasa = tarifa3;
	
	printf("su tarifa a pagar es: %.1f",tasa);
}
