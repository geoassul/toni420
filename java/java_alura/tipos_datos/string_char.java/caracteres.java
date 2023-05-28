
public class caracteres {

    public static void main(String[] args){
		String frase = "argentina campeeeeeon"; //podemos usar comillas dobles.
		char letra = '\uFF9B'; // se usa una sola comilla
		char letra1 = 'a';
		char letra2 = 90;
		
		System.out.println(frase +": " + letra + letra1 + letra2);
		
		// Sobre la memoria, cuando otorgamos un valor a un dato:
		int dato = 5;
		int dato2 = 0;
		// si reemplazamos alguno de los datos con otro dato
		dato = dato2;
		//dato obtiene el valor de dato2, no se "convierte en el dato2" sino solo obtiene el valor
		dato = 10;
		// aunque cambiemos el valor de dato, dato2 sera el primer valor que se le otorgo. 0
		System.out.println(dato2);
	}
}
