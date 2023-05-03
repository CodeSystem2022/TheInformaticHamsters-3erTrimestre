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


// 1.3 Creamos la clase Monitor - Alumno:


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






