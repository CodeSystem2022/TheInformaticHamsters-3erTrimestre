
/*
Clase 12: Clase 12 Proyecto estudiantes Parte 2
Laboratorio III: JAVA
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
*/

// 12.1 Creamos la Clase entidad Estudiante --Alumna: Nadia Acosta

package UTN;


import UTN.conexion.Conexion;

public class Main {
    public static void main(String[] args) {
        var conexion = Conexion.getConnection();
    if(conexion != null) {
        System.out.println("Conexion exitosa: " + conexion);
    }
    else
             System.out.println("Error al conectarse");
    } // Fin main
} // Fin clase