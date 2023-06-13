// 9.3 Creacion de la clase persona Alumno: Miguel Rodriguez Saquilan.


class Empleado extends Persona{
    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido,edad);
        this._idPersona  = ++ Empleado.contadorEmpleados;
        this._sueldo = sueldo; 

    }
    // agregamos solo el set para el id empleado
    get idEmpleado(){
        return this.idEmpleado;
    }
    get sueldo(){
        this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    // despues del get y el set avanzamos con la clase toString
    toString(){ // heredamos el toString de la clase padre
        return `
        ${super.toString()} 
        ${this._idEmpleado} 
        ${this._sueldo}`;

    }
}