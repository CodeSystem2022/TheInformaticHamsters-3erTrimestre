//package test;

import enumeraciones.Dias;
import static enumeraciones.Dias.JUEVES;
import static enumeraciones.Dias.LUNES;
import static enumeraciones.Dias.MARTES;
import static enumeraciones.Dias.VIERNES;

public class TestEnumeraciones {
    public static void main(String[] args){
        System.out.println("Dia 1: " + Dias.LUNES);
        indicarDiaSemana(Dias.LUNES); // Las enumeraciones se tratan como cadenas
    }
    
    // Alumno: Giuliana Paola Diaz Luna
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Séptimo dia de la semana");
                break;    
                
    }
    }
}
