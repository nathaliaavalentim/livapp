/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import DBConnection.ConnectPostgres;
import DBConnection.ConnectSqlite;
import Model.Aluno;
import Model.Performance;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.sql.Date;
import java.text.ParseException;
import java.text.SimpleDateFormat;

/**
 *
 * @author natha
 */
public class PerformancePostgresDAO {
    
    private Connection con = ConnectPostgres.getInstance().getConnection();
    
    private static PerformancePostgresDAO instance;
    
    private PerformancePostgresDAO(){
        
    }
    
    public static PerformancePostgresDAO getInstance(){
        if(instance == null)
            instance = new PerformancePostgresDAO();
        
        return instance;
    }
    
    
    public void createOrReplace(Performance performance){
        if(update(performance) <= 0){
            insert(performance);
        }
    }
    
    
    public int insert(Performance performance) {
        try{
            PreparedStatement  insert = con.prepareStatement
               ("INSERT INTO performance(id,username,date,count,des,key,aluno_id) VALUES (?,?,?,?,?,?,?)");
            insert.setString(1, String.valueOf(performance.hashCode()));
            insert.setString(2, performance.getUsername());
            insert.setDate(3, convertDate(performance.getDate()));
            insert.setInt(4, performance.getCount());
            insert.setDouble(5, performance.getDesempenho());
            insert.setString(6, performance.getKey());
            insert.setString(7, performance.getAluno_id());
            
            //UPDATE -> update, delete, insert
            int resultado = insert.executeUpdate();
            insert.close();
            return resultado;
        }
        catch(Exception e){
            return -1;
        }
    }
    
     public int update(Performance performance) {
        try{
            PreparedStatement  insert = con.prepareStatement
               ("UPDATE performance SET username=?,date=?,count=?,des=?,key=?,aluno_id=? where id=?");
            
            String tmp = performance.getDate().substring(0, 4);
            int year = Integer.parseInt(tmp);
            
            insert.setString(1, performance.getUsername());
            insert.setDate(2, convertDate(performance.getDate()));
            insert.setInt(3, performance.getCount());
            insert.setDouble(4, performance.getDesempenho());
            insert.setString(5, performance.getKey());
            insert.setString(6, performance.getAluno_id());
            insert.setString(7, String.valueOf(performance.hashCode()));
            
            
            //UPDATE -> update, delete, insert
            int resultado = insert.executeUpdate();
            insert.close();
            return resultado;
        }
        catch(Exception e){
            return -1;
        }
    }
     
     public java.sql.Date convertDate(String date) throws ParseException{
         

        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            
        java.util.Date util_dob = dateFormat.parse(date);
            
        return new java.sql.Date(util_dob.getTime());
     }
    
    
}
