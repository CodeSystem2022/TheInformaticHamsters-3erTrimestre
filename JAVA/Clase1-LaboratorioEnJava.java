/*
Clase 1: Laboratorio en Java
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nicolas Segovia
*/

// 1.1 Diagrama de Clase UML para este laboratorio: Tienen como tarea hacer este diagrama en VSC,
// aquí es donde creamos la clase padre DispositivoEntrada - Alumno: Nicolas Segovia 



// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno: 


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


// 1.5 Creamos la clase Orden: Parte 1 y 2 - Alumno:


// 1.6 Comenzamos las pruebas creando objetos de cada clase y las agregamos a 
// la lista de Orden: Parte 1, 2 y 3 - Alumno:


// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno:



