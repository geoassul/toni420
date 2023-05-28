
import java.sql.*;
import javax.sql.DataSource;
import com.mchange.v2.c3p0.ComboPooledDataSource;

public class TestPOOLDS {
	
	private DataSource datasource;
	//Public static void main( String args[] ) throws SQLException {
	public TestPOOLDS(){
		var pooledDataSource = new ComboPooledDataSource();
		pooledDataSource.setJdbcUrl("jdbc:sqlite:sample.db");
		pooledDataSource.setMaxPoolSize(10);
		this.datasource = pooledDataSource;
		
	}
	public Connection recuperarConexion() throws SQLException{
		return this.datasource.getConnection();
		}
	
}
