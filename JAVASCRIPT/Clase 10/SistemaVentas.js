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

/* 10.5 Prueba con la relacion de agregacion Parte 1 - Alumna: Nadia Acosta*/

calcularTotal(){
    let totalVenta = 0;
    for (let producto of this._productos){
        totalVenta += producto.precio;
    } //Fin del ciclo for
    return totalVenta
} //Fin del metodo calcularTotal

mostrarOrden () {
    let productoOrden = '';
    for (let producto of this._producto) {
        productoOrden += producto.toString()+'';
    } //Fin del ciclo for
    console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Producto: ${productoOrden}`)
}


let producto3 = new Producto('Cinturon', 50);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden();



/* 10.3 Prueba de la clase producto - Alumno: Miguel Rodriguez*/
let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
console.log(producto1.toString());
console.log(producto2.toString());




