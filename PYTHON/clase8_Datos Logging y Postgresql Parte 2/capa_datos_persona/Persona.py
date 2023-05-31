'''
Clase 8: Capa de Datos Logging y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''

# SI IMPORTAN ALGO SIEMPRE ACA ARRIBA

from logger_base import log


#  8.1 Creación de la Clase Persona -- Alumno : 

class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None): # lo dejamos en none para que no sea obligatorio la asignacion de valor a los parámetros


# 8.2 Prueba de la Clase Persona - Alumno: Giuliana Paola Diaz Luna

if __name__== '__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@mail.com')
    log.debug(persona1)
    persona2 = Persona(nombre='Jose',apellido='Lopez',email='jlopez@mail.com')
    log.debug(persona1)
    persona3= Persona(id_persona = 1)
    log.debug(persona1)






