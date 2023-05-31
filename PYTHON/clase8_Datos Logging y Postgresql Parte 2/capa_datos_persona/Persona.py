'''
Clase 8: Capa de Datos Logging y Postgresql Parte 2
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Miguel Rodriguez Saquilan
'''

# SI IMPORTAN ALGO SIEMPRE ACA ARRIBA
from logger_base import log

from logger_base import log

#  8.1 Creación de la Clase Persona -- Alumno : Marcelo Alejandro Quispe
class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            Id Persona: {self._id_persona}, 
            Nombre: {self._nombre}, 
            Apellido: {self._apellido},
            Email: {self._email}
        '''

    # Metodos Getters and Setters
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


# 8.2 Prueba de la Clase Persona - Alumno: Giuliana Paola Diaz Luna

if __name__== '__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@mail.com')
    log.debug(persona1)
    persona2 = Persona(nombre='Jose',apellido='Lopez',email='jlopez@mail.com')
    log.debug(persona1)
    persona3= Persona(id_persona = 1)
    log.debug(persona1)






