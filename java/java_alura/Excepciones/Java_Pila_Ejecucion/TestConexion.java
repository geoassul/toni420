
public class TestConexion {
	
	public static void main (String[] args) {
		Conexion con = new Conexion();
		con.leerDatos();
		con.cerrar();
		Conexion con = null;
		try{
			con = new Conexion();
			con.leerDatos();
			con.cerrar();
		} catch(IllegalStateException ex){
			System.out.println("Surgió un error en la conexión ");
		} finally {
			con.cerrar();
		}
	}
}

