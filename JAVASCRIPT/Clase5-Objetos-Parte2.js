/*
Clase 5: Objetos Parte 2
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
*/


// 5.1 Métodos get y set Parte 1  - Alumno: Giuliana Dealbera Etchechoury

let personaGet = {
    nombre: 'Frodo',
    apellido: 'Bolsón',
    raza: 'Hobbit',
    rol: 'Portador del anillo',
    get nombreRol(){
        return this.nombre + this.apellido + ' es el ' + this.rol;
    }
}
console.log('--Utilizando el método GET--')
console.log(personaGet.nombreRol);

// 5.1 Métodos get y set  Parte 2 - Alumno: Rodriguez Saquilan Miguel
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'aguantelaT@gmail.com',
    edad:28,
    idioma: 'ES' ,
    set lang(lang){
        this.idioma = lang.toUpperCase();
        console.log('Comenzamos con el metoso get y set  para idiomas');
        console.log(persona.lang);        



// 5.2 Constructores de objetos - Alumno:



// 5.3 Agregar métodos al constructor del objeto - Alumno: Giuliana Paola Diaz Luna

function Persona1(nombre, apellido, email){ //constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}

let padre =new Persona3('Leo','Lopez','lopez@gmail.com');
padre.nombre = 'Luis'; // modificamos el nombre
console.log(padre.nombreCompleto()); // utilizamos la funcion 

let madre =new Persona3('Laura','Contrera','contreral@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto()); // utilizamos la funcion 

// 5.4 Distintas formas de crear objetos - Alumno: Juan Pablo Nolan

//Caso objeto 1
let miObjeto1 = new Object(); //Esta es una opcion formal
//Caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//Caso String 1
let miCadena1 = new String("Hola"); //Sintaxis formal
//Caso String 2
let miCadena2 = "Hola"; //Esta es la sintaxis simplificada y recomendada

//Caso con numeros 1
let miNumero1 = new Number(1); //Es formal no recomendable
//Caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//Caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//Caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada

//Caso arreglos 1
let miArrelgo1 = new Array(); //Formal
//Caso arreglos 2
let miArrelgo2 = []; //Sintaxis recomendada

//Caso function 1
let miFuncion1 = new function(); //Todo despues de new es considerado objeto
//Caso function 2
let miFuncion2 = function(){}; //Notacion simplificada y recomendada

// 5.5 El uso de prototype - Alumno:  Marcelo Alejandro Quispe
// Uso de prototype
Persona3.prototype.telefono = '3513475612';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5493513475612'
console.log(madre.telefono);


// 5.6 El uso de call - Alumno: Nadia Acosta
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic', '54926248845')); Lic: Juan Perez 54926248845
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '5467789809034')); Ing: Carlos Lara 5467789809034

// 5.7 El uso de apply - Alumno:
