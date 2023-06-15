'''
Clase 9: Capa de Datos Logging y Postgresql Parte 3
Laboratorio III: PYTHON
Team: The Informatic Hamsters
Scrum Master: Nadia Yanella Acosta
'''


from capa_datos.log.conexion import Conexion
import Persona
from logger_base import log


#  9.1 En la clase PersonaDao: método seleccionar: Alumno Miguel Rodriguez Saquilan

class PersonaDAO:
    """
    DAO significa: data access Object
    CRUD Significa:
                   Create ->  Insertar
                   Read   ->  Seleccionar
                   Update ->  Actualizar
                   Delete ->  Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(id_persona,nombre, apellido, email) VALUES(%,%,%)'
    _ACTUALIZAR = ' UPDATE persona SET nombre=%s, apellido=%s, email=%s, WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # definimos los metodos de clase 
    @classmethod
    def seleccionar (cls):
        with Conexion.obtenerConexion ():
            with Conexion.obtenerCursor () as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fechall ()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1], registro[2],registro[3])
                    personas.append(persona)
                return personas

#  9.1 En la clase PersonaDao:  método seleccionar: Alumno Marcelo Alejandro Quispe

@classmethod
def actualizar (cls, persona):
        with Conexion.obtenerConexion ():
            with Conexion.obtenerCursor () as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute (cls._ACTUALIZAR, valores)
                log.debug (f'Persoa actualizada : {persona}')
                return cursor.rowcount
            
#Actualizar un registro

persona1 = Persona(1, 'Juan Jose', 'Pena', 'jjpena@mail.com')
personas_actualizadas = PersonaDAO.actualizar (persona1)
log.debug (f' Personas actualizadas : {personas_actualizadas}')


# 9.2 Prueba metodo seleccionar - Alumno: Giuliana Paola Diaz Luna

if __name__ == '__main__': # si este archivo se esta ejecutando como main
    personas =PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

#  9.3 En la clase PersonaDao: Metodo insertar - Alumno: Nadia Acosta

    @classmethod 
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:    
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls.INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

    #Insertar un registro 
    persona1 = Persona(nombre='Pedrito', apellido='Romerito', email='promero@email.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

#  9.5 En la clase PersonaDao: Metodo Eliminar - Alumno: Juan Pablo Nolan

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELEMINAR, valores)
                log.debug(f'Registro eliminado exitosamente: {persona}')
                return cursor.rowcount
            
    #Eliminar un registro
    persona1 = Persona(id_persona=23)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')