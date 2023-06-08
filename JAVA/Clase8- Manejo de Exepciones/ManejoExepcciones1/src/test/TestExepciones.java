//
// ASISTENCIA ALUMNO MARCELO QUISPE
package test;


import static aritmetica.Aritmetica.division;
import exepciones.OperacionesExepcion;
import javax.management.openmbean.OpenDataException;


public class TestExepciones {
    public static void main(String[] args) {
        int resultado = 0;
 // con este try vamos a controlar el flujo de nuestro programa para que no se detenga        
        try{
            resultado = division(10, 0);
        } catch (OperacionesExepcion e){
            System.out.println("Ocurrio un error de tipo OperacionExepcion ");
            System.out.println(e.getMessage());
//============================================================================================

// ASISTENCIA ALUMNO MIGUEL RODRIGUEZ SAQUILAN
            
            
            
        }catch(Exception e ){
            System.out.println("Ocurrio un  error!!!");
            e.printStackTrace(System.out);// se conoce como la pila de exepciones  
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("Sereviso la division entre cero");
        }
        System.out.println("La variable de resultado tiene como resultado "+ resultado);
    }
}
