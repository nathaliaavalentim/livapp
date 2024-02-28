package DBConnection;

/**
 *
 * @author natha
 */
import DBConnection.AbstractConexaoBanco;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author sqlitetutorial.net
 */
public class ConnectSqlite extends AbstractConexaoBanco {

    //Começo Singleton
    private static ConnectSqlite instance;

    private ConnectSqlite() {
        connect();
    }

    public static ConnectSqlite getInstance() {
        if (instance == null) {
            instance = new ConnectSqlite();
        }

        return instance;
    }
    //Final Singleton

    public void connect() {

        try {
            try {
                // db parameters
                Class.forName("org.sqlite.JDBC");
                String url = "jdbc:sqlite:C:/LivApp/mysite2/db.sqlite3";
                // create a connection to the database
                this.setConnection(DriverManager.getConnection(url));

                System.out.println("Connection to SQLite has been established.");

            } catch (SQLException e) {
                System.out.println(e.getMessage());
            } 
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
