package test;

import domain.*;

public class TestConversionObjeto {
    public static void main(String[] args) {
        Empleado empleado;       
        empleado = new Escritor("Esteban", 15000, TipoEscritura.CLASICO);
        //System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles()); //Si queremos acceder a metodos Escritor
        //empleado.getTipoEscritura(); //No se puede hacer
        
        //Downcasting
        //((Escritor)empleado).getTipoEscritura(); //Primera opcion - El objeto: empleado, es casteado a la clase hija: Escritor
        Escritor escritor = (Escritor)empleado; //Segunda opcion
        System.out.println(escritor.getTipoEscritura()); //Parte de la segunda opcion
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
        
        //Para el upcasting no hace falta hacer una conversion explicita, distinto al downcasting
        
    }
    
   
}
