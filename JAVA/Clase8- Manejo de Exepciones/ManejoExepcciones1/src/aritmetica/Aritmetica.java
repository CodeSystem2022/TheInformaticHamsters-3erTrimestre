// ASISTENCIA
// ALUMNO: NADIA ACOSTA
//ALUMNO:  Diaz Luna, Giuliana Paola
package aritmetica;

import exepciones.OperacionesExepcion;
import javax.management.openmbean.OpenDataException;

public class Aritmetica {
    // va ser de tipo publico static para que podamos mandarloa llamar directamento
    public static int division(int numerador, int denominador) throws OpenDataException{ 
           
       if(denominador == 0){
         throw new OpenDataException("Division entre cero");
       }  
       return numerador / denominador;
    }
    }
