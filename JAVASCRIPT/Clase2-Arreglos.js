/*
Clase 2: Arreglos
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
*/



// 2.1 Arreglos en JavaScript - Alumno: Nicolas Segovia

// Sintaxis antigua de declarar un arreglo, ya no se recomienda
let autos = new Array("Ferrari", "Renault", "BMW");

// Sintaxis nueva. En esta caso ya no se le asigna referencia como 'new'
const autos2 = ["Ferrari", "Renault", "BMW"];
// con const asignamos la referencia en memoria del arreglo, el cual no se va a poder modificar
// lo que si se podra modificar es el contenido. 

// 2.2 Recorremos los elementos de un arreglo - Alumno: Giuliana Dealbera Etchechoury

for(let elemento = 0; elemento < autos2.length; elemento++){
    console.log(elemento + ": " +autos2[elemento]); 
}

// 2.3 Modificamos los elementos - Alumno: 

// 2.4 Preguntamos si es un Array - Alumno: 