package test;

import domain.*;

public class TestSobreescritura {
    public static void main(String[] args) {
        //Sobre escritura
        //Gerente gerente1 = new Gerente("Jose", 5000, "Sistemas"); 
        //System.out.println("Gerente = " + gerente1.obtenerDetalles());
        
        //Polimorfismo
        Empleado empleado1 = new Empleado("Juan", 10000);
        imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        Gerente gerente1 = new Gerente("José", 5000, "Sistemas");
        imprimir(gerente1);
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());
    }
    
    //Polimorfismo
    public static void imprimir (Empleado empleado){
        String detalles = empleado.obtenerDetalles();
        System.out.println("detalles (desde metodo imprimir) = " + detalles);
    }
}
