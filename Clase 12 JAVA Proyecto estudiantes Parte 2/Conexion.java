
/*
Clase 12: Clase 12 Proyecto estudiantes Parte 2
Laboratorio III: JAVA
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
*/

// Clase conexion -- Alumno : Marcelo Alejandro Quispe

package UTN.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion = null;
        // Variables pra conectarnos ala base de datos
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/" + baseDatos;
        var usuario = "root";
        var password = "ADMIN";

        // cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException  | SQLException e){
            System.out.println("Ocurrio un error en la conexion: " + e.getMessage());
        } // Fin catch
        return conexion;
    } // Fin metodo Connection
}
