// 3.4 Parte 1 Manejo de bloques de código - Alumno: Nicolas Segovia
package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    //Bloque de inicializacion estatico
    static{
        System.out.println("Ejecución de bloque estático");
        ++Persona.contadorPersonas;    
        //idPersona = 10; No es un atributo estatico por eso tenemos un error
    }
    


// 3.4 Parte 2 Manejo de bloques de código - Alumno: Juan Pablo Nolan

    //Bloque de inicializacion no estatico (contexto dinamico)
    {
        System.out.println("Ejecucion de bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; //Incrementamos el atributo
    }
    

    //Los bloques de inicializacion se ejecutan antes del constructor
    
    public Persona(){
        System.out.println("Esta es la ejecucion del constructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
    
}
