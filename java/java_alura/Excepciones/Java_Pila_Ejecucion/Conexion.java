public class Conexion {

   public Conexion() {
       System.out.println("Abriendo conexion");
   }

   public void leerDatos() {
       System.out.println("Recibiendo datos");
       throw new IllegalStateException();
   }

   public void cerrar() {
       System.out.println("Cerrando conexion");
   }
}

