// 9.2 Creacion PruebaPersonas Alumno: Juan Pablo Nolan

class Persona{
    static contadorPersona = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersona;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
        
    }

    get idPesona(){
        return this._idPersona;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    get edad(){
        return this._edad;
    }

    set edad(edad){
        this._edad = edad;
    }

    toString(){
        return `
        ${this._idPersona}
        ${this._nombre}
        ${this._apellido}
        ${this._edad}`
    }
}

class Empleado extends Persona{
    
    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }
    
    get sueldo(){
        return this._sueldo;
    }

    set sueldo(sueldo){
        this._sueldo = sueldo;
    }

    toString(){
        return `
        ${super.toString()}
        ${this._idEmpleado}
        ${this._sueldo}`;
    }
}

class Cliente extends Persona{
    
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegustro = fechaRegistro;
    }

    get _idCliente(){
        return this._idCliente;
    }
    
    get fechaRegistro(){
        return this._fechaRegustro;
    }

    set fechaRegistro(fechaRegistro){
        this._fechaRegustro = fechaRegistro;
    }

    toString(){
        return `
        ${super.toString()}
        ${this._idCliente}
        ${this._fechaRegustro}`;
    }
}

// 9.6 Prueba Clase Persona - Alumno: Giuliana Paola Diaz Luna
let persona1 = new Persona('Juan','Perez',32);
console.log(persona1.toString());

let persona2 = new Persona('Carlos','Ortega',22);
console.log(persona2.toString());

// 9.7 Prueba Clase empleado - Alumno: Nadia Acosta
let empleado1 = new Empleado('Maite','Robledo', 31, 6000);
console.log(empleado1.toString());

let empleado2 = new Empleado('Carmen','Rodriguez', 28, 4000);
console.log(empleado2.toString());


// 9.7 Prueba Clase cliente - Alumno: Nadia Acosta
let cliente1 = new Cliente('Miguel','Sosa', 25, new Date());
console.log(cliente1.toString());

let cliente2 = new Cliente('Lorena','Rojas', 21, new Date());
console.log(cliente2.toString());
