/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import DBConnection.ConnectPostgres;
import DBConnection.ConnectSqlite;
import Model.Aluno;
import java.sql.Connection;
import java.sql.PreparedStatement;

/**
 *
 * @author natha
 */
public class AlunoPostgresDAO {
    
    private Connection con = ConnectPostgres.getInstance().getConnection();
    
    private static AlunoPostgresDAO instance;
    
    private AlunoPostgresDAO(){
        
    }
    
    public static AlunoPostgresDAO getInstance(){
        if(instance == null)
            instance = new AlunoPostgresDAO();
        
        return instance;
    }
    
    public void createOrReplace(Aluno aluno){
        if(update(aluno) <= 0){
            insert(aluno);
        }
    }
    
    
    public int insert(Aluno aluno) {
        try{
            PreparedStatement  insert = con.prepareStatement
               ("INSERT INTO products(id,name,price,category_id,banner) VALUES (?,?,?,?,?)");
            insert.setString(1, String.valueOf(aluno.getId()));
            insert.setString(2, aluno.getUsername());
            insert.setFloat(3, 0);
            insert.setString(4, "68cd4286-a416-40d4-915c-b0b600164f38");
            insert.setString(5, "-");
            
            //UPDATE -> update, delete, insert
            int resultado = insert.executeUpdate();
            insert.close();
            return resultado;
        }
        catch(Exception e){
            return -1;
        }
    }
    
     public int update(Aluno aluno) {
        try{
            PreparedStatement  insert = con.prepareStatement
               ("UPDATE products SET name=? where id=?");
            insert.setString(1, aluno.getUsername());
            insert.setString(2, String.valueOf(aluno.getId()));
            
            
            //UPDATE -> update, delete, insert
            int resultado = insert.executeUpdate();
            insert.close();
            return resultado;
        }
        catch(Exception e){
            return -1;
        }
    }
    
    
}
