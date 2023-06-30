
/*
Clase 12: Clase 12 Proyecto estudiantes Parte 2
Laboratorio III: JAVA
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
*/

// 12.2 Listado de estudiantes con la Clase EstudianteDAO -> Parte 1, 2, 3 y 4 -- Alumno : Marcelo Alejandro Quispe

package UTN.datos;

import UTN.dominio.Estudiante;

import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    // Metodo listar
    public List<Estudiante> listarEstudiantes(){
        List <Estudiante> estudiantes = new ArrayList<>();
        // Creamos algunos objetos  que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; // Envia la setencia  a labase de datos
        ResultSet rs; // Obtenemos el resultado de  la base de datos
        // Creamos un objeto de tipo conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 ORDER BY idestudiantes2022";
        try{
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2022"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail (rs.getString("email"));
                // Falta agregarlo a la lista
                estudiantes.add(estudiante);
            }
        }catch(Exception e){
            System.out.println("Ocurrio  un error al seleccionar datos : " + e.getMessage());
        }
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println("Ocurrio un error al cerrar la conexion: "+ e.getMessage());
            }
        }//  Fin finally
        return estudiantes;
    }// Fin metodo Listar

// 12.4 Creamos en PersonaDAO() el método -> fin by id --Alumno: Juan Pablo Nolan

    // Metodo por id -> fin by id

    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 WHERE idestudiantes2022=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if(rs.next()){
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true; // Se encontro un registro
            } // Fin if
        }catch (Exception e){
            System.out.println("Ocurrio un error al buscar estudiante: " + e.getMessage());
        }// Fin catch
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("Ocurrio un error al cerrar  la conexion: " + e.getMessage());
            }// Fin catch
        }// Fin finally
        return false;
    }

// 12.6 Método agregarEstudiante() -> Parte 1 y 2  --Alumna: Nadia Acosta

    //Metodo agregar un nuevo estudiante
    public boolean agregarEstudiante (Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql ="INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            return true;
        }catch(Exception e){
            System.out.println("Ocurrio un error al agregar estudiante: " + e.getMessage());
        } // Fin catch
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println(" Error al cerrar la conexion: " + e.getMessage());
            }// Fin catch
        }// Fin finally
        return false;
    }// Fin Metodo agregarEstudiante

// 12.8 Agregamos el método -> modificarEstudiante() -- Alumno: Juan Pablo Nolan

    // Metodo para modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2022 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2022=?";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.setInt(5, estudiante.getIdEstudiante());
            ps.execute();
            return true;
        }catch (Exception e){
            System.out.println("Error al modificar estudiante: " + e.getMessage());
        }// Fin catch
        finally {
            try{
                con.close();
            }catch (Exception e ){
                System.out.println("Error al cerrar la conexion: " + e.getMessage());
            }// Fin catch
        }// Fin finally
        return false;
    }// Fin metodo modificarEstudiante
    
// 12.9 Comenzamos con las pruebas del método -> modificarEstudiante() --Alumna: Giuliana Paola Diaz Luna
    public static void main(String[] args) {
        var estudianteDao = new EstudianteDAO();
        // Modificar estudiante
        var estudianteModificado = new Estudiante(1, "Juan Carlos", "Juarez", "1234567897", "juan@mail.com");
        var modificado = estudianteDao.modificarEstudiante(estudianteModificado);
        if(modificado)
            System.out.println("Estudiante modificado: " + estudianteModificado);
        else
            System.out.println("No se modifico el estudiante: " + estudianteModificado);

// 12.7 Comenzamos con las pruebas del Método -> agregarEstudiante() Parte 1 y 2 -- Alumno: Miguel Rodriguez Saquilan

        // Agregar estudiante
        //var nuevoEstudiante = new Estudiante("Carlos", "Lara","5493513475622", "carlosl@mail.com");
        //var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
        //if (agregado)
        //    System.out.println("Estudiante agregado: " + nuevoEstudiante);
        //else
        //    System.out.println("No se agregado estudiante : " + nuevoEstudiante);


// 12.3 Comenzamos con las pruebas del método listarEstudiantes() -- Alumno: Juan Pablo Nolan
        // Listar lo estudiantes
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDao.listarEstudiantes();
        estudiantes.forEach(System.out::println); // Funcion lambda para imprimir

// 12.5 Hacemos las pruebas del método -> buscarEstudiantePorId() -- Alumno: Miguel Rodriguez Saquilan

        // Buscar por id
        // var estudiante1 = new Estudiante(1);
        //System.out.println("Estudiantes antes de la busqueda: " + estudiante1);
        //var encontrado = estudianteDao.buscarEstudiantePorId(estudiante1);
        //if (encontrado)
        //    System.out.println("Estudiante encontrado: " + estudiante1);
       // else
        //    System.out.println("No se encontro el estudiante: " + estudiante1.getIdEstudiante());

        }
    }


