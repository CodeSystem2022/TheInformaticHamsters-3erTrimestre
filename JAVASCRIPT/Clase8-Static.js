/*
//Clase 8: Static
//Laboratorio III: JAVASCRIPT
//Team: The Informatic Hamsters
//Scrum Master: Miguel Rodriguez Saquilan
*/

class Persona{

// poner lo que va dentro de esta clase aca.

    static contadorPersonas = 0; // Atributo estatico
        //email = 'Valor default email'; // Atributo no estatico

    static get MAX_OBJ(){ // Este metodo simula una constante
        return 5;
    }

constructor(nombre, apellido){
    this._nombre = nombre;
    this._apellido = apellido;   
    if (Persona.contadorPersonas < Persona.MAX_OBJ){
    this.idPersona = ++Persona.contadorPersonas;
    }
    else{
        console.log(' Se a superado el maximo de objetos permitidos');
    }
    //console.log('Se incrementa el contador : ' + Persona.contadorObjetosPersona);
}

    get nombre(){
        return this._nombre;
    }  
    
    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;        
    }

    set nombre(nombre){
        this._nombre = nombre;
    }


nombreCompleto(){
    return this.idPersona + ' ' + this._nombre + ' ' + this._apellido;
}   
// Sobreescribiendo  el metodo de la clase padre (Object)
    toString(){ // Regresa un String
        // Se aplica el poliformismo que significa = multiples formas  en tiempo de ejecucion
        // El metodo que se ejecuta depende  si es una referencia   de tipo padre o hija
        return this.nombreCompleto();
    }    


    static saludar(){
        console.log("Saludo desde este metodo static");
    }

    static saludar2(persona){
        console.log(persona.nombre + ' ' + persona.apellido);
    }

}
class Empleado extends Persona{ // Clase hija
    constructor(nombre, apellido, departamento){
        super (nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
    // Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto ()+ ' , ' + this._departamento;
    }
}    
/* 8.1 Palabra static con métodos: Parte 1 y 2  - Alumno: Marcelo Alejandro Quispe */

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('Maria', 'Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString esta es la manera de acceder  a atributos  y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

// persona1.saludar(); No se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);


// 8.2 Atributos estáticos:  Alumno:
  

   



// 8.3 Atributos estáticos vs No estáticos:   Alumno:



// 8.4 Uso de la palabra static: Parte 1 y 2  - Alumno:




// 8.5 Creación de constantes estáticas - Alumno
