/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import Model.Performance;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import DBConnection.ConnectSqlite;

/**
 *
 * @author natha
 */
public class PerformanceSqlLiteDAO {
    
    private Connection con = ConnectSqlite.getInstance().getConnection();
    
    private static PerformanceSqlLiteDAO instance;
    
    private PerformanceSqlLiteDAO(){
        
    }
    
    public static PerformanceSqlLiteDAO getInstance(){
        if(instance == null)
            instance = new PerformanceSqlLiteDAO();
        
        return instance;
    }
    
    public ArrayList<Performance> findAll() {
        
        ArrayList<Performance> lista = new ArrayList<>();
        
        try{
            Statement  stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("select c.aluno_id,a.username,date(c.date) as d, count() as c, (1.0/count()) as des, u.key from contador c, usuarios u, auth_user a where c.aluno_id = a.id and a.username = u.user group by date(c.date), c.aluno_id order by c.date asc");
            
            while(rs.next()){
                Performance p = new Performance(rs.getString("aluno_id"), rs.getString("username"), rs.getString("d"), rs.getInt("c"), rs.getDouble("des"), rs.getString("key"));
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
