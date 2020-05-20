/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Business;

import java.awt.List;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author lenovo
 */
public class JDBC {
    
    public ArrayList<Object[]> loadSampleData(String type) {
       ArrayList<Object[]> res = new ArrayList<Object[]>();
 
       try{
           Class.forName("com.mysql.cj.jdbc.Driver");


           
           String url = "jdbc:mysql://localhost:3306/renameee?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
           String user = "root";
           String pwd = "121314@Jgw";
           Connection con = DriverManager.getConnection(url,user,pwd);
           Statement st = con.createStatement();
           ResultSet rs = null;
           
           if(type == "user"){
               rs = st.executeQuery("select * from User_T");        
           }
           else if(type == "order"){
               rs = st.executeQuery("select * from Order_T");
           }
           else{
               rs = st.executeQuery("select * from Product_T");
           }
           
           int col = rs.getMetaData().getColumnCount();
           while(rs.next()){
               Object[] rows = new Object[col];
               for(int i = 1;i<=col;i++){
                   rows[i-1] = rs.getObject(i);
               } 
               res.add(rows);
            }
           rs.close();        
           st.close();
       }
       catch(Exception e){
           JOptionPane.showMessageDialog(null,e);
       }
       return res;
    }
}
