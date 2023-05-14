
package paquete2;


public class Clase4 {
    private String atributoPrivate = "atributo Privado";
    
    private Clase4() {
        System.out.println("Constructor privado");
    }
    
    // Creamos un contructor public para poder crear objetos
    public Clase4(String argumento) { // Aque se puede llamar al contructor vacio
        this();
        System.out.println("Contructor publico");
    }
    
    //Metodo private 
    private void metodoPrivado(){
        System.out.println("Metodo privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
}
