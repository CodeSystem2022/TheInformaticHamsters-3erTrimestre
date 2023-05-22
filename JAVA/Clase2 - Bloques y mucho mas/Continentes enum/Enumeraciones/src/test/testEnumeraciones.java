
package test;

import enumeraciones.Dias;


public class testEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1 :"+ Dias.LUNES);
        indicarDiaSemana(Dias.LUNES); // las enumeraciones se tratan como cadenas
        indicarDiaSemana(Dias.MARTES);
    }
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semna ");
                break;
            case  MARTES:
                System.out.println("Sgundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semna");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semna");
                break;
            case DOMINGO:
                System.out.println("Sextimo dia de la semana");
                break;
            default:
                System.out.println("Eso nio es un adia de la semana");
                
        }
    }
}
