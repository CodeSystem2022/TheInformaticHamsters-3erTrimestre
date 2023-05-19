package domian;

public class Rectangulo extends FiguraGeometrica{
    public Rectangulo(String tipoFigura){
        super(tipoFigura);
    }

    @override
    public void dibujar(){
        system.out.println('Se imprime un: ' + this.getClass().getSimpleName());
    }
}


