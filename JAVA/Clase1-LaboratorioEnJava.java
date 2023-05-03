/*
Clase 1: Laboratorio en Java
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nicolas Segovia
*/

// 1.1 Diagrama de Clase UML para este laboratorio: Tienen como tarea hacer este diagrama en VSC,
// aquí es donde creamos la clase padre DispositivoEntrada - Alumno: Nicolas Segovia 



// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno: 


// 1.3 Creamos la clase Monitor - Alumno:


// 1.4 Creamos la clase Computadora - Alumno:


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


// 1.2 Creamos la clase hija Raton y la clase Teclado - Alumno:



