/*
Clase 7:Clases Parte 1
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: 
*/

// 6.1 Sintaxis de Clases en JavaScript: Parte 1 - Alumno:

// 6.1 Sintaxis de Clases en JavaScript: Parte 2 - Alumno: Giuliana Paola Diaz Luna

class Persona{
    // si no se define un constructor jv agrega un constructor vacio de manera automatica
    constructor(nombre,apellido){
        this.nombre = nombre; // inicializamos los atributos
        this.apellido = apellido;         
    }
}

// Creacion de objetos
let persona1 = new Persona ('Giuliana', 'Diaz');
console.log(persona1);

let persona2 = new Persona ('Fanny', 'Luna');
console.log(persona2);



// 6.2 Método Get y Set: Parte Get y Parte Set - Alumno: Nadia Acosta

class Persona{
    constructor(nombre,apellido){
        this._nombre = nombre; 
        this._apellido = apellido;         
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
}

let persona1 = new Persona ('Giuliana', 'Diaz');
console.log(persona1.nombre); Giuliana
persona1.nombre = 'Nadia';
console.log(persona1.nombre); Nadia
let persona2 = new Persona ('Fanny', 'Luna');
console.log(persona2.nombre); Fanny
persona2.nombre = 'Mia'
console.log(persona2.nombre); Mia



// 6.3 hoisting y clases: Parte 1 y 2 - Alumno:



// 6.4 Herencia: Parte 1 y 2 - Alumno: 


     



// 



