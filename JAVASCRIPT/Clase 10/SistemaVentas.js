/*
Clase 10: Proyecto Ventas
Laboratorio III: Javascript
Team: The Informatic Hamsters
Scrum Master: Giuliana Diaz
*/



/* 10.4 Creacion de la clase Orden. Parte 1 - Alumno: Juan Pablo Nolan*/

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregaoProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto); //Tenemos dos tipos de sintaxis: 1
            //this._productos[this._contadorProductosAgregados++] = producto; //Segunda sintaxis
        }
        else{
            console.log("No se pueden agregar mas productos");
        }
    } //Fin del metodo agregarProductos
} //Fin de la clase Orden



/* 10.3 Prueba de la clase producto - Alumno: Miguel Rodriguez*/
let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
console.log(producto1.toString());
console.log(producto2.toString());




