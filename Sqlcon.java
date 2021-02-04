import java.sql.*;

public class Sqlcon
{
	public static void main (String[] args)
	{
		Connection con = null;
		try
		{
			String url = "jdbc:mysql://10.10.14.47:3306/mytest"+
				"?verifyServerCertificate=false"+
				"&useSSL=true"+
				"&requireSSL=true";
			String user = "<mysqluser>";
			String password = "<mysqlpass>";
                        System.setProperty("javax.net.ssl.keyStore", "/etc/mysqlcerts/keystore_jdbc.jks");
                        System.setProperty("javax.net.ssl.keyStorePassword", "<JKS password>");
                        System.setProperty("javax.net.ssl.trustStore", "/etc/mysqlcerts/truststore.jks");
                        System.setProperty("javax.net.ssl.trustStorePassword", "<JKS password>");

			Class dbDriver = Class.forName("com.mysql.cj.jdbc.Driver");
			con = DriverManager.getConnection(url, user, password);
                        String query = "select * from mytest.tasty";
                        Statement st = con.createStatement();
			ResultSet rs = st.executeQuery(query);
			while (rs.next()){
				int id = rs.getInt("id");
				String name=rs.getString("name");
				System.out.println("id: "+id+" name: "+name);
			}
 			st.close();

  			//System.out.println("connected...."+con);
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
		}
	}
}
