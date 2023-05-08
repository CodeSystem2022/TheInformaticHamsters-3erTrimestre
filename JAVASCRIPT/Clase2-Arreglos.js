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

// 2.2 Recorremos los lementos de un arreglo - Alumno Quiquinto Romina Ayelen
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos); ['Ferrari', 'Renault', 'BMW']

console.log(autos[0]); Ferrari
console.log(autos[2]); BMW

for(Let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]); 0 : Ferrari, 1 : Remault, 2:  BMW
}

// 2.3 Modificamos los elementos del arreglo- Alumno: Nadia Acosta
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //Agregamos el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar elementos teniendo cuidado
autos[6] = 'Renault';
console.log(autos); ['Ferrari', 'Volvo', 'BMW', 'Audi', 'Porche', 'Renault']


// 2.3 Modificamos los elementos del arreglo- Alumno: Miguel Rodriguez Saquilan
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //Agregamos el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo
// la de push seria la primera y la otra es recorrer todo el largo del arreglo
autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar elementos teniendo cuidado
// por que podemos generar espacios vacios 

autos[6] = 'Renault';
console.log(autos); ['Ferrari', 'Volvo', 'BMW', 'Audi', 'Porche', 'Renault']

// 2.4 Preguntamos si es un Array - Alumno: Juan Pablo Nolan

// Como preguntar si es una Array o Arreglo 
//Con las CLASE ARRAY
console.log(Array.isArray(autos2)); // Devuelve un bool


// 2.4 Preguntamos si es un Array - Alumno: Giuliana Paola Diaz Luna
console.log(Array.isArray(autos)); // Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array

// CON INSTANCEOF
console.log(autos2 instanceof Array); // Preguntamos si la variable es una instacia de la calse Array.
