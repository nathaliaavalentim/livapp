/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package livappmiddleware;

import DAO.AlunoPostgresDAO;
import DAO.AlunoSqlLiteDAO;
import DAO.PerformancePostgresDAO;
import DBConnection.ConnectSqlite;
import DBConnection.AbstractConexaoBanco;
import DAO.PerformanceSqlLiteDAO;
import DBConnection.ConnectPostgres;
import Model.Aluno;
import Model.Performance;
import java.util.ArrayList;

/**
 *
 * @author natha
 */
public class LivAppMiddleware {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        AbstractConexaoBanco sqlite = ConnectSqlite.getInstance();
        AbstractConexaoBanco postgres = ConnectPostgres.getInstance();
        ArrayList<Performance> listPerformance = PerformanceSqlLiteDAO.getInstance().findAll();
        ArrayList<Aluno> listAluno = AlunoSqlLiteDAO.getInstance().findAll();
        
        
        for(Aluno a: listAluno){
            AlunoPostgresDAO.getInstance().createOrReplace(a);
        }
        
        for(Performance p: listPerformance){
            PerformancePostgresDAO.getInstance().createOrReplace(p);
        }
        
        
        ConnectSqlite.getInstance().close();
        ConnectPostgres.getInstance().close();
        
        
        
    }
    
}
