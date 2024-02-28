/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DBConnection;

import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author natha
 */
public class ConnectPostgres extends AbstractConexaoBanco {

    //Começo Singleton
    private static ConnectPostgres instance;

    private ConnectPostgres() {
        connect();
    }

    public static ConnectPostgres getInstance() {
        if (instance == null) {
            instance = new ConnectPostgres();
        }

        return instance;
    }
    //Final Singleton

    public void connect() {

        try {
            try {
                // db parameters
                Class.forName("org.postgresql.Driver");
                
                
                String server = "url_servidor";
                String database = "db";
                String url = "jdbc:postgresql://"+server+"/"+database;
                String user = "usuario";
                String pass = "senha";
            
                setConnection(DriverManager.getConnection(url, user, pass));
                
       

                System.out.println("Connection to Postgres has been established.");

            } catch (SQLException e) {
                System.out.println(e.getMessage());
            } 
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
    
}
