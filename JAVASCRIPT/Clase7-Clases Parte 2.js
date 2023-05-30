/*
Clase 7:Clases Parte 2
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Marcelo Alejandro Quispe
*/


// 7.1 Heredar métodos  - Alumno: Miguel Rodriguez Saquilan
nombreCompleto(){
    return this._nombre+' '+this._apellido;
}
console.log(empleado1.nombreCompleto());




// 7.2 Sobreescritura - Alumno:
     



// 7.3 Clase Object, toString, sobreescritura y Polimorfismo- Alumno: Giuliana Paola Diaz Luna

// Object.prototype.toString // esta es la manera de acceder a atributos y metodos de manera dinamica

// Sobrescribiendo el metodo de la clase padre (object) de clase persona
toString(){ // regresa un string
    // se aplica el polimorfismo= multiples formas en tiempo de ejecucion
    // El metodo que se ejecuta depende si es una referencia de tipo padre o hija
    return this.nombreCompleto();
}

console.log(empleado1.toString()); // se ejecuta el metodo de la clase hija

console.log(persona1.toString()); // se ejecuta el metodo de la clase padre
