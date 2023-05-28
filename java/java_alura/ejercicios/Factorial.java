public class Factorial{  //aqui agregamos un nombre a la clase de java, luego de class

    public static void main(String[] args){
        int n = 10;
        int resultado = 1;
        for (int contador = 1; contador <= n; contador++){
            resultado = contador * resultado;
            System.out.println(resultado);
            }
    }

}
