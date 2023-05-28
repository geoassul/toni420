import java.sql.*;
import javax.sql.DataSource;
import com.mchange.v2.c3p0.ComboPooledDataSource;

public class pruebaPOOL {
	
	public static void main (String[] args) throws SQLException {
		TestPOOLDS con = new TestPOOLDS();
		for (int i = 0; i < 20; i++) {
			Connection conexion = con.recuperarConexion();
			System.out.println("open POOL:" + (i + 1));
			
			}
		
	}
}
