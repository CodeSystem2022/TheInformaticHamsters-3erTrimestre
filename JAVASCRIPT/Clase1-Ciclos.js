/*
Clase 1: Ciclos
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Nicolas Segovia
*/



// 1.1 Ciclo While - Alumno: Nicolas Segovia

let contador  = 0; 
while(contador < 3){
    console.log(contador);
    contador ++;
}

console.log("Fin de ciclo while");

// 1.2 Ciclo do While - Alumno: Miguel Rodriguez Saquilan
let contDoWhile = 0;
do{
    console.log(contDoWhile); 
    conteo ++;
}while(contDoWhile < 3);
console.log("Fin del ciclo DO WHILE");



// 1.3 Ciclo For - Alumno: Giuliana Dealbera Etchechoury

for(let contFor = 0; contFor < 3; contFor++){
    console.log(contFor); //0, 1, 2
}
console.log("Fin del ciclo FOR")

// 1.4 Palabra reservada Break - Alumno: Marcelo Quispe
for(let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 == 0){
        console.log(contando); // muestra todos los pares
        break;
    }
}

// 1.5 Palabra reservada Continue - Alumno: Juan Pablo Nolan

for(let contando = 0; contando < 10; contando++){
    //separo pares de impares
    if(contando % 2 !== 0){
        continue; // ir a la siguiente iteracion
    }
    console.log(contando);
}

console.log("Termina el ciclo");

// 1.6 Etiquetas Labels - Alumno:
