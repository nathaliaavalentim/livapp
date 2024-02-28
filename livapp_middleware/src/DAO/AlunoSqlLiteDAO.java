/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import DBConnection.ConnectSqlite;
import Model.Aluno;
import Model.Performance;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author natha
 */
public class AlunoSqlLiteDAO {
    
private Connection con = ConnectSqlite.getInstance().getConnection();
    
    private static AlunoSqlLiteDAO instance;
    
    private AlunoSqlLiteDAO(){
        
    }
    
    public static AlunoSqlLiteDAO getInstance(){
        if(instance == null)
            instance = new AlunoSqlLiteDAO();
        
        return instance;
    }
    
    public ArrayList<Aluno> findAll() {
        
        ArrayList<Aluno> lista = new ArrayList<Aluno>();
        
        try{
            Statement  stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("select a.id,a.username, u.key from auth_user a left join usuarios u on (a.username = u.user) order by a.id asc");
            
            while(rs.next()){
                Aluno p = new Aluno(rs.getInt("id"), rs.getString("username"), rs.getString("key"));
                lista.add(p);
            }
            
            stmt.close();
        }
        catch(Exception e){
            System.out.println("Deu problema");
        }
        return lista;
    }
    
}
