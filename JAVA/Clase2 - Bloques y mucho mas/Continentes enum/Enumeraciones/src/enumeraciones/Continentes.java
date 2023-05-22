
package enumeraciones;

public enum Continentes {
    AFRICA (53, "1.2 Billones"),
    EUROPA (43,"1.6 Billones" ),
    ASIA (87,"5.2 Billones"),
    AMERICA (35, "5.2 Billones"),
    OCEANIA (12, "3.2 Billones");
    
    private final int paises;
    private  final String habitantes;

    private Continentes(int paises, String habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    // Metodo Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
