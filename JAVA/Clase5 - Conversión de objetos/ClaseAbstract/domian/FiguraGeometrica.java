package domian;

public abstract class FiguraGeometrica{
    protected String tipoFigura;

    protected FiguraGeometrica(String tipoFigura){
        this.tipoFigura = tipoFigura;
    }

    public abstract void dibujar();
    
    public String getTipoFigura(){
        return tipoFigura;
    }

    @override
    public String toString(){
        return 'FiguraGeometrica{' + 'tipoFigura = ' + tipoFigura + '}';
    }
}