
package Accesodatos;

// una interface no ereda de la clase object si se puede 
// extender de otra clase interface
public interface IAccesoDatos {
// CREAMOS UNA CONSTANTE PUBLIC ESTATIC Y FINAL CON UN VALOR(10)
// Y CUALQUIER METODO QUE AGREGEMOS VA A SER PUBLICO Y ABSTRACTO
// ESTO SIEMPRE ES ASI EN INTERFACE    
    int MAX_REGISTRO = 10;
    
// Metodo insertar es abstracto y sin cuerpo
    // vamos a simular una base de datos con estos metodos
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
}
