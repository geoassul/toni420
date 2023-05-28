
public class Flujo {

    public static void main(String[] args) {
    System.out.println("Inicio de main");
    metodo1();
    System.out.println("Fin de main");
  }

  public static void metodo1(){
	  
    System.out.println("Inicio de metodo1");
    try{
		metodo2();
	}
	catch(MiException exceptiom){
		System.out.println("hoola");
	}
    System.out.println("Fin de metodo1");
  }
  
  public static void metodo2(){
	  
    System.out.println("Inicio de metodo2"); 
    throw new MiException("hola mundo de errores"); 
    }
}
