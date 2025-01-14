import java.sql.*;
class Jdbc
{
    public static void main(String args[])
   {
      String driver="com.mysql.jdbc.Driver";
	  String url="jdbc:mysql://localhost:3306/school";
	  String username="root";
	  String password="21mg1a0573";
	  try{
	  Class.forName(driver);
	  Connection con=DriverManager.getConnection(url,username,password);
	  Statement stmt=con.createStatement();
	  stmt.executeUpdate("insert into person values(1,'sravani')");
	  stmt.executeUpdate("insert into person values(2,'ramesh')");
	  stmt.executeUpdate("insert into person values(3,'leela')");
	  stmt.executeUpdate("insert into person values(4,'chinnu')");
	  con.close();
	  }
	  catch(Exception e)
	  {
	    System.out.println(e);
	  }
	 
	}
} 