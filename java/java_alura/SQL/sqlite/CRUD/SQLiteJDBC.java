import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SQLiteJDBC{
    public static void main(String[] args){
        Connection connection = null; // creamos la variable para la clase Connection
        try{
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:sample.db");  // usamos drive manager, utilizando solo un parametro, evitando el user y password.
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30);  // set timeout to 30 sec.
            statement.executeUpdate("drop table if exists person");
            statement.executeUpdate("create table person (id integer, name string)");
            statement.executeUpdate("insert into person values(1, 'leo')");
            statement.executeUpdate("insert into person values(2, 'yui')");
            ResultSet rs = statement.executeQuery("select * from person");
            System.out.println(rs.getClass().getSimpleName());
            while(rs.next()){
                // read the result set
                System.out.println("name = " + rs.getString("name"));
                System.out.println("id = " + rs.getInt("id"));
            }
        }
        catch(SQLException e){
            // if the error message is "out of memory",
            // it probably means no database file is found
            System.err.println(e.getMessage());
            }
        finally{
            try{
                if(connection != null)
                  connection.close(); // !!IMPORTANTE: cerramos la conexion a la base de datos
            }
            catch(SQLException e){
                // connection close failed.
                System.err.println(e.getMessage());
            }
        }
    }
}
