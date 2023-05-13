/*
Clase 3: Funciones
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Nadia Acosta
*/


// 3.1 Introducción a funciones - Alumno: Nadia Acosta

miFuncion(8, 2); //esto se denomina hosting

function miFuncion(a, b) {
    console.log("Sumamos: "+ (a + b)); Sumamos: 10, Sumamos: 9
}

//Llamando la función 
miFuncion(5, 4);


// 3.2 Palabra return - Alumno: Nicolas Segovia

function miFuncion(a, b) {
    //console.log("Sumamos: "+ (a + b)); Sumamos: 10, Sumamos: 9
    return a + b;
}

//Llamando la función 
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);



// 3.3 Funciones de tipo expresión  - Alumno: Nadia Acosta

let x = function(a, b){ return a + b}; //necesita cierre con punto y coma
resultado = x(5, 6); //al llamarla se pone la variable y parentesis
console.log(resultado); 11

// 3.4 Funciones de tipo self e invoking - Alumno: Miguel Rodriguez Saquilan

//funciones de tipo self y invoking se llaman a si misma
(function(a,b){
    console.log('Ejecutando la funcion: '+(a+b))
})(9,6); 


// 3.5 Tipos de datos de una función - Alumno:



// 3.6 Funciones flecha  - Alumno: Juan Pablo Nolan

//Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado); 10




// 3.7 Argumentos y parámetros  - Alumno:



// 3.8 Concepto de hoisting - Alumno:



// 3.9 Paso por valor - Alumno: Giuliana Dealbera Etchechoury

let primitivo = 10;
function cambiarValor(o){ //paso por VALOR
    o = 20;
}
cambiarValor(primitivo);
console.log(primitivo); // o = 10, no sufre cambio.

// 3.9.1 Paso por referencia - Alumno: Giuliana Dealbera Etchechoury

const persona = {
    nombre: 'Juan',
    apellido: 'López'
}
console.log(persona); // {nombre: 'Juan', apellido: 'López'}
function cambiarPersona(p1){
    p1.nombre = 'Nina';
    p1.apellido = 'Perez';
}
cambiarPersona(persona);
console.log(persona); // {nombre: 'Nina', apellido: 'Perez'}