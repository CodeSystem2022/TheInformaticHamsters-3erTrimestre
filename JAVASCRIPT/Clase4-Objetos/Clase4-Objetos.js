/*
Clase 4: Objetos
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Giuliana Paola Diaz Luna
*/



// 4.1 Introducción a los Objetos en JavaScript Parte 1 - Alumno: Juan Pablo Nolan


let x = 10; //variable de tipo primitiva
console.log(x.length); undefined

//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30
}

console.log(persona.nombre);


// 4.1 Introducción a los Objetos en JavaScript Parte 2 - Alumno: Marcelo Alejandro Quispe
let x = 10; // variable de tipo primitiva
console.log(x.length);

// Objeto 
let persona = {
    nombre : 'Carlos',
    apellido : 'Gil',
    email : 'cgil@gmail.com',
    edad : 30,
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);


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



// 4.4  Cómo acceder a las propiedades de los Objetos - Alumno: Giuliana Dealbera Etchechoury

//opcion 1:
console.log(person['apellido']); //accediento al objeto como si fuese un arreglo

//opcion 2:
for(propiedad in persona){  //utilizando el ciclo for 
    console.log(propiedad);
    console.log(persona[propiedad]);
}

// 4.5 Agregar y eliminar propiedades de los Objetos - Alumno: Giuliana Paola Diaz Luna

// forma correcta: cambiamos dinamicamente el valor del objeto persona
persona.apellido = 'Diaz'; 
console.log(persona);

// forma incorrecta: cambiamos dinamicamente el valor del objeto persona
persona.apellida = 'Diaz'; // agregamos accidentalmente una nueva propiedad "apellida"
console.log(persona);

// eliminamos la propiedad apellida
delete persona.apellida;
console.log(persona);


// 4.6 Ejecutamos desde el navegador - Alumno: Nadia Acosta
//ver archivo index.html

// 4.7 Distintas formas de imprimir un Objeto con: Object.values()  y JSON.stringify() - Alumno: Miguel Rodriguez Saquilan

// Numero 4 utilizaremos JSON.stringity
console.log('// Numero 4 utilizaremos JSON.stringity')
let personaString = JSON.stringify(persona);
console.log(personaString);






