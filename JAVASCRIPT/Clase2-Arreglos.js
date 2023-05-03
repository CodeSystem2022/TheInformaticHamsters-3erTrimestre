/*
Clase 2: Arreglos
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Giuliana Dealbera Etchechoury
*/



// 2.1 Arreglos en JavaScript - Alumno: Marcelo Quispe
// Creacion de Array o arreglos
// let autos = new Array('Ferrari', 'Renault', 'BMW'); ESTA ES LA VIEJA SINTAXIS
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

// Recorremos  los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);
for(let i = 0; i < autos.length; i++){
    console.log(i+ ':' +autos[i]);
}

// Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

// Agregamos nuevos valores al arreglo
autos.push('Audi'); // Agregamos el elemento al final
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

// Tercera forma de agregar elementos TENIENDO CUIDADO
autos[6] = 'Renault';
console.log(autos);

// Como preguntar si es un Array o Arreglo
console.log(Array.isArray(autos)); // Devuelve un booleano

console.log(autos instanceof Array); // Preguntamos si la variable es una instancia de la clase Array


// 2.2 Recorremos los elementos de un arreglo - Alumno: Giuliana Dealbera Etchechoury

for(let elemento = 0; elemento < autos2.length; elemento++){
    console.log(elemento + ": " +autos2[elemento]); 
}

// 2.3 Modificamos los elementos - Alumno: 

// 2.4 Preguntamos si es un Array - Alumno: 