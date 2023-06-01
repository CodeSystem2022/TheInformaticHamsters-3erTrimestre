/*
Clase 7:Clases Parte 1
Laboratorio III: JAVASCRIPT
Team: The Informatic Hamsters
Scrum Master: Quiquinto Romina Ayelen (abandono la carrera 29-05-2023)
Scrum Master: Giuliana Paola Diaz Luna 
*/


// 6.3 hoisting y clases: Parte 1 y 2 - Alumno: Giuliana Paola Diaz Luna
// Hosting: no se puede crear una objeto antes de haber definido la clase
// let persona1 = new Persona('Martín', 'Pérez'); 


// 6.1 Sintaxis de Clases en JavaScript: Parte 1 y 2 - Alumno: Giuliana Paola Diaz Luna
// Se recomienda que el nombre de la clase empiece con mayúscula para poder reconocer fácilmente las clases en JavaScript. 
// Una clase puede tener atributos y métodos. Si no se define un constructor JavaScript agregará uno vacío de manera automática.
class Persona{ // clase padre
    constructor(nombre, apellido){
        // inicializamos los atributos de la clase
        this._nombre = nombre;
        this._apellido = apellido;
    }

    // 6.2 Método Get y Set: Parte Get y Parte Set - Alumno: Nadia Acosta
    
    // Método Get: lee la información del atributo
    // no se puede llamar igual que nuestra propiedad, agregamos un guion bajo antes del atributo en el constructor
    get nombre(){
        return this._nombre;
    }
    // Metodo Set: modifica el valor del atributo
    set nombre(nombre){
        this._nombre = nombre;
    }
 
    //  Cramos el metodo get y set para apellido 
    get apellido(){ 
    return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
}


// 6.4 Herencia: Parte 1 y 2 - Alumno: Giuliana Paola Diaz Luna
class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido); // se llama al constructor de la clase padre
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
}


// Creacion de objeto 1
let persona1 = new Persona('Martín', 'Pérez');
console.log(persona1.nombre); // llammamos desde el metodo get
console.log(persona1.apellido);
persona1.nombre = 'Juan Carlos';// llamamos al metodo set para modificar el atributo nombre
persona1.apellido = 'Diaz';
console.log(persona1.nombre);
console.log(persona1.apellido;
//console.log(persona1); // llamamos desde el objeto

// Creacion de objeto 2
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre); 
console.log(persona2.apellido);
persona2.nombre = 'María Laura';
persona2.apellido = 'Martinez';
console.log(persona2.nombre);
console.log(persona2.apellido);
//console.log(persona2);

let empleado1 = new Empleado("María", "Gimenez", "Sistemas");
console.log(empleado1); 
console.log(empleado1.nombre);