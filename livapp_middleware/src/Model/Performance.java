/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;

import java.util.Date;
import java.util.Objects;

/**
 *
 * @author natha
 */
public class Performance {
    
    String aluno_id;
    String username;
    String date;
    int count;
    double desempenho;
    String key;

    public Performance(String aluno_id, String username, String date, int count, double desempenho, String key) {
        this.aluno_id = aluno_id;
        this.username = username;
        this.date = date;
        this.count = count;
        this.desempenho = desempenho;
        this.key = key;
    }

    public String getAluno_id() {
        return aluno_id;
    }

    public void setAluno_id(String aluno_id) {
        this.aluno_id = aluno_id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public double getDesempenho() {
        return desempenho;
    }

    public void setDesempenho(double desempenho) {
        this.desempenho = desempenho;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 47 * hash + Objects.hashCode(this.aluno_id);
        hash = 47 * hash + Objects.hashCode(this.username);
        hash = 47 * hash + Objects.hashCode(this.date);
        hash = 47 * hash + this.count;
        hash = 47 * hash + (int) (Double.doubleToLongBits(this.desempenho) ^ (Double.doubleToLongBits(this.desempenho) >>> 32));
        hash = 47 * hash + Objects.hashCode(this.key);
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Performance other = (Performance) obj;
        if (this.count != other.count) {
            return false;
        }
        if (Double.doubleToLongBits(this.desempenho) != Double.doubleToLongBits(other.desempenho)) {
            return false;
        }
        if (!Objects.equals(this.aluno_id, other.aluno_id)) {
            return false;
        }
        if (!Objects.equals(this.username, other.username)) {
            return false;
        }
        if (!Objects.equals(this.date, other.date)) {
            return false;
        }
        return Objects.equals(this.key, other.key);
    }
    
    
    
    
    
}
