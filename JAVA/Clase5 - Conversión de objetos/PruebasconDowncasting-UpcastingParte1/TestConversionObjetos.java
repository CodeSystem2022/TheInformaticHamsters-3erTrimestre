//TestConversionObjetos.java
//Polimorfismo : Andrea Llavel, trabajamos en conversion(cast); upcasting(de hijo a padre) y downcasting(de padre a hijo)

package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;   //variable de tipo padre, import todas las clase en el paquete domain
        //Luego asignamos una referencia, y apuntamos a la clase hija
        //le pasamos los parametros necesarios; el nombre, el sueldo, el tipo de escritura,que con el operador de punto vamos a 
        //acudir lo que es en nuestra numeracion el tipo CLASICO.
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO); 
        //System.out.println("empleado =" + empleado);
        System.out.println(empleado.obtenerDetalles());   //Si queremos acceder a metodos Escritor
        //empleado.getTipoEscritura();  //No se puede hacer
        //Downcasting : convertimos la clase padre a hijo/a
        //((Escritor)empleado).getTipoEscritura(); //Tenemos 2 opciones : esta es una
        Escritor escritor = (Escritor)empleado;  //Esta es una opcion
        escritor.getTipoEscritura();
        
        //Upcasting : convertimos la clase hijo/a en padre
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
    //Al ejecutar vemos exactamente lo mismo con Upcasting y Dowcasnting
    //Es un tipo cast, una conversion.
}
