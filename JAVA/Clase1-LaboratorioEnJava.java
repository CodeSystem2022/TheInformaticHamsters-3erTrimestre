/*
Clase 1: Laboratorio en Java
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nicolas Segovia
*/

// 1.1 Diagrama de Clase UML para este laboratorio: Tienen como tarea hacer este diagrama en VSC,
// aquí es donde creamos la clase padre DispositivoEntrada - Alumno: Nicolas Segovia 




// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno: Nadia Acosta
package ar.com.system2023.mundopc;

public class Raton extends DispositivoEntrada {
    private final int idRaton;
    private static int contadorRatones;

    public Raton(String tipoEntrada, String marca){
        super(tipoEntrada, marca) ;
        this.idRaton = ++Raton.contadorRatones;
    }
    
    @Override 
    public String toString() {
        return "Raton{" + "idRaton=" + idRaton + ", "+super.toString()+ '}';
    }

}

// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno: Giuliana Paola Diaz Luna


package ar.com.system2023.mundopc;

public class Raton extends DispositivoEntrada{
    private final int idRaton;
    private static int contadorRatones;
    
    public Raton(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++Raton.contadorRatones;
    }

    @Override
    public String toString() {
        return "Raton{" + "idRaton=" + idRaton + ", "+super.toString()+'}';
    }
}

// 1.3 Creamos la clase Monitor - Alumno: Juan Pablo Nolan

package ar.com.system2023.mundopc;

public class Monitor {
    private final int idMonitor;
    private String marca;
    private double tamanio;
    private static int contadorMonitores;
    
    private Monitor(){
        this.idMonitor = ++Monitor.contadorMonitores;
    }

    public Monitor(String marca, double tamanio){
        this(); //llamado al constructor vacio
        this.marca = marca;
        this.tamanio = tamanio;
        
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getTamanio() {
        return this.tamanio;
    }

    public void setTamanio(double tamanio) {
        this.tamanio = tamanio;
    }

    //Ingresamos manualmente el getIdMonitor
    public int getidMonitor() {
        return this.idMonitor;
    }

    @Override
    public String toString() {
        return "Monitor{" + "idMonitor=" + idMonitor + ", marca=" + marca + ", tamanio=" + tamanio + '}';
    }   
}

// 1.4 Creamos la clase Computadora - Alumno: Giuliana Dealbera Etchechoury

package ar.com.system2023.mundopc;

public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;

    private Computadora(){
        this.idComputadora = ++Computadora.contadorComputadoras;
    }

    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton){
        this();
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }

    public int getidComputadora(){
        return idComputadora;
    }

    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public Monitor getMonitor(){
        return monitor;
    }
    public void setMonitor(Monitor monitor){
        this.monitor = monitor;
    }

    public Teclado getTeclado(){
        return teclado;
    }
    public void setTeclado(Teclado teclado){
        this.teclado = teclado;
    }

    public Raton getRaton(){
        return raton;
    }
    public void setRaton(Raton raton){
        this.raton = raton;
    }

    @Override
    public String toString(){
        return "Computadora{" + "idComputadora= " + idComputadora + ", nombre= " + nombre + ", monitor= " + monitor + ", teclado= " + teclado + ", raton= " + raton;
    }
}


// 1.5 Creamos la clase Orden: Parte 1 y 2 - Alumno:Miguel Rodriguez Saquilan
package ar.com.system2023.mundopc;

public class Orden {
    private final int idOrden;
    private Computadora computadora[]; // Arreglo de objetos
    private static int contadorOrdenes;
    private static final  int MAX_COMPUTADORAS = 10;
    private int contadorComputadora;
    
    //Constructor vacio
    
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
    }
    
   //Metodo para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora){
        if (this.contadorComputadora < Orden.MAX_COMPUTADORAS){
            this.computadora[this.contadorComputadora++] = computadora;
        }
        else{
            System.out.println("Has superado el limite " +Orden.MAX_COMPUTADORAS);
        }
    }
    //Mostrar orden
    public void mostarOrden(){
        System.out.println("Orden  #:"+this.idOrden);
        System.out.println("Computadoras de la orden #: " + this.idOrden);
        for(int i = 0; i < this.contadorComputadora; i++){
            System.out.println(this.computadora[i]);
        }
    }
}


// 1.6 Comenzamos las pruebas creando objetos de cada clase y las agregamos a 
// la lista de Orden: Parte 1, 2 y 3 - Alumno:
package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13);// IMPortar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("bluetooth", " HP");
        Computadora computadoraHP = new Computadora(" Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        // Creamos objetos de diferentes marcas 
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("bluetooth", " Gamer");
        Computadora computadoraGamer = new Computadora(" Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Orden orden1 = new Orden();
        Orden orden2 = new Orden(); // Una nueva lista para el objeto orden2
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        
        orden1.mostarOrden();
        orden2.mostarOrden();
        
        // Crear mas objetos de tipo computadora  con todos sus elementos.
        // completar una lista en el objeto  orden1 que llegue a los 10 elementos
        // probar de esta manera los metodos al mzximo rendimiento
    }
}


//Esto es un ejemplo. IGNORAR




