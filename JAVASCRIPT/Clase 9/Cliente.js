class Cliente extends Persona {

    static contadorClientes = 0;

    constructor (nombre, apellido, edad, fecharegistro){
        super (nombre, apellido, edad);
        this._idCliente =  ++Cliente.contador.Clientes;
        this._fechaRegistro = fecharegistro;
    }

    get _idCliente (){
        return this._idCliente;
    }

    get _fecharegistro (){
        return this._fechaRegistro;
    }

    set fecharegistro (fecharegistro){
        this._fechaRegistro = fecharegistro;
    }

    toString (){
        return super.toString() + ' '  + this._idCliente + ' ' + this._fecharegistro;
    }
}