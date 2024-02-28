/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DBConnection;

import java.sql.Connection;

/**
 *
 * @author natha
 */
public abstract class AbstractConexaoBanco {
    
    private Connection connection;
    
    public Connection getConnection() {
        return connection;
    }

    public void setConnection(Connection connection) {
        this.connection = connection;
    }
    
    public void close(){
        if(connection != null){
            try{
                connection.close();
            }
            catch(Exception e){
                
            }
        }
    }
    
    
    
}
