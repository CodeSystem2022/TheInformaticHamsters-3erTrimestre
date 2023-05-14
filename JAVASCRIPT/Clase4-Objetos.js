/*
Clase 4: Objetos
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Giuliana Paola Diaz Luna
*/



// 4.1 Introducción a los Objetos en JavaScript Parte 1 - Alumno:


// 4.1 Introducción a los Objetos en JavaScript Parte 2 - Alumno:


// 4.2 Agregamos métodos a los Objetos - Alumno: Nicolas Segovia

let x = 10;// variable de tipo primitiva
console.log(x.length);

//Objeto 
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){ //metodo o funcionen JS
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombreCompleto());

// 4.3 Diferentes formas de crear un Objeto - Alumno: 



// 4.4  Cómo acceder a las propiedades de los Objetos - Alumno:



// 4.5 Agregar y eliminar propiedades de los Objetos - Alumno: 



// 4.6 Ejecutamos desde el navegador - Alumno: 



// 4.7 Distintas formas de imprimir un Objeto con: Object.values()  y JSON.stringify() - Alumno:





