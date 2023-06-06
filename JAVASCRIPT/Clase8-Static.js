/*
//Clase 8: Static
//Laboratorio III: JAVASCRIPT
//Team: The Informatic Hamsters
//Scrum Master: Miguel Rodriguez Saquilan
*/

class Persona{ // clase padre

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
  

   



// 8.3 Atributos estáticos vs No estáticos:   Alumno: Giuliana Paola Diaz Luna

// atributo estatico: se asocia a la clase
// atributo no estatico: se asocia con los objetos

console.log(persona1.email);
console.log(empleado1.email); //tbm se puede acceder desde el objeto de la clase hija
//console.log(Persona.email); // no se puede acceder de la clase padre porque el atributo email es no estatico

// 8.4 Uso de la palabra static: Parte 1 y 2  - Alumno: Nadia Acosta // Modificaciones al codigo

class Persona {

    static contadorPersonas = 0; //Atributo estatico

    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        this.idPersona = ++Persona.contadorPersonas;
    }

}


    nombreCompleto() {
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }


    console.log(persona1.toString()); 1 Juan Carlos Perez
    console.log(persona2.toString()); 2 Maria Laura Lara
    console.log(empleado1.toString();) 3 Maria Gimenez, Sistemas
    console.log(Persona.contadorPersonas); 3

    let persona3 = new Persona('Carla', 'Pertosi');
    console.log(persona3.toString()); 4 Carla Pertosi
    console.log(Persona.contadorPersonas); 4

// 8.5 Creación de constantes estáticas - Alumno: Juan Pablo Nolan


console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; //No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let persona4 = new  Persona('Franco', 'Diaz');
console.log(persona4.toString());   
let persona5 = new Persona('Liliana', 'Paz')
console.log(persona5.toString());   