import java.sql.*;
import javax.sql.DataSource;
import com.mchange.v2.c3p0.ComboPooledDataSource;

public class ProductoJDBC {
	private Int id;
	private String nombre;
	private String descripcion;
	private Int cantidad;
	
	public ProductoJDBC(String nombre,String descripcion, Integer cantidad){
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.cantidad = cantidad;
		
		}
	}


