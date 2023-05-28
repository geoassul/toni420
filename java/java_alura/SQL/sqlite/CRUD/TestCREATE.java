import java.sql.*;

public class TestCREATE {

   public static void main( String args[] ) throws SQLException{
      Connection c = null;
      Statement stmt = null;
      
      try {
         //Class.forName("org.sqlite.JDBC");
         c = DriverManager.getConnection("jdbc:sqlite:sample.db");
         System.out.println("Opened database successfully");

         stmt = c.createStatement();
         String sql = "CREATE TABLE employees " +
                        "(ID INT PRIMARY KEY     NOT NULL," +
                        " NAME           TEXT    NOT NULL, " + 
                        " firstName      TEXT    NOT NULL, " + 
                        " lastName       TEXT    NOT NULL )"; 
         stmt.executeUpdate(sql);
         stmt.close();
         c.close();
      } catch ( Exception e ) {
         System.err.println( e.getClass().getName() + ": " + e.getMessage() );
         System.exit(0);
      }
      System.out.println("Table created successfully");
   }
}
