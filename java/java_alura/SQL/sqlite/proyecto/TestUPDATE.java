import java.sql.*;

public class TestUPDATE {

  public static void main( String args[] ) throws SQLException {
  
   Connection c = null;
   //Statement stmt = null;
   
   try {
      // Class.forName("org.sqlite.JDBC");
      c = DriverManager.getConnection("jdbc:sqlite:sample.db");
      c.setAutoCommit(false);
      System.out.println("Opened database successfully");
      PreparedStatement stmt = c.prepareStatement("UPDATE COMPANY SET SALARY = ?   WHERE ID=?");
      stmt.setInt(1,677776);
      stmt.setInt(2,1);
      stmt.execute();
      /*stmt = c.createStatement();
      String sql = "UPDATE COMPANY set SALARY = 0000.0   where ID=3;";
      stmt.executeUpdate(sql);
      c.commit();*/
      //ResultSet rs = stmt.executeQuery( "SELECT * FROM COMPANY;");
      stmt = c.prepareStatement("SELECT * FROM COMPANY");
      stmt.execute();
      ResultSet rs = stmt.getResultSet();

      while ( rs.next() ) {
         int id = rs.getInt("id");
         String  name = rs.getString("name");
         int age  = rs.getInt("age");
         String  address = rs.getString("address");
         float salary = rs.getFloat("salary");
         
         System.out.println( "ID = " + id );
         System.out.println( "NAME = " + name );
         System.out.println( "AGE = " + age );
         System.out.println( "ADDRESS = " + address );
         System.out.println( "SALARY = " + salary );
         System.out.println();
      }
      rs.close();
      stmt.close();
      c.close();
   } catch ( Exception e ) {
      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
      System.exit(0);
   }
    System.out.println("Operation done successfully");
   }
}
